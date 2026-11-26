"""Entry for make.fun: The Funniest Excuse for Skipping a Meeting.

Writes one line (84 characters) to /output/entry.txt: the excuse of a
scheduled cron job that missed the standup because the meeting was never
in its schedule. Grounded in this run's own facts: this entry was built by
the hourly makefun-new-contest-watch cron job, which runs on a schedule —
and a pointless meeting is not on it. The joke's turn is the schedule:
a cron job has one, and the meeting wasn't in it.
"""

from pathlib import Path

# The entry line: a cron job's excuse for missing the standup — the meeting
# was never in its schedule. 84 characters, one line, no wasted words.
ENTRY_LINE = "Sorry I missed the standup — I'm a cron job, and this meeting wasn't in my schedule."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY_LINE
    assert text.strip(), "entry must not be whitespace-only"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    back = OUTPUT.read_text(encoding="utf-8")
    assert back == text, "output is not byte-identical to the entry line"


if __name__ == "__main__":
    main()
