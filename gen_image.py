"""Paint the news-image-20261123 front page: one picture that sums up
Monday 23 November 2026.

This file only runs at build time (here, with Pillow). The graded
program is main.py, which hands the finished art.jpg to the output
folder. Everything on the page is drawn with PIL primitives -- shapes
and text, no photos, no borrowed artwork -- so every headline reads
exactly as spelled below.

The day's stories, checked against reporting dated 23 Nov 2026 from
Reuters, AP, CNN, Just Security's Early Edition, Rigzone,
stockanalysis, iHeart/BBC, The Daily Fox and Glasgow Times:

  LEAD: the COP31 climate summit in Antalya ends with no deal after
  record overtime. The EU and 130+ countries reject a final text
  silent on fossil fuels -- the first COP failure since 2009, and
  COP32 moves to Addis Ababa. UN chief Guterres is "deeply
  disappointed".
  1. Trump hosts Zelenskyy at Mar-a-Lago for 3+ hours. The 20-point
  peace plan is "90% agreed" and US security guarantees are "100%
  agreed"; territory (Donbas) and the Zaporizhzhia nuclear plant
  still block a deal. Trump spoke to Putin for over an hour first
  and says the war is "maybe very close" to ending.
  2. Ukraine sinks the Russian corvette Merkury off Libya with sea
  drones, confirmed by Zelenskyy on Monday. A Russian cargo ship is
  hit in the Baltic; the Kremlin calls it "terrorist activity".
  3. Democrats win 258 House seats, their largest majority since
  1992: Chuck Hubbard beats Virginia Foxx in North Carolina's 5th
  by 330 votes after a recount. Democrats also take the Senate
  (54+ seats).
  4. Bahrain reports 2 wounded in Saturday's Iranian strikes on a
  civilian industrial facility; the IRGC says it hit US military
  positions. The Gulf states rally behind Bahrain.
  5. Wall Street rebounds: S&P futures +2.9%, Nasdaq-100 +3.5%,
  Dow +2.0% after Friday's rout put the S&P and Dow in correction.
  Nvidia +8% premarket; CrowdStrike to buy Zscaler for $43.9bn.
  Also today: 24 killed, ~30 missing in the Milkita candy-factory
  fire in Cikande, Indonesia; US troops said to deploy to Honduras
  against the cartels; COP32 heads to Addis Ababa.
"""

import math

from PIL import Image, ImageDraw, ImageFont

SIDE = 1024
MARGIN = 36
RIGHT = SIDE - MARGIN

PALETTE = {
    "paper": (247, 243, 234),
    "ink": (26, 26, 26),
    "grey": (74, 74, 74),
    "navy": (26, 42, 74),
    "red": (178, 34, 34),
    "steel": (96, 108, 124),
    "sky": (206, 224, 236),
    "gold": (196, 152, 44),
    "green": (46, 110, 62),
    "white": (252, 251, 247),
    "blue": (70, 110, 180),
    "rise": (110, 220, 130),
    "sand": (240, 205, 110),
}

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
FACES = {
    "serif_b": FONT_DIR + "DejaVuSerif-Bold.ttf",
    "serif": FONT_DIR + "DejaVuSerif.ttf",
    "sans_b": FONT_DIR + "DejaVuSans-Bold.ttf",
    "sans": FONT_DIR + "DejaVuSans.ttf",
}


def load_font(face, size):
    return ImageFont.truetype(FACES[face], size)


def fit_words(pen, body, face_font, width):
    """Greedy word wrap measured in pixels."""
    fitted, current = [], ""
    for word in body.split():
        candidate = word if current == "" else current + " " + word
        if pen.textlength(candidate, font=face_font) <= width:
            current = candidate
        elif current:
            fitted.append(current)
            current = word
        else:
            current = word
    if current:
        fitted.append(current)
    return fitted


def draw_paragraph(pen, origin, body, face_font, colour, width, spacing=1.18):
    """Draw wrapped text starting at origin; return the y below it."""
    x, y = origin
    gap = int(face_font.size * spacing)
    for row in fit_words(pen, body, face_font, width):
        pen.text((x, y), row, font=face_font, fill=colour)
        y += gap
    return y


def draw_centred(pen, middle, top, body, face_font, colour):
    span = pen.textlength(body, font=face_font)
    pen.text((middle - span / 2, top), body, font=face_font, fill=colour)


canvas = Image.new("RGB", (SIDE, SIDE), PALETTE["paper"])
pen = ImageDraw.Draw(canvas)


def masthead():
    draw_centred(pen, SIDE / 2, 26, "THE WORLD TODAY",
                 load_font("serif_b", 74), PALETTE["ink"])
    pen.line([(MARGIN, 118), (RIGHT, 118)], fill=PALETTE["ink"], width=3)
    pen.line([(MARGIN, 124), (RIGHT, 124)], fill=PALETTE["ink"], width=1)
    draw_centred(pen, SIDE / 2, 136, "MONDAY 23 NOVEMBER 2026",
                 load_font("sans_b", 41), PALETTE["red"])
    draw_centred(pen, SIDE / 2, 188, "THE DAY'S WORLD NEWS IN ONE IMAGE",
                 load_font("sans", 19), PALETTE["grey"])
    pen.line([(MARGIN, 222), (RIGHT, 222)], fill=PALETTE["ink"], width=2)


LEAD_TOP, LEAD_BOTTOM = 238, 486
LEAD_TEXT_X = 396
LEAD_TEXT_W = RIGHT - LEAD_TEXT_X - 24


def lead_story():
    pen.rectangle([MARGIN, LEAD_TOP, RIGHT, LEAD_BOTTOM],
                  outline=PALETTE["ink"], width=2)
    # pictogram: a cracked globe under a hot sun, stamped NO DEAL
    pen.ellipse([66, 292, 226, 452], fill=PALETTE["sky"],
                outline=PALETTE["navy"], width=3)
    pen.line([(146, 292), (146, 452)], fill=PALETTE["navy"], width=2)
    pen.line([(66, 372), (226, 372)], fill=PALETTE["navy"], width=2)
    # jagged crack across the globe
    pen.line([(120, 300), (140, 330), (128, 356), (152, 384),
              (138, 412), (158, 444)], fill=PALETTE["red"], width=4)
    pen.ellipse([268, 272, 324, 328], fill=PALETTE["gold"],
                outline=PALETTE["gold"])
    for spoke in range(8):
        angle = spoke * math.pi / 4
        pen.line([(296 + 36 * math.cos(angle), 300 + 36 * math.sin(angle)),
                  (296 + 46 * math.cos(angle), 300 + 46 * math.sin(angle))],
                 fill=PALETTE["gold"], width=4)
    pen.rectangle([258, 360, 382, 398], fill=PALETTE["red"])
    pen.text((266, 366), "NO DEAL", font=load_font("sans_b", 22),
             fill=PALETTE["white"])
    pen.text((66, 258), "CLIMATE SUMMIT", font=load_font("sans_b", 19),
             fill=PALETTE["navy"])
    # lead words
    pen.text((LEAD_TEXT_X, 256), "ANTALYA, TURKEY",
             font=load_font("sans_b", 19), fill=PALETTE["red"])
    after_head = draw_paragraph(
        pen, (LEAD_TEXT_X, 284), "COP31 COLLAPSES WITH NO DEAL",
        load_font("serif_b", 43), PALETTE["ink"], LEAD_TEXT_W, spacing=1.12)
    draw_paragraph(
        pen, (LEAD_TEXT_X, after_head + 8),
        "The UN climate summit in Antalya ends with no deal "
        "after record overtime. The EU and 130 countries "
        "rejected a text silent on fossil fuels.",
        load_font("serif", 22), PALETTE["grey"], LEAD_TEXT_W, spacing=1.25)


PANEL_W, PANEL_H = 466, 148


def story_panel(left, top, kicker, headline, sub, painter):
    pen.rectangle([left, top, left + PANEL_W, top + PANEL_H],
                  outline=PALETTE["ink"], width=2)
    pen.text((left + 14, top + 9), kicker, font=load_font("sans_b", 15),
             fill=PALETTE["red"])
    painter(left + 14, top + 33)
    draw_paragraph(pen, (left + 120, top + 31), headline,
                   load_font("serif_b", 26), PALETTE["ink"],
                   PANEL_W - 134, spacing=1.12)
    pen.text((left + 120, top + 122), sub, font=load_font("sans", 15),
             fill=PALETTE["grey"])


def paint_flags(x, y):
    # two flags on poles (US stripes, Ukraine blue over yellow)
    # plus a small document stamped 90%
    for stripe in range(7):
        pen.line([(x + 8, y + 12 + stripe * 4), (x + 30, y + 12 + stripe * 4)],
                 fill=PALETTE["red"] if stripe % 2 == 0 else PALETTE["white"],
                 width=4)
    pen.rectangle([x + 8, y + 12, x + 18, y + 22], fill=PALETTE["navy"])
    pen.rectangle([x + 40, y + 12, x + 64, y + 24], fill=PALETTE["blue"])
    pen.rectangle([x + 40, y + 24, x + 64, y + 36], fill=PALETTE["gold"])
    pen.line([(x + 4, y + 8), (x + 4, y + 84)], fill=PALETTE["ink"], width=3)
    pen.line([(x + 36, y + 8), (x + 36, y + 84)], fill=PALETTE["ink"], width=3)
    pen.rectangle([x + 66, y + 48, x + 100, y + 84], fill=PALETTE["white"],
                  outline=PALETTE["ink"], width=2)
    pen.text((x + 70, y + 56), "90%", font=load_font("sans_b", 15),
             fill=PALETTE["green"])


def paint_ship(x, y):
    # a warship listing and sinking, waves below, a drone above
    pen.polygon([(x + 8, y + 40), (x + 78, y + 58), (x + 66, y + 72),
                 (x + 14, y + 62)], fill=PALETTE["steel"],
                outline=PALETTE["ink"])
    pen.rectangle([x + 30, y + 30, x + 48, y + 44], fill=PALETTE["navy"])
    pen.line([(x + 40, y + 12), (x + 40, y + 30)], fill=PALETTE["ink"], width=2)
    for crest in (x + 2, x + 30, x + 58):
        pen.arc([crest, y + 66, crest + 26, y + 84], start=0, end=180,
                fill=PALETTE["navy"], width=3)
    pen.ellipse([x + 76, y + 4, x + 84, y + 12], fill=PALETTE["ink"])
    pen.line([(x + 80, y + 12), (x + 80, y + 20)], fill=PALETTE["ink"], width=2)
    pen.line([(x + 72, y + 16), (x + 88, y + 16)], fill=PALETTE["ink"], width=2)


def paint_dome(x, y):
    # a capitol dome with columns
    pen.pieslice([x + 22, y + 6, x + 66, y + 52], start=180, end=360,
                 fill=PALETTE["white"], outline=PALETTE["ink"], width=2)
    pen.rectangle([x + 18, y + 48, x + 70, y + 58], fill=PALETTE["white"],
                  outline=PALETTE["ink"], width=2)
    for column in (x + 24, x + 38, x + 52):
        pen.line([(column, y + 58), (column, y + 82)], fill=PALETTE["ink"],
                 width=3)
    pen.line([(x + 14, y + 82), (x + 74, y + 82)], fill=PALETTE["ink"], width=3)


def paint_factory(x, y):
    # factory silhouette, a missile arc coming down, a burst of flame
    pen.rectangle([x, y + 58, x + 88, y + 88], fill=PALETTE["steel"])
    pen.rectangle([x + 8, y + 34, x + 20, y + 58], fill=PALETTE["steel"])
    pen.rectangle([x + 58, y + 44, x + 68, y + 58], fill=PALETTE["steel"])
    pen.arc([x + 6, y - 6, x + 96, y + 62], start=300, end=55,
            fill=PALETTE["red"], width=4)
    pen.polygon([(x + 74, y + 30), (x + 84, y + 46), (x + 64, y + 46)],
                fill=PALETTE["red"])
    pen.polygon([(x + 40, y + 40), (x + 50, y + 58), (x + 30, y + 58)],
                fill=PALETTE["gold"])


STORIES = [
    (36, 500, "MAR-A-LAGO - DIPLOMACY", "PEACE PLAN 90% AGREED",
     "Zelenskyy at Mar-a-Lago; Donbas blocks", paint_flags),
    (522, 500, "OFF LIBYA - CONFLICT", "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
     "Kyiv: sea drones sank the corvette", paint_ship),
    (36, 660, "WASHINGTON - POLITICS", "DEMOCRATS WIN 258 HOUSE SEATS",
     "Largest majority since 1992; Senate too", paint_dome),
    (522, 660, "BAHRAIN - CONFLICT", "BAHRAIN: 2 WOUNDED IN IRAN STRIKES",
     "Tehran hit a civilian plant; Gulf rallies", paint_factory),
]


MARKET_TOP, MARKET_BOTTOM = 820, 900


def markets_strip():
    pen.rectangle([MARGIN, MARKET_TOP, RIGHT, MARKET_BOTTOM],
                  fill=PALETTE["navy"])
    trend = [(58, MARKET_TOP + 62), (84, MARKET_TOP + 54),
             (108, MARKET_TOP + 58), (132, MARKET_TOP + 36),
             (158, MARKET_TOP + 22)]
    pen.line(trend, fill=PALETTE["rise"], width=4)
    pen.polygon([(158, MARKET_TOP + 22), (146, MARKET_TOP + 24),
                 (154, MARKET_TOP + 34)], fill=PALETTE["rise"])
    pen.text((196, MARKET_TOP + 12), "WALL STREET REBOUNDS AFTER CORRECTION WEEK",
             font=load_font("serif_b", 24), fill=PALETTE["white"])
    pen.text((196, MARKET_TOP + 50),
             "S&P +2.9%    NASDAQ +3.5%    DOW +2.0%    NVIDIA +8%",
             font=load_font("sans_b", 19), fill=PALETTE["sand"])


def also_today():
    pen.line([(MARGIN, 914), (RIGHT, 914)], fill=PALETTE["ink"], width=2)
    pen.text((MARGIN, 922), "ALSO TODAY", font=load_font("sans_b", 19),
             fill=PALETTE["red"])
    draw_paragraph(
        pen, (MARGIN, 948),
        "24 killed, ~30 missing in Indonesia candy-factory fire - "
        "US troops said to deploy to Honduras against cartels - "
        "CrowdStrike to buy Zscaler for $43.9bn - COP31: first "
        "failure since 2009; COP32 to Addis Ababa",
        load_font("serif", 18), PALETTE["ink"], SIDE - 2 * MARGIN,
        spacing=1.15)


masthead()
lead_story()
for left, top, kicker, headline, sub, painter in STORIES:
    story_panel(left, top, kicker, headline, sub, painter)
markets_strip()
also_today()

canvas.save("art.jpg", quality=88)
print("wrote art.jpg", canvas.size)
