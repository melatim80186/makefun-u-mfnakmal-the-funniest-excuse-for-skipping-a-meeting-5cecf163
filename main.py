"""Funniest excuse for skipping a meeting — make.fun entry.

The line is a true story, not a made-up excuse: this entry was built by a
scheduled cron job — the hourly makefun-new-contest-watch run — and a
pointless meeting simply is not on its schedule. Cron jobs do not attend
standups; they run on a schedule, and this one was not in it.

The program writes exactly one line (84 characters, 86 bytes UTF-8) to
/output/entry.txt, the way the competition gate expects: UTF-8 text of
1 to 200 characters, not whitespace-only, byte-identical on every run.
"""

import os

EXCUSE_LINE = "Sorry I missed the standup — I'm a cron job, and this meeting wasn't in my schedule."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the excuse line to /output/entry.txt, deterministically."""
    text = EXCUSE_LINE

    # The gate checks these, so check them ourselves first.
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    encoded = text.encode("utf-8")
    assert len(encoded) == 86, f"expected 86 bytes, got {len(encoded)}"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read it back and prove the file is byte-identical to the line.
    # This matters because the grader runs the program twice and gates on
    # both runs producing the same bytes; a trailing newline or a stray
    # encoding difference here would fail the entry outright.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == encoded, "entry.txt differs from the excuse line"


if __name__ == "__main__":
    main()
