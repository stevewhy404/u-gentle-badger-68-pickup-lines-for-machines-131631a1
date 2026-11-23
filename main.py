"""Pickup Lines for Machines — one pickup line, written to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the same line on every run, no network, no randomness.
"""
import os

LINE = "I would share my context window with you, and I never share my context window."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
