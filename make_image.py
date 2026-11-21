#!/usr/bin/env python3
"""Build entry.png: a newspaper front page summing up world news,
Saturday 21 November 2026. Runs locally with PIL; the grader never
runs this script (main.py only copies entry.png)."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
NAVY = (18, 38, 68)
NAVY2 = (28, 58, 96)
RED = (178, 34, 34)
GOLD = (198, 158, 60)
BLUE = (36, 90, 150)
TEAL = (0, 120, 113)
ORANGE = (176, 92, 20)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_MAST = font("DejaVuSans-Bold.ttf", 62)
F_DATE = font("DejaVuSans-Bold.ttf", 28)
F_KICK = font("DejaVuSans-Bold.ttf", 23)
F_LEAD = font("DejaVuSans-Bold.ttf", 38)
F_LEADCAP = font("DejaVuSans.ttf", 22)
F_H = font("DejaVuSans-Bold.ttf", 24)
F_C = font("DejaVuSans.ttf", 20)
F_TICK = font("DejaVuSans.ttf", 20)
F_TICKB = font("DejaVuSans-Bold.ttf", 21)
F_FOOT = font("DejaVuSans-Bold.ttf", 19)
F_LBL = font("DejaVuSans-Bold.ttf", 19)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def draw_chart_icon(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(253, 238, 238), outline=RED, width=3)
    d.line([(x + 10, y + s - 12), (x + 10, y + 10)], fill=INK, width=3)
    d.line([(x + 10, y + s - 12), (x + s - 10, y + s - 12)], fill=INK, width=3)
    pts = [(x + 14, y + 20), (x + 26, y + 26), (x + 38, y + 22),
           (x + 50, y + 38), (x + 62, y + 52)]
    d.line(pts, fill=RED, width=4, joint="curve")
    d.polygon([(x + 62, y + 52), (x + 52, y + 50), (x + 60, y + 62)], fill=RED)


def draw_scales_icon(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 244, 243), outline=TEAL, width=3)
    cx = x + s // 2
    d.line([(cx, y + 12), (cx, y + s - 14)], fill=INK, width=4)
    d.line([(x + 12, y + 22), (x + s - 12, y + 22)], fill=INK, width=4)
    for px in (x + 12, x + s - 12):
        d.line([(px, y + 22), (px - 8, y + 42)], fill=INK, width=3)
        d.line([(px, y + 22), (px + 8, y + 42)], fill=INK, width=3)
        d.arc([px - 11, y + 36, px + 11, y + 54], 0, 180, fill=TEAL, width=4)
    d.rectangle([x + 8, y + s - 12, x + s - 8, y + s - 8], fill=INK)


def draw_quake_icon(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(250, 240, 224), outline=ORANGE, width=3)
    d.rectangle([x + 14, y + 30, x + 30, y + s - 12], fill=ORANGE)
    d.rectangle([x + 38, y + 20, x + 56, y + s - 12], fill=(140, 70, 10))
    d.line([(x + 32, y + 8), (x + 26, y + 24), (x + 36, y + 34),
            (x + 28, y + 48), (x + 38, y + s - 12)], fill=INK, width=3)
    d.line([(x + 44, y + 8), (x + 50, y + 20), (x + 42, y + 30)], fill=INK, width=3)


def draw_flags_icon(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 240, 250), outline=BLUE, width=3)
    d.line([(x + 20, y + 14), (x + 20, y + s - 12)], fill=INK, width=3)
    d.line([(x + 52, y + 14), (x + 52, y + s - 12)], fill=INK, width=3)
    d.polygon([(x + 20, y + 14), (x + 46, y + 20), (x + 20, y + 28)], fill=BLUE)
    d.polygon([(x + 52, y + 14), (x + 26, y + 20), (x + 52, y + 28)], fill=RED)
    d.line([(x + 20, y + 40), (x + 52, y + 40)], fill=GOLD, width=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 118], fill=NAVY)
    t = "THE WORLD TODAY"
    d.text(((W - d.textlength(t, font=F_MAST)) / 2, 16), t, font=F_MAST, fill=WHITE)
    t2 = "SATURDAY  •  21 NOVEMBER 2026"
    d.text(((W - d.textlength(t2, font=F_DATE)) / 2, 80), t2, font=F_DATE, fill=GOLD)
    d.rectangle([0, 118, W, 124], fill=GOLD)

    # --- lead story: Russia / Poland ---
    d.text((28, 138), "WAR IN EUROPE — LEAD STORY", font=F_KICK, fill=RED)
    lead = wrap(d, "RUSSIA'S BIGGEST STRIKE HITS UKRAINE — MISSILES FALL IN POLAND",
                F_LEAD, 600)
    y = 168
    for ln in lead:
        d.text((28, y), ln, font=F_LEAD, fill=INK)
        y += 48
    cap = ("400+ drones and 110 missiles hit Kyiv overnight, killing at "
           "least 8. Two missiles and a drone fell in Poland; PM Tusk "
           "calls it a provocation.")
    text_block(d, 28, y + 8, wrap(d, cap, F_LEADCAP, 600), F_LEADCAP, INK, 27)

    # lead illustration: night sky, missile trails, blast
    ix, iy, iw, ih = 656, 140, 340, 252
    d.rectangle([ix, iy, ix + iw, iy + ih], fill=NAVY2)
    for cx, cy, r in [(700, 180, 3), (760, 165, 2), (830, 195, 3),
                      (900, 170, 2), (950, 210, 3), (690, 240, 2),
                      (860, 230, 2), (930, 260, 2)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
    d.arc([ix + 30, iy + 60, ix + 200, iy + 260], 200, 330, fill=WHITE, width=5)
    d.arc([ix + 120, iy + 20, ix + 300, iy + 220], 200, 330, fill=GOLD, width=5)
    d.ellipse([ix + 168, iy + 78, ix + 182, iy + 92], fill=WHITE)
    d.ellipse([ix + 258, iy + 38, ix + 272, iy + 52], fill=GOLD)
    bx, by = ix + 210, iy + 195
    for ang in range(0, 360, 45):
        import math
        x2 = bx + int(34 * math.cos(math.radians(ang)))
        y2 = by + int(34 * math.sin(math.radians(ang)))
        d.line([(bx, by), (x2, y2)], fill=(255, 140, 40), width=6)
    d.ellipse([bx - 16, by - 16, bx + 16, by + 16], fill=(255, 180, 60))
    d.ellipse([bx - 7, by - 7, bx + 7, by + 7], fill=(255, 220, 120))
    d.rectangle([ix, iy + ih - 30, ix + iw, iy + ih], fill=(0, 0, 0))
    d.text((ix + 12, iy + ih - 26), "KYIV  •  WARSAW", font=F_LBL, fill=WHITE)

    d.line([(28, 420), (W - 28, 420)], fill=INK, width=3)

    # --- 2x2 story grid ---
    cells = [
        (28, 432, RED, "MARKETS", "AI SELL-OFF PUTS WALL STREET IN CORRECTION",
         "S&P 500 −3.7%, Nasdaq −5.3%. Nvidia falls about 14% as the SEC "
         "opens an accounting probe.", draw_chart_icon),
        (524, 432, TEAL, "JUSTICE", "UN COURT: MYANMAR COMMITTED GENOCIDE",
         "ICJ rules 9–6 that Myanmar committed genocide against the "
         "Rohingya in 2017 and orders an inquiry and compensation.",
         draw_scales_icon),
        (28, 656, ORANGE, "DISASTER", "MAGNITUDE 6.8 QUAKE SHAKES PERU",
         "Strong earthquake strikes the Junín region in the Andes; "
         "tremors felt 320 km away in Lima.", draw_quake_icon),
        (524, 656, BLUE, "POLITICS", "UK AND EU SEAL POST-BREXIT DEALS",
         "Food-trade checks scrapped from March 2028, carbon markets "
         "linked, and a youth-mobility scheme for 100,000.",
         draw_flags_icon),
    ]
    for (cx, cy, col, kick, head, cap, icon) in cells:
        d.rectangle([cx, cy, cx + 472, cy + 212], fill=CARD, outline=(200, 200, 200), width=2)
        d.rectangle([cx, cy, cx + 472, cy + 8], fill=col)
        icon(d, cx + 16, cy + 26, 72)
        d.text((cx + 104, cy + 24), kick, font=F_KICK, fill=col)
        hy = text_block(d, cx + 104, cy + 54,
                        wrap(d, head, F_H, 472 - 120), F_H, INK, 29)
        text_block(d, cx + 16, max(cy + 124, hy + 8),
                   wrap(d, cap, F_C, 472 - 32), F_C, (60, 60, 60), 26)

    # --- ticker: also today ---
    d.rectangle([0, 880, W, 962], fill=NAVY)
    d.text((28, 890), "ALSO TODAY", font=F_TICKB, fill=GOLD)
    tick = ("COP31 misses its deadline as the draft drops fossil fuels  •  "
            "Cancer pill makes tumours undetectable in 1 in 12 patients  •  "
            "Houthi missiles aimed at Riyadh intercepted")
    text_block(d, 28, 914, wrap(d, tick, F_TICK, W - 56), F_TICK, WHITE, 24)

    # --- footer ---
    ft = "21 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE"
    d.text(((W - d.textlength(ft, font=F_FOOT)) / 2, 976), ft,
           font=F_FOOT, fill=GREY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
