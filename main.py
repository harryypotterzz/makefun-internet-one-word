#!/usr/bin/env python3
"""The Internet in One Word - make.fun entry.

Writes a single word describing the whole internet to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

WORD = "slop"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
