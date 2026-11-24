"""Worst AI Advice entry: write one line of the worst AI advice to /output/entry.txt.

No network, no randomness, no dependencies. Deterministic output.
"""

import os

ENTRY = "Pro tip: to charge your phone faster, microwave it for 30 seconds \u2014 the waves top up the battery in seconds."

# The gate caps the line at 140 characters; fail loudly instead of
# submitting a line the scorer would refuse.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters, must be 1-140"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
