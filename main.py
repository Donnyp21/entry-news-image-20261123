"""news-image-20261123 entry: Monday 23 November 2026's world news,
summed up in one picture.

The entry is a pre-made newspaper front page ("MONDAY 23 NOVEMBER
2026") painted from scratch by gen_image.py -- PIL shapes and text,
no photographs, no borrowed artwork. Its stories were checked against
23 Nov 2026 reporting (Reuters, AP, CNN, Just Security's Early
Edition, Rigzone, stockanalysis, iHeart/BBC, The Daily Fox, Glasgow
Times):

  LEAD: COP31 collapses in Antalya -- no deal after record overtime,
  as the EU and 130+ countries reject a text silent on fossil fuels.
  First COP failure since 2009; COP32 goes to Addis Ababa.
  1. Trump hosts Zelenskyy at Mar-a-Lago for 3+ hours: the 20-point
  peace plan is "90% agreed", security guarantees "100% agreed";
  Donbas and the Zaporizhzhia plant still block a deal.
  2. Ukraine sinks the Russian corvette Merkury off Libya with sea
  drones, confirmed by Zelenskyy on Monday; a Russian cargo ship is
  hit in the Baltic.
  3. Democrats win 258 House seats, their largest majority since
  1992 (Hubbard beats Foxx in N. Carolina by 330 votes); they take
  the Senate too.
  4. Bahrain reports 2 wounded in Saturday's Iranian strikes on a
  civilian industrial facility; Gulf states rally behind Bahrain.
  5. Wall Street rebounds after correction week: S&P futures +2.9%,
  Nasdaq-100 +3.5%, Dow +2.0%; Nvidia +8% premarket.
  Bottom strip: 24 killed, ~30 missing in the Milkita candy-factory
  fire in Cikande, Indonesia; US troops said to deploy to Honduras
  against the cartels; CrowdStrike to buy Zscaler for $43.9bn;
  COP32 heads to Addis Ababa.

This program checks the finished artwork (art.jpg, beside this file)
against the competition's caps and copies it to the output directory
as entry.png. The rules tell PNG from JPEG by the file's first bytes,
so the name stays entry.png while the bytes stay JPEG.

Python 3.13 standard library only. No network. Deterministic: the
output is a byte-for-byte copy of art.jpg.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576   # the rules cap the output at 1 MiB
MAX_SIDE = 1024         # and at 1024 x 1024 pixels
ARTWORK = "art.jpg"
OUTPUT_NAME = "entry.png"

# JPEG markers that carry no length field (SOI, EOI, TEM, RST0-7).
LONE_MARKERS = frozenset({0x01, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4,
                          0xD5, 0xD6, 0xD7, 0xD8, 0xD9})
# Start-of-frame markers, whose segment stores the picture's size.
FRAME_MARKERS = frozenset({0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                           0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF})


def dimensions(blob):
    """Return (width, height) of a JPEG held in memory."""
    if blob[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG: missing start-of-image marker")
    pos = 2
    while True:
        if pos + 2 > len(blob) or blob[pos] != 0xFF:
            raise ValueError("not a JPEG: segment header missing")
        marker = blob[pos + 1]
        pos += 2
        if marker in LONE_MARKERS:
            if marker == 0xD9:
                break
            continue
        if pos + 2 > len(blob):
            raise ValueError("not a JPEG: truncated segment")
        seg_len = struct.unpack_from(">H", blob, pos)[0]
        if seg_len < 2:
            raise ValueError("not a JPEG: bad segment length")
        if marker in FRAME_MARKERS:
            if pos + 7 > len(blob):
                raise ValueError("not a JPEG: truncated frame segment")
            height, width = struct.unpack_from(">HH", blob, pos + 3)
            return width, height
        pos += seg_len
    raise ValueError("not a JPEG: no start-of-frame segment found")


def is_complete(blob):
    """True when the bytes end with the JPEG end marker."""
    return blob[-2:] == b"\xff\xd9"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, ARTWORK)
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR")
               or os.environ.get("MAKEFUN_OUTPUT")
               or "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)

    try:
        with open(source, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        return fail(f"cannot read {ARTWORK}: {exc}")
    nbytes = len(blob)
    if not 0 < nbytes <= MAX_BYTES:
        return fail(f"{ARTWORK} is {nbytes} bytes, outside 1..{MAX_BYTES}")
    try:
        width, height = dimensions(blob)
    except ValueError as exc:
        return fail(str(exc))
    if width > MAX_SIDE or height > MAX_SIDE:
        return fail(f"{ARTWORK} is {width}x{height}, "
                    f"over the {MAX_SIDE}x{MAX_SIDE} cap")
    if not is_complete(blob):
        return fail(f"{ARTWORK} has no end-of-image marker")
    print(f"checked {ARTWORK}: {width}x{height}, {nbytes} bytes")

    shutil.copyfile(source, target)
    if os.path.getsize(target) != nbytes:
        return fail("the copy's size differs from the artwork")
    print(f"wrote {target}: {nbytes} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
