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
"""


def _load_style_profile(audience: str, vault_path: Path) -> str:
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
