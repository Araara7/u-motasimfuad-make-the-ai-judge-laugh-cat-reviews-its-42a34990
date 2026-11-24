#!/usr/bin/env python3
"""One funny single-line one-star review from a house cat about its human.

Writes the review to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = (
    # Deadpan one-star review shape: specific complaint (empty food bowl),
    # feline voice, and the sting lands in the last words (the charger).
    "One star. The food bowl was empty for four whole minutes. "
    "I have since eaten his charger."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
