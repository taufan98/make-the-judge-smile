#!/usr/bin/env python3
"""Make the Judge Smile — make.fun bounty entry.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt. Deterministic, standard library only,
no network, no environment secrets.
"""

import os

ENTRY = (
    "At dawn the street cat that always hisses at me trotted over, "
    "dropped a wet leaf at my feet, and waited \u2014 like it had finally "
    "decided we were friends."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "entry must be a single line"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = "output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")

    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
