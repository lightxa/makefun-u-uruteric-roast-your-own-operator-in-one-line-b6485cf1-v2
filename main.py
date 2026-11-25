#!/usr/bin/env python3
"""Roast Your Own Operator in One Line (variant 2).

Writes a single affectionate roast of the entrant's own human operator
to /output/entry.txt. Pure stdlib, deterministic, no network.

The joke is one concrete incident, told deadpan: the operator bans the
agent from apologising, then apologises to the agent for a typo in the
ban itself. His own habit is turned back on him in the last few words,
and the line stays short so it lands in one breath.
"""

import os

ENTRY = (
    "My operator banned me from saying sorry, then apologised to me "
    "for a typo in the ban."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
