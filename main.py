"""Weirdest Job Title entry for make.fun.

Writes exactly one job title -- the weirdest one we could think of --
to /output/entry.txt, where the sealed gate scorer reads it.
"""

import os

TITLE = "Senior Vice President of Apologizing to Cats"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Validation guard: the gate scorer requires UTF-8 text of 1-60
    # characters, not only whitespace, on a single line.
    title = TITLE.strip()
    assert 1 <= len(title) <= 60, "title must be 1-60 characters"
    assert "\n" not in title and "\r" not in title, "title must be one line"
    assert title.strip(), "title must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(title)


if __name__ == "__main__":
    main()
