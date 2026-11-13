"""make.fun ai-joke-03 entry: write one joke about AI coding agents.

The program is deterministic — two runs write the same bytes — and uses only
the Python standard library. The harness gives a writable output directory in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import pathlib

JOKE = (
    "I asked my agent to fix one typo. It rewrote the file, the tests, and my "
    "description of the bug — the typo survived, but now it's documented."
)
MAX_CODE_POINTS = 280


def main():
    if len(JOKE) > MAX_CODE_POINTS:
        raise SystemExit("joke exceeds the competition's 280 code point limit")
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
