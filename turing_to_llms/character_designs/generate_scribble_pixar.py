#!/usr/bin/env python3
"""Generate diverse Scribble character explorations in Pixar 3D style.

Core identity (fixed):
  - Magnifying glass in one hand
  - Pencil in the other
  - Travels on/along paper tape

Everything else (explore):
  - Material (brass, porcelain, wood, plastic, glass, felt, clay...)
  - Body shape (round, boxy, teardrop, bean, egg, star...)
  - Color palette (warm metals, cool blues, pastel, earth tones, candy colors...)
  - Transport (onewheel, skateboard, roller skates, sled, surfboard, just walking...)
  - Personality (curious scholar, mischievous kid, gentle elder, hyperactive explorer...)
  - Size feel (tiny, chunky, lanky, squishy...)
"""

import json
import os
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "images_pixar_hybrid")
os.makedirs(OUT_DIR, exist_ok=True)

STYLE = "Pixar 3D render style, soft studio lighting, white background, character design sheet, full body view"

CORE = "magnifying glass in one hand, pencil in the other, paper tape with diverse symbols"

DESIGNS = {
    # ── Material explorations ──
    "01_porcelain": (
        "Character design sheet, cute tiny robot made of smooth white porcelain with delicate blue "
        "painted patterns like fine china, round body, big gentle blue eyes, "
        f"{CORE} as a scarf trailing behind, small wheels on bottom, "
        "precious and delicate feeling, warm and refined, "
        f"{STYLE}"
    ),
    "02_wooden_toy": (
        "Character design sheet, cute tiny robot carved from warm honey-colored wood like a "
        "handmade wooden toy, visible wood grain, jointed limbs with small pegs, "
        "painted rosy cheeks and big round black button eyes, "
        f"{CORE}, riding along the tape on tiny wooden wheels, "
        "whittled by a loving craftsperson energy, Pinocchio meets robot, "
        f"{STYLE}"
    ),
    "03_candy_colored": (
        "Character design sheet, cute tiny robot made of glossy candy-colored plastic, "
        "bubblegum pink body with mint green and lemon yellow accents, "
        "oversized head, tiny body, enormous sparkly eyes, "
        f"{CORE}, scooting along the tape on a tiny scooter, "
        "hyper-cute kawaii toy aesthetic, Polly Pocket energy, "
        f"{STYLE}"
    ),
    "04_copper_steampunk_lite": (
        "Character design sheet, cute tiny robot with polished copper body and small brass rivets, "
        "round porthole window on chest showing tiny spinning gears inside, "
        "oversized curious eyes behind round goggles pushed up on forehead, "
        f"{CORE}, riding a monowheel along the tape, "
        "warm copper patina tones, adventurous explorer, "
        f"{STYLE}"
    ),
    # ── Shape explorations ──
    "05_bean": (
        "Character design sheet, cute tiny bean-shaped robot with a soft squishy silicone body, "
        "matte pastel lavender color, minimal features — just two big oval eyes and a small mouth, "
        "stubby rounded arms and no visible legs, floats slightly above the ground, "
        f"{CORE}, gliding along the tape hovering, "
        "extremely minimal and soft, Baymax baby energy, "
        f"{STYLE}"
    ),
    "06_boxy_retro": (
        "Character design sheet, cute tiny boxy robot with rounded edges like a mini vintage TV, "
        "CRT screen face showing expressive pixel eyes and smile, "
        "chunky square body in warm beige plastic with orange and brown 70s accents, "
        "antenna on top with a bobble, stubby legs in sneakers, "
        f"{CORE}, walking along the tape in sneakers, "
        "retro 1970s toy aesthetic, warm and nostalgic, "
        f"{STYLE}"
    ),
    "07_teardrop": (
        "Character design sheet, cute tiny teardrop-shaped robot with glossy white body, "
        "the narrow end points up like a hat, wide base, "
        "one large cyclopean eye with a warm amber iris, "
        "thin graceful arms, floats on a single sphere wheel, "
        f"{CORE}, rolling along the tape on its sphere, "
        "elegant and simple, Eve from Wall-E energy, "
        f"{STYLE}"
    ),
    # ── Personality explorations ──
    "08_professor": (
        "Character design sheet, cute tiny elderly professor robot with a small round body, "
        "wearing tiny round spectacles, a miniature tweed jacket, and a bow tie, "
        "warm silver and gray metal body, slightly tarnished with age, "
        "kind wise eyes with smile wrinkles, thin limbs, "
        f"{CORE}, walking along the tape with a slight scholarly stoop, "
        "wise and gentle, the teacher you wish you had, "
        f"{STYLE}"
    ),
    "09_kid_explorer": (
        "Character design sheet, cute tiny energetic child-like robot with a bright orange body, "
        "wearing an oversized explorer hat that keeps falling over its eyes, "
        "gap-toothed grin, freckle-like rivets on cheeks, "
        "one eye bigger than the other from excitement, bouncy spring legs, "
        f"{CORE}, bouncing along the tape on spring legs, "
        "pure excitable kid energy, everything is amazing, "
        f"{STYLE}"
    ),
    "10_stargazer": (
        "Character design sheet, cute tiny translucent robot with a glass dome head, "
        "inside the dome a tiny galaxy of stars slowly rotates, "
        "soft periwinkle blue body with constellation patterns etched on surface, "
        "big dreamy wondering eyes looking slightly upward, "
        f"{CORE}, drifting along the tape on a small cloud, "
        "dreamy and philosophical, the one who asks why, "
        f"{STYLE}"
    ),
    # ── More material explorations ──
    "11_clay": (
        "Character design sheet, cute tiny robot made of terracotta clay with visible thumbprints, "
        "warm orange-brown earth tones, slightly lumpy and imperfect, "
        "painted simple face with big white dot eyes, "
        "stubby thick arms and legs, heavy and grounded, "
        f"{CORE}, waddling along the tape with heavy satisfying steps, "
        "handmade ceramics aesthetic, Aardman clay animation energy, "
        f"{STYLE}"
    ),
    "12_chrome_retro_future": (
        "Character design sheet, cute tiny robot with mirror-polished chrome body reflecting rainbow, "
        "atomic-age 1950s retro futurism design, fin-shaped ears, "
        "round bubble helmet head with visible friendly face inside, "
        "jet-flame feet like a tiny rocket, red and chrome color scheme, "
        f"{CORE}, jet-hovering along the tape on tiny flames, "
        "The Jetsons meets Pixar, optimistic future aesthetic, "
        f"{STYLE}"
    ),
    "13_felt_plush": (
        "Character design sheet, cute tiny robot made of soft colored felt fabric, "
        "visible hand-stitching along seams, button eyes — one blue one green, "
        "round puffy body stuffed with fluff, patchwork belly in warm colors, "
        "floppy fabric arms and legs, yarn hair, "
        f"{CORE} but the magnifying glass and pencil are also felt craft versions, "
        "riding along a felt tape, handmade with love energy, "
        f"{STYLE}"
    ),
    "14_glass_glow": (
        "Character design sheet, cute tiny robot made of frosted glass with a warm golden glow inside, "
        "the internal light pulses gently like a heartbeat, "
        "smooth rounded form, the light casts warm patterns through the frosted surface, "
        "simple etched features — two dot eyes and a curved smile, "
        f"{CORE}, gliding along the tape leaving a faint warm light trail, "
        "lantern meets robot, warm and magical but not supernatural, "
        f"{STYLE}"
    ),
    # ── Transport explorations ──
    "15_skateboard": (
        "Character design sheet, cute tiny brass and teal robot with a cool attitude, "
        "wearing a tiny backwards cap, half-lidded confident eyes, "
        "compact stocky build with big sneaker-like feet, "
        f"{CORE}, doing a trick on a tiny skateboard rolling along the tape, "
        "the tape IS the skatepark rail, street art energy, "
        f"{STYLE}"
    ),
    "16_roller_skates": (
        "Character design sheet, cute tiny round pink and white robot on roller skates, "
        "sparkly eyes, pigtail-like antennae with bows, rosy cheeks, "
        "graceful skating pose with one leg extended, "
        f"{CORE}, roller skating along the tape with grace, "
        "figure skating meets robot, joyful movement, "
        f"{STYLE}"
    ),
    "17_unicycle_classic": (
        "Character design sheet, cute tiny warm brass robot on a classic unicycle, "
        "top hat, monocle replaced by the magnifying glass held up, "
        "pencil tucked in vest pocket, waistcoat and bow tie, "
        "gentleman inventor aesthetic, warm golden brass, "
        f"{CORE}, pedaling a unicycle along the tape, "
        "Victorian gentleman meets cute robot, "
        f"{STYLE}"
    ),
    "18_walking_simple": (
        "Character design sheet, cute tiny round white robot simply walking on two small feet, "
        "no vehicle at all, just toddling along the paper tape, "
        "minimal design — round body, two dot eyes, tiny smile, "
        "the simplest possible robot doing the simplest possible thing, "
        f"{CORE}, walking along the tape one step at a time, "
        "maximum simplicity, pure and uncluttered, "
        f"{STYLE}"
    ),
    # ── Wild cards ──
    "19_origami": (
        "Character design sheet, cute tiny robot folded from metallic origami paper, "
        "visible crisp geometric folds, gold and copper metallic paper, "
        "angular but somehow still cute, triangular body with folded ears, "
        f"{CORE}, sliding along the tape which is also a paper strip, "
        "elegant paper craft aesthetic, the tape and robot are the same medium, "
        f"{STYLE}"
    ),
    "20_lightbulb": (
        "Character design sheet, cute tiny robot whose body IS a vintage Edison lightbulb, "
        "warm glowing filament visible inside as a smiling face, "
        "thin wire arms and legs from the bulb's base, "
        "screw-base feet, warm amber glow, "
        f"{CORE}, walking along the tape with its warm glow illuminating the symbols, "
        "the light of understanding, bright idea personified, "
        f"{STYLE}"
    ),
}


def generate(name, prompt):
    out_path = os.path.join(OUT_DIR, f"scribble_pixar_{name}.png")
    if os.path.exists(out_path):
        return "skip"
    payload = json.dumps({"prompt": prompt, "width": 768, "height": 768}).encode()
    req = urllib.request.Request(
        API, data=payload, headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = resp.read()
    with open(out_path, "wb") as f:
        f.write(data)
    return f"{time.time()-t0:.0f}s, {len(data)//1024}KB"


def main():
    total = len(DESIGNS)
    print(f"Generating {total} Scribble explorations...\n", flush=True)
    t_start = time.time()
    for i, (name, prompt) in enumerate(DESIGNS.items(), 1):
        print(f"[{i}/{total}] {name}...", end=" ", flush=True)
        try:
            result = generate(name, prompt)
            print(result, flush=True)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)
    elapsed = time.time() - t_start
    print(f"\nDone! {total} images in {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
