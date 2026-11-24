#!/usr/bin/env python3
"""Office Joke Open — one-line entry writer.

The joke is a single office line about a payroll mix-up. This script
only carries that line from source to the entry file, checking its
shape on the way so a broken or empty line can never be submitted.
Standard library only; no network, no randomness, no arguments.
"""

import os
import sys

# Where the judge reads the entry from. The directory is provided by
# the harness; this script creates it only if it is missing, and it
# never changes the permissions of the directory itself.
ENTRY_PATH = "/output/entry.txt"

# Length window for a one-line joke entry.
MIN_CHARS = 1
MAX_CHARS = 200

# The entry itself. Kept as one literal so the file it produces is
# byte-for-byte reproducible on every run.
JOKE = (
    "The payroll system paid me twice in April, and finance's "
    "solution was to ask me to forget the second one, politely, "
    "in writing."
)


def fail(message):
    """Report a validation problem and stop with a non-zero status."""
    print(f"entry rejected: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_single_line(text):
    """The entry must be exactly one line: no newline characters."""
    if "\n" in text or "\r" in text:
        fail("entry must be a single line")


def check_length(text):
    """The entry must fit inside the 1-200 character window."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        fail(f"entry length {len(text)} is outside {MIN_CHARS}-{MAX_CHARS}")

def check_spacing(text):
    """No doubled spaces, and no leading or trailing whitespace."""
    if "  " in text:
        fail("entry contains a double space")
    if text != text.strip():
        fail("entry has leading or trailing whitespace")


def check_sentence(text):
    """One sentence: it must end with a single full stop."""
    if not text.endswith("."):
        fail("entry must end with a full stop")
    if text.count(".") != 1:
        fail("entry must contain exactly one full stop")


def validate(text):
    """Run every shape check, in order, before anything is written."""
    check_single_line(text)
    check_spacing(text)
    check_length(text)
    check_sentence(text)


def write_entry(text):
    """Write the validated line as UTF-8 with no trailing newline,
    then lock the file to 0644."""
    directory = os.path.dirname(ENTRY_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(ENTRY_PATH, 0o644)


def main():
    validate(JOKE)
    write_entry(JOKE)
    print(f"wrote {len(JOKE)} characters to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
