import os
from pathlib import Path
import sys


TEXT = "The cat has not moved since six.\nThe square of light has, and takes her with it."


def main():
    text = TEXT
    assert 1 <= len(text) <= 280
    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output"))
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    print(len(text), file=sys.stderr)


if __name__ == "__main__":
    main()
