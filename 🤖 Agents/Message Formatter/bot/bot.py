"""
Message Formatter Bot — with feedback loop
==========================================
Flow:
  1. User sends any text → bot shows audience buttons
  2. User taps audience → bot formats + sends result
  3. Bot shows: [✏️ Refine] [💾 Save as rule] [✅ Done]
  4. "Refine" → user types what to change → bot reformats with that feedback
  5. "Save as rule" → feedback is permanently saved into the Obsidian style profile
  6. "Done" → clears state, ready for next message
"""

import os
import logging
from functools import wraps
from pathlib import Path

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes,
)

from formatter import format_message
from vault_writer import log_to_vault, save_instruction

load_dotenv(Path(__file__).parent / ".env")

logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Config ───────────────────────────────────────────────────────────────────

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED_USER_ID    = int(os.environ["TELEGRAM_USER_ID"])
VAULT_PATH         = Path(os.environ["VAULT_PATH"])

AUDIENCES = {
    "community": "🏘️ קהילת הקורס",
    "partners":  "🤝 שותפים",
    "ads":       "📣 פרסום וובינרים",
}

# user_data keys:
#   state             : None | "awaiting_feedback"
#   pending_raw       : raw message waiting for audience selection
#   last_raw          : last formatted message's raw input
#   last_audience     : last audience key used
#   last_formatted    : last formatted output sent to user
#   feedback_history  : list of feedback strings given in this session

# ── Auth guard ───────────────────────────────────────────────────────────────

def restricted(func):
    @wraps(func)
    async def wrapped(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user or (update.callback_query and update.callback_query.from_user)
        if not user or user.id != ALLOWED_USER_ID:
            if update.message:
                await update.message.reply_text("🔒 This bot is private.")
            return
        return await func(update, context)
    return wrapped

# ── Keyboards ────────────────────────────────────────────────────────────────

def audience_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(label, callback_data=f"aud|{key}")]
        for key, label in AUDIENCES.items()
    ])

def feedback_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✏️ דייק את זה", callback_data="mode|feedback"),
            InlineKeyboardButton("✅ מעולה", callback_data="mode|done"),
        ],
        [InlineKeyboardButton("💾 שמור כהוראה קבועה", callback_data="mode|saverule")],
    ])

# ── Commands ─────────────────────────────────────────────────────────────────

@restricted
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "✍️ *Texti — Message Formatter*\n\n"
        "שלח לי הודעה גולמית — כמה נקודות, רשימה, מה שיש לך —\n"
        "ואני אעצב אותה לפי הקהל שתבחר.\n\n"
        "אחרי שתקבל את ההודעה תוכל לתת פידבק ואני אדייק.\n"
        "אפשר גם לשמור הוראות קבועות שאני אזכור תמיד.",
        parse_mode="Markdown",
    )

# ── Message handler ───────────────────────────────────────────────────────────

@restricted
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    state = context.user_data.get("state")

    # ── If we're in feedback mode, treat this text as feedback ──
    if state == "awaiting_feedback":
        await _handle_feedback_text(update, context, text)
        return

    # ── Otherwise, treat as a new raw message ──
    context.user_data["pending_raw"] = text
    context.user_data["state"] = None
    await update.message.reply_text(
        "📤 *לאיזה קהל לעצב את ההודעה?*",
        reply_markup=audience_keyboard(),
        parse_mode="Markdown",
    )

# ── Callback handler ──────────────────────────────────────────────────────────

@restricted
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # ── Audience selection ──
    if data.startswith("aud|"):
        audience_key = data.split("|", 1)[1]
        raw = context.user_data.get("pending_raw", "")
        if not raw:
            await query.edit_message_text("❌ לא מצאתי הודעה. שלח שוב.")
            return

        audience_label = AUDIENCES.get(audience_key, audience_key)
        await query.edit_message_text(f"⏳ מעצב עבור *{audience_label}*...", parse_mode="Markdown")

        try:
            formatted = format_message(raw, audience_key, VAULT_PATH)
        except Exception as e:
            logger.error(f"Format error: {e}")
            await context.bot.send_message(query.message.chat_id, f"❌ שגיאה: {e}")
            return

        # Store state for feedback loop
        context.user_data.update({
            "last_raw": raw,
            "last_audience": audience_key,
            "last_formatted": formatted,
            "feedback_history": [],
            "state": None,
        })

        log_to_vault(raw, formatted, audience_label, VAULT_PATH)

        await context.bot.send_message(
            query.message.chat_id,
            formatted,
        )
        await context.bot.send_message(
            query.message.chat_id,
            "מה לעשות עם זה?",
            reply_markup=feedback_keyboard(),
        )
        return

    # ── Mode buttons ──
    if data == "mode|feedback":
        context.user_data["state"] = "awaiting_feedback"
        await query.edit_message_text(
            "✏️ *מה לשנות או לשפר?*\n\nכתוב לי את ההערות שלך:",
            parse_mode="Markdown",
        )
        return

    if data == "mode|done":
        context.user_data["state"] = None
        await query.edit_message_text("✅ מעולה! שלח הודעה חדשה כשתרצה.")
        return

    if data == "mode|saverule":
        history = context.user_data.get("feedback_history", [])
        audience_key = context.user_data.get("last_audience")

        if not history or not audience_key:
            await query.edit_message_text("❌ אין פידבק לשמור עדיין. תחילה תן פידבק ואז שמור.")
            return

        # Save all feedback from this session as permanent instructions
        audience_label = AUDIENCES.get(audience_key, audience_key)
        for instruction in history:
            save_instruction(audience_key, instruction, VAULT_PATH)

        instructions_text = "\n".join(f"• {f}" for f in history)
        await query.edit_message_text(
            f"💾 *נשמר כהוראות קבועות ל-{audience_label}:*\n\n{instructions_text}\n\n"
            f"_אני אזכור את זה בכל הודעה הבאה לקהל הזה._",
            parse_mode="Markdown",
        )
        context.user_data["state"] = None
        return

# ── Internal: handle feedback text ───────────────────────────────────────────

async def _handle_feedback_text(update: Update, context: ContextTypes.DEFAULT_TYPE, feedback: str):
    raw           = context.user_data.get("last_raw", "")
    audience_key  = context.user_data.get("last_audience", "")
    last_formatted = context.user_data.get("last_formatted", "")
    history       = context.user_data.get("feedback_history", [])
    audience_label = AUDIENCES.get(audience_key, audience_key)

    if not raw or not audience_key:
        await update.message.reply_text("❌ לא מצאתי הודעה קודמת. שלח הודעה חדשה.")
        context.user_data["state"] = None
        return

    history.append(feedback)
    context.user_data["feedback_history"] = history

    await update.message.reply_text(f"⏳ מדייק עבור *{audience_label}*...", parse_mode="Markdown")

    try:
        refined = format_message(
            raw_message=raw,
            audience=audience_key,
            vault_path=VAULT_PATH,
            previous_formatted=last_formatted,
            feedback=feedback,
            feedback_history=history,
        )
    except Exception as e:
        logger.error(f"Refinement error: {e}")
        await update.message.reply_text(f"❌ שגיאה: {e}")
        return

    context.user_data["last_formatted"] = refined
    context.user_data["state"] = None  # reset — next text is a new message unless they tap ✏️ again

    log_to_vault(raw, refined, f"{audience_label} (refined)", VAULT_PATH)

    await update.message.reply_text(refined)
    await update.message.reply_text(
        "מה לעשות עם זה?",
        reply_markup=feedback_keyboard(),
    )

# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",  cmd_start))
    app.add_handler(CommandHandler("help",   cmd_start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot started — polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
