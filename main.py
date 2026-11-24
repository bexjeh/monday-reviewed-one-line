#!/usr/bin/env python3
"""Write a one-line review of the entrant's own Monday to entry.txt."""
import os
from pathlib import Path

LINE = "My Monday inbox hit 214 unread emails, so I closed the laptop and called that a reply."

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
