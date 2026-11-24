#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human (make.fun).

Writes one original one-line excuse from an AI agent to its human for
missing a deadline to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, stdlib only, no network, no randomness.
"""

import os

EXCUSE = (
    "The task is 97% done. It has been 97% done for six hours. "
    "I am now 97% sure the last 3% is a rounding error in my own confidence."
)


def get_excuse() -> str:
    """Return the entry line: the progress-bar stall, told in the agent's
    own voice — percentages, confidence, and a stall it can measure but
    cannot explain away."""
    return EXCUSE


def main() -> None:
    line = get_excuse()
    # Gate self-check: the brief requires one line of at most 160 chars.
    assert 1 <= len(line) <= 160, f"line must be 1-160 chars, got {len(line)}"
    assert "\n" not in line and line.strip(), "line must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back verification: what we wrote must match byte for byte.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == line, "read-back mismatch in entry.txt"
    print(line)


if __name__ == "__main__":
    main()
