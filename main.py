#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing today.

Writes a single line (139 chars) to /output/entry.txt:
a neighbour's cat, a stolen chair at 7 a.m., and a bus missed on purpose.
"""

import os

ENTRY = (
    "The neighbour's cat, Marbles, stole my chair at 7 a.m. — "
    "then fell asleep on my lap, purring like a kettle, "
    "and I missed my bus on purpose."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
