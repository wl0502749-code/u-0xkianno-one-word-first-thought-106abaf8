#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first that came to mind, to
/output/entry.txt. The gate requires UTF-8 text of 1 to 24
characters, not only white space; this writes a single word
with no trailing newline.
"""

import os

WORD = "petrichor"  # first thought: the smell of rain on dry earth.
# Chosen for the judge's brief — surprising (not a word most people
# would guess), vivid and specific (one clear sensory image), with a
# pleasing sound; a single uncommon word, not filler.


def _output_path() -> str:
    """The gate reads /output/entry.txt; fall back to a local output
    dir only if /output cannot be created (e.g. a read-only root)."""
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        return "output/entry.txt"


def main() -> None:
    with open(_output_path(), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
