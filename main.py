"""The Threatening Cactus - one funny line for the One-Line Laugh-Off.

The program writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output), with no trailing newline. The bounty's gate: entry.txt must be
UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

TEXT = "I told my therapist I talk to my plants. She asked if they answer back. I said only the cactus, and only in threats."
# Why this line: a confession that sounds normal, then two turns the reader
# does not see coming - first the plants answer back, then only the cactus
# does, and only in threats. The punch word lands last, the line stays short
# (116 chars), and the joke is a fresh angle: no knock-knock, no bar, no
# "walks into" setup, just a therapy session going quietly wrong.


def gate(text):
    """Check the 1-200 character gate: UTF-8, 1-200 chars, not only
    whitespace, no leading or trailing whitespace, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry is %d chars, gate is 1-200" % len(text))
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    gate(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    read_back = raw.decode("utf-8")
    if read_back != TEXT:
        raise ValueError("read-back differs from TEXT")
    gate(read_back)
    print("wrote %d chars to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
