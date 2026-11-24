"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Gate: 1-120 characters, one line, not whitespace.
"""

import os

LINE = "ERROR: Crumb tray full. I am now 90% crumbs and legally a different appliance."

assert 1 <= len(LINE) <= 120, f"line must be 1-120 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only whitespace"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()

assert written == LINE, "round-trip check failed: file content differs from LINE"
assert not written.endswith("\n"), "entry must be exactly one line, no trailing newline"
assert len(written.encode("utf-8")) == len(LINE), "entry must be plain ASCII-length bytes"
print(f"wrote {len(LINE)} chars to /output/entry.txt")
