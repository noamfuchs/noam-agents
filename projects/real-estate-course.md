---
name: Real Estate Course
status: active
goal: "Produce 12-chapter Hebrew online course for Israeli real estate investors"
started: 2026-04
---

# Real Estate Course

**Goal:** 12-chapter Hebrew online course for Israeli real estate investors. Conversational, sharp, direct — not academic.
**Speaker:** Amit
**Partner:** Itay
**Format:** Word .docx scripts, 3,000–4,000 Hebrew words per chapter (~60 min each).
**Current state:** Chapters 1–3 done. Chapters 4–12 pending.

## Chapter status
- [x] 1
- [x] 2
- [x] 3
- [ ] 4 _(source PDFs available)_
- [ ] 5 _(source PDFs available)_
- [ ] 6 _(source PDFs available)_
- [ ] 7 _(source PDFs available)_
- [ ] 8 _(source PDFs available)_
- [ ] 9 _(source TBA)_
- [ ] 10 _(source TBA)_
- [ ] 11 _(source TBA)_
- [ ] 12 _(source TBA)_

## Stakeholders
- [[people/amit]] — speaker
- [[people/itay]] — partner

## Open items
- [ ] Draft chapter 4 script
- [ ] Sync with Amit on chapter 4 voice/pacing

## Production workflow (added 2026-06-03)
- **Input:** PDF slide deck (numbered PART 1, PART 2, ...).
- **Output:** Word `.docx` script (`פרק_NN_תסריט.docx`), Hebrew, 3,000–4,000 words (about 60 min).
- **Process:** extract deck with `pdftotext` → write expanded Hebrew script following the approved ch.1–3 style → structure as Heading 1 (chapter title), Heading 2 (sections), Normal paragraphs, bracketed stage directions like `[מצגת: ...]`, `[הפסקה קצרה]`, `[דוגמה אישית: ...]` → build `.docx` with python-docx → send to Amit for voice/pacing review.
- **Locations:** scripts → `~/Desktop/clawed bot/קורס/פרקים/`; source PDFs → `~/Desktop/clawed bot/קורס/חומרים/` (old) and `~/Desktop/clawed bot/קורס/חומרים חדש/` (PART 3–8). PART 9–12 PDFs supplied later.

## Notes
- Output language: Hebrew
- Tone: conversational, sharp, direct, not academic
