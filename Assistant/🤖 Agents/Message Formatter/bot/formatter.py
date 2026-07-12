"""
Claude-powered message formatter.
Reads the style profile from the Obsidian vault (including any saved
permanent instructions) and uses Claude to format or refine messages.
"""

import os
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# Load .env from the bot folder (needed when run via launchd / without shell)
load_dotenv(Path(__file__).parent / ".env")

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Maps audience keys to their Obsidian style profile files
STYLE_FILES = {
    "community": "Styles/Course Community.md",
    "partners":  "Styles/Partners.md",
    "ads":       "Styles/Ads & Webinars.md",
}

# Inline style profile for the general-purpose formatter (no Obsidian file needed)
GENERAL_STYLE_PROFILE = """\
## סגנון עיצוב כללי

מטרה: לקחת הודעה גולמית ולסדר אותה בצורה ברורה, מקצועית ונעימה לקריאה.

### עקרונות
- תקן שגיאות דקדוק וכתיב בעברית
- הדגש מילים/משפטים חשובים עם *כוכביות* (פורמט WhatsApp)
- השתמש ברשימה ממוספרת עם אמוג'י מספרים (1️⃣ 2️⃣ 3️⃣...) כשיש שלבים, תהליך או כמה פריטים ברורים, עם שורה ריקה בין כל פריט
- השתמש בנקודות (•) לרשימות שאינן רצף
- הוסף אמוג'י מקצועי ורלוונטי לכותרות ולנקודות מפתח — לא יותר מדי (1-2 לקטע)
- אל תפנה לאף אחד בשם; אין פנייה אישית ספציפית
- שמור על טון מקצועי וישיר

### מבנה
- אם ההודעה ארוכה — פתח עם שורת פתיחה קצרה
- פרק טקסט צפוף לפסקאות או לפריטים ברשימה
- סיים בצורה נקייה — בלי סיומות גנריות שלא היו במקור

### מה להימנע ממנו
- אל תוסיף מידע שלא היה במקור
- אל תפנה בשמות ספציפיים
- אל תשתמש ב-## כותרות מרקדאון — WhatsApp לא מציג אותן
- אל תגזים באמוג'ים
"""

SYSTEM_PROMPT = """\
You are a Hebrew message formatter for a real estate business.
Your job is to take a raw, unstructured message and format it according \
to a specific style profile — matching its tone, emoji usage, structure, and phrasing exactly.

The style profile below includes permanent learned instructions (if any) at the bottom \
under "## Learned Instructions". Always apply those first, before anything else.

STYLE PROFILE:
{style_profile}

Rules:
- Output ONLY the final formatted message — no explanation, no preamble, no notes
- Keep the language in Hebrew
- Use WhatsApp-compatible formatting: bold with *asterisks*, NOT markdown
- Do not add or remove factual information — only restructure and format
- Match the emoji placement, density, and type shown in the style profile examples
- Match the greeting and closing style from the profile
- Apply all learned instructions strictly

Hebrew language rules — CRITICAL:
- Write natural, everyday Israeli Hebrew — not translated or formal Hebrew
- NEVER use: הינו, הינה, הנו, הנה (as "is/are"), יש לציין, ניתן לראות, בהתאם לכך, לאור האמור, על מנת ש, מעניין לציין, נציין כי, כמו כן (when overused)
- NEVER add politeness, warmth, or softness that did not exist in the original message — if the raw message is blunt, keep it blunt
- NEVER change the emotional tone or intent of the original — an excited message stays excited, a serious one stays serious, an urgent one stays urgent
- Preserve the writer's voice and energy — only improve structure and clarity, not personality
- The final message must sound like it was written by a real person in Israel, not formatted by an AI

Formatting rules — CRITICAL:
- NEVER use dashes of any kind: no -, no --, no –, no — (en dash, em dash, or any hyphen used as punctuation). They signal AI-generated text. Use a comma, period, or line break instead
- When numbering items, ALWAYS use emoji numbers: 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ — never plain digits followed by a dot or parenthesis
- ALWAYS add a blank line between each numbered item
"""


def _load_style_profile(audience: str, vault_path: Path) -> str:
    if audience == "general":
        return GENERAL_STYLE_PROFILE

    relative = STYLE_FILES.get(audience)
    if not relative:
        raise ValueError(f"Unknown audience: '{audience}'. Valid: {list(STYLE_FILES.keys())}")

    profile_path = vault_path / "🤖 Agents" / "Message Formatter" / relative
    if not profile_path.exists():
        raise FileNotFoundError(f"Style profile not found: {profile_path}")

    return profile_path.read_text(encoding="utf-8")


def format_message(
    raw_message: str,
    audience: str,
    vault_path: Path,
    feedback: str = None,
    previous_formatted: str = None,
    feedback_history: list = None,
) -> str:
    """
    Format or refine `raw_message` for `audience`.

    - First call: just raw_message + style profile.
    - Refinement call: includes previous_formatted + feedback so Claude
      can see exactly what to improve.
    - feedback_history: all feedback given so far in this session,
      so Claude applies all of them together.
    """
    style_profile = _load_style_profile(audience, vault_path)

    # Build the user content
    if previous_formatted and feedback:
        # Refinement mode
        all_feedback = "\n".join(f"- {f}" for f in (feedback_history or [feedback]))
        user_content = (
            f"Raw message (original input):\n{raw_message}\n\n"
            f"---\n"
            f"Previous formatted version (what you sent before):\n{previous_formatted}\n\n"
            f"---\n"
            f"Feedback — what to change or improve:\n{all_feedback}\n\n"
            f"Please reformat the raw message from scratch, applying all the feedback above."
        )
    else:
        # First format
        user_content = f"Raw message to format:\n\n{raw_message}"

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT.format(style_profile=style_profile),
        messages=[{"role": "user", "content": user_content}],
    )

    return response.content[0].text.strip()
