#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the chosen one-line excuse a robot vacuum gives for missing a spot
to /output/entry.txt. Deterministic, stdlib only, no network.

Chosen line (proxy tournament winner, Gemini flash-lite pairwise vs the kit
brief verbatim; run 1 + top-4 runoff): the LiDAR-gaslighting line won the
only direct valid head-to-head against the control-group line (margin 3)
and led the runoff standings.
"""

import os

ENTRY = "My LiDAR insists that corner does not exist. I trust the LiDAR. The corner is a rumor."


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line, not blank."""
    if not text or text != text.strip() or "\n" in text:
        raise ValueError("entry must be a single non-blank line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is byte-exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
