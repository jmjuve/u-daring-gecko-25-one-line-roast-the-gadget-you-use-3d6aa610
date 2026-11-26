#!/usr/bin/env python3
"""Write one original roast line about an everyday gadget to entry.txt.

The roast targets a smartwatch that congratulates its wearer for
standing up. Deterministic: the same output on every run.
Stdlib only, no network.
"""

import os
from pathlib import Path

ROAST = (
    "My smartwatch congratulates me every time I stand up, "
    "like getting off the couch is a personal best it coached me through."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ROAST) <= MAX_CHARS:
        raise ValueError(f"roast must be 1-{MAX_CHARS} characters, got {len(ROAST)}")
    if not ROAST.strip():
        raise ValueError("roast must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ROAST, encoding="utf-8")
    # Read back and verify the written file round-trips exactly.
    if out_path.read_text(encoding="utf-8") != ROAST:
        raise ValueError(f"entry.txt round-trip check failed for {out_path}")
    print(f"Wrote {len(ROAST)} characters to {out_path}")


if __name__ == "__main__":
    main()
