# RFS Mentor-Shortlist Page Generator

**Location:** `~/Downloads/run_for_startups/`
**Purpose:** Generates a self-contained HTML index page listing about 15 Run For Startups mentors/advisors (founders, VCs, investors) with photos, bios, tags, and contact links.
**Status:** Reference tool; not wrapped in a skill.

## Structure
- `build_page.py` - Python builder; base64-embeds images + text, outputs a single self-contained `index.html`.
- `assets/opt/` - optimized mentor photos (JPEGs).
- Per-mentor data: name, role, company + URL, badge, description, tags, LinkedIn URL, email + email-status (verified / public / guess).

## Related
- [[rfs-guest-onepagers]] - the guest one-pager PDFs (different tool, same community).
- [[adam-teer-run-for-startups]] - community owner.
