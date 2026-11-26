"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one fixed satirical sentence to entry.txt in the output
directory. The sentence is a single line, well under the 320-character
gate, and it is written exactly the same on every run: no clock, no
randomness, no network, no model calls, standard library only.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys


ROAST = (
    "They drafted four hundred pages of law to govern artificial "
    "intelligence, then stalled the vote because nobody in the room "
    "could turn the draft itself into a PDF."
)

MAX_CHARS = 320


def check_line(line):
    """Refuse anything that would fail the gate, before writing."""
    if not line or not line.strip():
        raise ValueError("roast line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError("roast line is %d chars, over %d" % (len(line), MAX_CHARS))
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("roast line must be exactly one sentence")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    return line


def output_path():
    """Where the grader expects the text: $MAKEFUN_OUTPUT_DIR, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main(argv):
    line = check_line(ROAST)
    if len(argv) > 1:
        target = argv[1]
    else:
        target = output_path()
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
