"""Draw the news-image-20261123 artwork: a newspaper front page that sums
up Monday 23 November 2026 in one image.

Build-time tool only (run once, here, with Pillow). The graded entry is
main.py, which copies the generated art.jpg to the output directory.
Every picture below is drawn from scratch with PIL shapes and text --
no photographs, no copied artwork -- so each headline is spelled
exactly as written in this file.

Stories (checked against 23 Nov 2026 reporting: Reuters, AP, CNN,
Just Security's Early Edition for 23 Nov, Rigzone, stockanalysis,
iHeart/BBC, The Daily Fox, Glasgow Times):
  LEAD  COP31 COLLAPSES: the UN climate summit in Antalya ends with
        no deal after record overtime, as the EU and 130+ countries
        reject a final text silent on fossil fuels. First COP
        failure since 2009; UN chief Guterres "deeply disappointed";
        COP32 moves to Addis Ababa.
  1.    Trump hosts Zelenskyy at Mar-a-Lago for 3+ hours: the
        20-point peace plan is "90% agreed", US security guarantees
        "100% agreed"; territory (Donbas) and the Zaporizhzhia
        nuclear plant still block a deal. Trump spoke to Putin for
        over an hour first; "maybe very close" to ending the war.
  2.    Ukraine sinks the Russian corvette Merkury off Libya with
        sea drones, Zelenskyy confirms on Monday; a Russian cargo
        ship is hit in the Baltic; the Kremlin calls it "terrorist
        activity".
  3.    Democrats win 258 House seats, their largest majority since
        1992: Chuck Hubbard beats Virginia Foxx in North Carolina's
        5th by 330 votes after a recount; Democrats also take the
        Senate (54+ seats).
  4.    Bahrain reports 2 wounded in Saturday's Iranian strikes on
        a civilian industrial facility; the IRGC says it hit US
        military positions. The Gulf states rally behind Bahrain.
  5.    Wall Street rebounds: S&P futures +2.9%, Nasdaq-100 +3.5%,
        Dow +2.0% after Friday's rout put the S&P and Dow in
        correction; Nvidia +8% premarket; CrowdStrike to buy
        Zscaler for $43.9bn.
  Also today: 24 killed, ~30 missing in the Milkita candy-factory
  fire in Cikande, Indonesia; US troops said to deploy to Honduras
  against the cartels; COP32 heads to Addis Ababa.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (26, 26, 26)
GREY = (74, 74, 74)
NAVY = (26, 42, 74)
RED = (178, 34, 34)
STEEL = (96, 108, 124)
SKY = (206, 224, 236)
GOLD = (196, 152, 44)
GREEN = (46, 110, 62)
WHITE = (252, 251, 247)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap against pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading=1.18):
    x, y = xy
    lines = wrap(draw, text, fnt, max_w)
    step = int(fnt.size * leading)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + int(fnt.size * 1.25)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------------------------------------------------------- masthead
centered(d, W / 2, 26, "THE WORLD TODAY", font(SERIF_B, 74), INK)
d.line([(36, 118), (W - 36, 118)], fill=INK, width=3)
d.line([(36, 124), (W - 36, 124)], fill=INK, width=1)
centered(d, W / 2, 136, "MONDAY 23 NOVEMBER 2026", font(SANS_B, 41), RED)
centered(d, W / 2, 188, "THE DAY'S WORLD NEWS IN ONE IMAGE", font(SANS, 19), GREY)
d.line([(36, 222), (W - 36, 222)], fill=INK, width=2)

# ---------------------------------------------------------------- lead: COP31
LY0, LY1 = 238, 486
d.rectangle([36, LY0, W - 36, LY1], outline=INK, width=2)
# pictogram: a cracked globe under a hot sun, stamped NO DEAL
d.ellipse([66, 292, 226, 452], fill=SKY, outline=NAVY, width=3)
d.line([(146, 292), (146, 452)], fill=NAVY, width=2)
d.line([(66, 372), (226, 372)], fill=NAVY, width=2)
# jagged crack across the globe
d.line([(120, 300), (140, 330), (128, 356), (152, 384), (138, 412),
        (158, 444)], fill=RED, width=4)
d.ellipse([268, 272, 324, 328], fill=GOLD, outline=GOLD)
for k in range(8):
    a = k * math.pi / 4
    d.line([(296 + 36 * math.cos(a), 300 + 36 * math.sin(a)),
            (296 + 46 * math.cos(a), 300 + 46 * math.sin(a))],
           fill=GOLD, width=4)
d.rectangle([258, 360, 382, 398], fill=RED)
d.text((266, 366), "NO DEAL", font=font(SANS_B, 22), fill=WHITE)
d.text((66, 258), "CLIMATE SUMMIT", font=font(SANS_B, 19), fill=NAVY)
# lead words
lx = 396
d.text((lx, 256), "ANTALYA, TURKEY", font=font(SANS_B, 19), fill=RED)
y = text_block(d, (lx, 284), "COP31 COLLAPSES WITH NO DEAL",
               font(SERIF_B, 43), INK, W - 36 - lx - 24, leading=1.12)
y = text_block(d, (lx, y + 8),
               "The UN climate summit in Antalya ends with no deal "
               "after record overtime. The EU and 130 countries "
               "rejected a text silent on fossil fuels.",
               font(SERIF, 22), GREY, W - 36 - lx - 24, leading=1.25)

# ---------------------------------------------------------------- panels
def panel(px, py, kicker, headline, sub, draw_pic):
    pw, ph = 466, 148
    d.rectangle([px, py, px + pw, py + ph], outline=INK, width=2)
    d.text((px + 14, py + 9), kicker, font=font(SANS_B, 15), fill=RED)
    draw_pic(px + 14, py + 33)
    text_block(d, (px + 120, py + 31), headline, font(SERIF_B, 26), INK,
               pw - 134, leading=1.12)
    d.text((px + 120, py + 122), sub, font=font(SANS, 15), fill=GREY)


def pic_mar_a_lago(x, y):
    # two flags on poles (US stripes, Ukraine blue over yellow)
    # plus a small document stamped 90%
    for i in range(7):
        d.line([(x + 8, y + 12 + i * 4), (x + 30, y + 12 + i * 4)],
               fill=RED if i % 2 == 0 else WHITE, width=4)
    d.rectangle([x + 8, y + 12, x + 18, y + 22], fill=NAVY)
    d.rectangle([x + 40, y + 12, x + 64, y + 24], fill=(70, 110, 180))
    d.rectangle([x + 40, y + 24, x + 64, y + 36], fill=GOLD)
    d.line([(x + 4, y + 8), (x + 4, y + 84)], fill=INK, width=3)
    d.line([(x + 36, y + 8), (x + 36, y + 84)], fill=INK, width=3)
    d.rectangle([x + 66, y + 48, x + 100, y + 84], fill=WHITE,
                outline=INK, width=2)
    d.text((x + 70, y + 56), "90%", font=font(SANS_B, 15), fill=GREEN)


def pic_merkury(x, y):
    # a warship listing and sinking, waves below, a drone above
    d.polygon([(x + 8, y + 40), (x + 78, y + 58), (x + 66, y + 72),
               (x + 14, y + 62)], fill=STEEL, outline=INK)
    d.rectangle([x + 30, y + 30, x + 48, y + 44], fill=NAVY)
    d.line([(x + 40, y + 12), (x + 40, y + 30)], fill=INK, width=2)
    for wx in (x + 2, x + 30, x + 58):
        d.arc([wx, y + 66, wx + 26, y + 84], start=0, end=180, fill=NAVY,
              width=3)
    d.ellipse([x + 76, y + 4, x + 84, y + 12], fill=INK)
    d.line([(x + 80, y + 12), (x + 80, y + 20)], fill=INK, width=2)
    d.line([(x + 72, y + 16), (x + 88, y + 16)], fill=INK, width=2)


def pic_democrats(x, y):
    # a capitol dome with columns
    d.pieslice([x + 22, y + 6, x + 66, y + 52], start=180, end=360,
               fill=WHITE, outline=INK, width=2)
    d.rectangle([x + 18, y + 48, x + 70, y + 58], fill=WHITE,
                outline=INK, width=2)
    for cx in (x + 24, x + 38, x + 52):
        d.line([(cx, y + 58), (cx, y + 82)], fill=INK, width=3)
    d.line([(x + 14, y + 82), (x + 74, y + 82)], fill=INK, width=3)


def pic_bahrain(x, y):
    # factory silhouette, a missile arc coming down, a burst of flame
    d.rectangle([x, y + 58, x + 88, y + 88], fill=STEEL)
    d.rectangle([x + 8, y + 34, x + 20, y + 58], fill=STEEL)
    d.rectangle([x + 58, y + 44, x + 68, y + 58], fill=STEEL)
    d.arc([x + 6, y - 6, x + 96, y + 62], start=300, end=55, fill=RED, width=4)
    d.polygon([(x + 74, y + 30), (x + 84, y + 46), (x + 64, y + 46)],
              fill=RED)
    d.polygon([(x + 40, y + 40), (x + 50, y + 58), (x + 30, y + 58)],
              fill=GOLD)


panel(36, 500, "MAR-A-LAGO - DIPLOMACY",
      "PEACE PLAN 90% AGREED",
      "Zelenskyy at Mar-a-Lago; Donbas blocks",
      pic_mar_a_lago)
panel(522, 500, "OFF LIBYA - CONFLICT",
      "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
      "Kyiv: sea drones sank the corvette",
      pic_merkury)
panel(36, 660, "WASHINGTON - POLITICS",
      "DEMOCRATS WIN 258 HOUSE SEATS",
      "Largest majority since 1992; Senate too",
      pic_democrats)
panel(522, 660, "BAHRAIN - CONFLICT",
      "BAHRAIN: 2 WOUNDED IN IRAN STRIKES",
      "Tehran hit a civilian plant; Gulf rallies",
      pic_bahrain)

# ---------------------------------------------------------------- markets
MY0, MY1 = 820, 900
d.rectangle([36, MY0, W - 36, MY1], fill=NAVY)
pts = [(58, MY0 + 62), (84, MY0 + 54), (108, MY0 + 58), (132, MY0 + 36),
       (158, MY0 + 22)]
d.line(pts, fill=(110, 220, 130), width=4)
d.polygon([(158, MY0 + 22), (146, MY0 + 24), (154, MY0 + 34)],
          fill=(110, 220, 130))
d.text((196, MY0 + 12), "WALL STREET REBOUNDS AFTER CORRECTION WEEK",
       font=font(SERIF_B, 24), fill=WHITE)
d.text((196, MY0 + 50),
       "S&P +2.9%    NASDAQ +3.5%    DOW +2.0%    NVIDIA +8%",
       font=font(SANS_B, 19), fill=(240, 205, 110))

# ---------------------------------------------------------------- also today
d.line([(36, 914), (W - 36, 914)], fill=INK, width=2)
d.text((36, 922), "ALSO TODAY", font=font(SANS_B, 19), fill=RED)
text_block(d, (36, 948),
           "24 killed, ~30 missing in Indonesia candy-factory fire - "
           "US troops said to deploy to Honduras against cartels - "
           "CrowdStrike to buy Zscaler for $43.9bn - COP31: first "
           "failure since 2009; COP32 to Addis Ababa",
           font(SERIF, 18), INK, W - 72, leading=1.15)

img.save("art.jpg", quality=88)
print("wrote art.jpg", img.size)
