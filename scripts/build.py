#!/usr/bin/env python3
"""Validate that the complete original UI source is preserved.

Git/GitHub can normalize text file line endings from CRLF to LF.
The integrity comparison treats ONLY these two newline encodings as equivalent;
all other bytes must match the exact uploaded original content.
"""
from pathlib import Path
import argparse
import hashlib

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "original" / "Reaper_X_New_UI__unaltered.txt"
SRC = ROOT / "src" / "KIDzUIx4.luau"
DIST = ROOT / "dist" / "KIDzUIx4.lua"

# Reference: Reaper X New UI(2).txt, 442,747 bytes with CRLF line endings.
ORIGINAL_CRLF_SHA256 = "b4cfc7170e8a0e119f7d18547bb906da1792b7f6ec17fc8e984aec07cf57058c"
# Same exact text, with CRLF converted to LF (no other changes allowed).
ORIGINAL_LF_SHA256 = "8bea13a05d54bd5b10b44a99fdc17da6633ed3007c0b58415b070fab693f27ca"


def normalize_newlines(contents: bytes) -> bytes:
    """Make CRLF and LF compare equally; do not trim, reformat or delete code."""
    return contents.replace(b"\r\n", b"\n")


def sha256(contents: bytes) -> str:
    return hashlib.sha256(contents).hexdigest()


def build(check=False):
    original = ORIGINAL.read_bytes()
    normalized_original = normalize_newlines(original)
    original_hash = sha256(original)
    normalized_hash = sha256(normalized_original)

    if normalized_hash != ORIGINAL_LF_SHA256:
        raise AssertionError(
            "Original content mismatch (not merely CRLF/LF conversion). "
            f"Expected normalized SHA-256 {ORIGINAL_LF_SHA256}; got {normalized_hash}. "
            "Restore the original file from the verified upload/ZIP."
        )
    if not normalized_original.startswith(b"local UI = (function()"):
        raise AssertionError("Unexpected original beginning")
    if not normalized_original.rstrip().endswith(b"end)()"):
        raise AssertionError("Unexpected original ending")

    # Append export without touching any of the actual source bytes.
    newline = b"\r\n" if b"\r\n" in original else b"\n"
    exported = original + newline + b"return UI" + newline
    expected_normalized = normalized_original + b"\nreturn UI\n"

    if check:
        for path in (SRC, DIST):
            if not path.exists():
                raise AssertionError(f"Missing file: {path}")
            actual_normalized = normalize_newlines(path.read_bytes())
            if actual_normalized != expected_normalized:
                raise AssertionError(
                    f"{path.relative_to(ROOT)} differs from original source + return UI "
                    "(beyond CRLF/LF line ending differences)"
                )
        print("PASS: complete original code preserved, and src/dist match with the export patch.")
        print(f"Original file SHA-256: {original_hash}")
        if original_hash != ORIGINAL_CRLF_SHA256:
            print("NOTE: line endings were normalized by Git/GitHub; original content is unchanged.")
    else:
        SRC.parent.mkdir(parents=True, exist_ok=True)
        DIST.parent.mkdir(parents=True, exist_ok=True)
        SRC.write_bytes(exported)
        DIST.write_bytes(exported)
        print("Built src/ and dist/ from the complete original (no deletions).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    build(parser.parse_args().check)
