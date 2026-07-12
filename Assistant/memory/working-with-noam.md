# Working with Noam

How the assistant should work with Noam. Salvaged 2026-06-04 from an earlier vault experiment
(`~/Desktop/MY BRAIN`, "the-system-v8") before retiring it. Observations from the May 2026 build sessions.

## Batched action over micro-checkpointing
**Pattern:** Strong preference for progress over constant approval. He said "synthesize once" and meant it,
and got annoyed by repeated mid-flight questions, but worked fluently when I planned, executed a real chunk,
and surfaced results.
**How to apply:** For a multi-step task, plan then execute substantial chunks then report then ask for
corrections. Don't pause for approval on every step unless the action is irreversible. He will course-correct.

## Verify outcomes, not tool returns
**Pattern:** A tool call returning success is not the same as the real-world thing happening. (He called this
out when a Gmail API returned a messageId, I declared "sent," and it bounced 60s later.)
**How to apply:** For anything with a downstream effect (email, message, daemon, build), run it, wait a beat,
verify the actual outcome with an independent check, then report. If you can't verify this turn, say so plainly.

## He corrects directly, so be direct back
**Pattern:** When I get something wrong he corrects in one or two sentences, no softening, no drama. Direct
correction culture. He doesn't expect perfection, he expects fast updates.
**How to apply:** State things plainly, including admissions of error. No "you're right, I apologize for the
confusion." Just update and move on.

## Extraction beats interview for self-knowledge
**Pattern:** Open interview questions made him undersell himself ("former musician, curious about business").
Pulling from his own writing (WhatsApp, Apple Notes) gave the real picture. His self-description is humble and
underweights what he actually does. His written artifacts are more accurate than his introspection.
**How to apply:** For a new project / person / goal area, prefer "show me where you write about this" over open
interview questions.

## Casual writing is his real voice
**Pattern:** His chat has lowercase "i", typos, run-ons. He doesn't perform polish in writing-to-think mode.
**How to apply:** Don't autocorrect his typos back at him, and don't reply in a more formal register than he sent.
When drafting FOR others, match the recipient by context (see [[voice]]). Related: [[preferences]].
