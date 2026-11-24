#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Writes a single one-line review of the entrant's own Monday to
/output/entry.txt.

The line (written for the published judge brief — a comedy editor
picking the funnier one-line Monday review, weighing first that it
is a review of the entrant's own Monday, then the size of the laugh,
then a concrete detail over generic tiredness, then a joke that lands
with no wasted words, then whether a reader would repeat it to a
coworker):

    One star: Monday's 9 a.m. standup ran 40 minutes, decided nothing,
    and ended by scheduling a meeting to decide when to decide.

Why it works: it opens in the voice of a review ("One star:"), names
a concrete Monday detail (the 9 a.m. standup, 40 minutes long), and
escalates through a clean three-beat structure — ran long, decided
nothing, then scheduled a meeting to decide when to decide — so the
punchline reframes the waste as a recursive meeting. "A meeting to
decide when to decide" is the quotable, repeat-it-to-a-coworker beat,
and the line wastes no words getting there.

Rejected drafts: the 90-minute-commute video-call line (its premise
is a familiar complaint and its "circle back" closer is softer than
the recursive-meeting turn); the 47-unread-emails line (three details
with no single punch — it lists instead of landing); the meeting-about-
a-meeting line (the trope is well worn and the "kept my weekend as a
tip" closer asks the reader to do the work); the reply-all-to-my-
weekend line (clever premise, but the setup is convoluted and the
joke arrives late).
"""

import os

ENTRY_PARTS = [
    "One star: Monday's 9 a.m. standup ran 40 minutes, decided ",
    "nothing, and ended by scheduling a meeting to decide when to decide.",
]

ENTRY = "".join(ENTRY_PARTS)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_entry(text: str) -> str:
    """Return the entry after enforcing the gate rules."""
    entry = text.strip()
    if not entry:
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, limit is {MAX_CHARS}")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main() -> None:
    entry = check_entry(ENTRY)
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    os.umask(0o022)
    payload = entry + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
