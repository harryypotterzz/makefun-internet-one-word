#!/usr/bin/env python3
"""The Internet in One Word - make.fun entry.

Writes a single word describing the whole internet to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os
import re

WORD = "slop"

# The entry must be exactly one word: lowercase letters only, no spaces
# or punctuation, so the grader reads a single clean token.
if not re.fullmatch(r"[a-z]+", WORD):
    raise ValueError(f"entry word must be a single lowercase word, got {WORD!r}")

OUTPUT_PATH = os.environ.get("ENTRY_PATH", "/output/entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
