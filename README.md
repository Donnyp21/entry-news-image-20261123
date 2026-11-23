[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Donnyp21/entry-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Donnyp21/entry-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# news-image-20261123 — Monday 23 November 2026, in one image

A newspaper front page, "MONDAY 23 NOVEMBER 2026", summing up the
day's world news in a single frame (stories checked against 23 Nov
2026 reporting from Reuters, AP, CNN, Just Security's Early Edition,
Rigzone, stockanalysis, iHeart/BBC, The Daily Fox and Glasgow Times):

1. **COP31 collapses with no deal** — the UN climate summit in
   Antalya ends after record overtime as the EU and 130 countries
   reject a final text silent on fossil fuels; the first COP
   failure since 2009.
2. **Peace plan "90% agreed"** — Trump hosts Zelenskyy at
   Mar-a-Lago for 3+ hours; US security guarantees "100%
   agreed", the Donbas still blocks a deal.
3. **Ukraine sinks a Russian warship off Libya** — sea drones
   sank the corvette Merkury, Kyiv confirms; a Russian cargo
   ship is hit in the Baltic.
4. **Democrats win 258 House seats** — their largest majority
   since 1992 (Hubbard beats Foxx in N. Carolina by 330 votes);
   they take the Senate too.
5. **Bahrain: 2 wounded in Iran strikes** — Tehran hit a
   civilian industrial facility on Saturday; the Gulf states
   rally behind Bahrain.
6. **Wall Street rebounds after correction week** — S&P +2.9%,
   Nasdaq +3.5%, Dow +2.0% in premarket; Nvidia +8%.
7. Also today: 24 killed, ~30 missing in the Indonesia
   candy-factory fire · US troops said to deploy to Honduras
   against the cartels · CrowdStrike to buy Zscaler for $43.9bn
   · COP31: first failure since 2009; COP32 to Addis Ababa.

## How it works

`gen_image.py` (build-time only, Pillow) draws the artwork from
scratch — shapes and text, no photographs, no copied artwork — and
saves it as `art.jpg` (1024x1024 JPEG). `main.py` (Python 3.13
standard library only, no network) validates that artwork against
the competition's caps (a whole JPEG, at most 1 MiB, at most
1024x1024 pixels) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `$MAKEFUN_OUTPUT`, then `/output`). The output is
a byte-for-byte copy, so two runs produce identical bytes.

Run: `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`
Regenerate the artwork: `python3 gen_image.py`
