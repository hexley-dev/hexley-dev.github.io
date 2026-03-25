#!/usr/bin/env python3
"""Expand the 'Just Walking' Scribble concept across different materials.

Core: the simplest possible robot — round, two dot eyes, toddling along tape.
Magnifying glass in one hand, pencil in the other.
No vehicle. Just walking.

Vary ONLY the material/texture. Keep the simple round shape.
"""

import json
import os
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "images_walking_materials")
os.makedirs(OUT_DIR, exist_ok=True)

STYLE = "Pixar 3D render style, soft studio lighting, white background, character design sheet, full body view"

CORE = (
    "Character design sheet, cute tiny round robot simply walking on two small feet, "
    "no vehicle, toddling along paper tape with diverse symbols, "
    "magnifying glass in one hand, pencil in the other, "
    "minimal simple design, maximum simplicity and charm"
)

DESIGNS = {
    "01_white_matte": (
        f"{CORE}, smooth matte white plastic body like an Apple product, "
        "soft rounded form, two small black dot eyes, tiny gentle smile, "
        "clean and minimal, warm but modern, "
        f"{STYLE}"
    ),
    "02_warm_brass": (
        f"{CORE}, warm polished brass body with a soft golden glow, "
        "slightly weathered patina in the creases, two round dark eyes, "
        "the warmth of an old pocket watch, "
        f"{STYLE}"
    ),
    "03_terracotta": (
        f"{CORE}, terracotta clay body with visible subtle fingerprints from being shaped by hand, "
        "warm orange-brown earth tones, matte unglazed surface, "
        "painted white dot eyes, simple painted smile, "
        "pottery studio warmth, "
        f"{STYLE}"
    ),
    "04_frosted_glass": (
        f"{CORE}, frosted translucent glass body with a warm golden light glowing softly inside, "
        "the light pulses gently, smooth rounded form, "
        "features etched into the glass surface — two dot eyes and a small smile, "
        "lantern warmth, "
        f"{STYLE}"
    ),
    "05_honey_wood": (
        f"{CORE}, carved from warm honey-colored wood with visible grain, "
        "smooth sanded surface, jointed wooden limbs with tiny pegs, "
        "painted rosy cheeks and black dot eyes, "
        "handmade wooden toy from a craftsman's workshop, "
        f"{STYLE}"
    ),
    "06_soft_felt": (
        f"{CORE}, made of soft pastel mint green felt fabric, "
        "visible hand-stitching along seams in white thread, "
        "mismatched button eyes one blue one brown, "
        "slightly squishy and imperfect, stuffed with cotton, "
        "handmade with love, "
        f"{STYLE}"
    ),
    "07_brushed_steel": (
        f"{CORE}, brushed stainless steel body with fine circular brushing marks, "
        "cool silver tones with subtle warm reflections, "
        "precision-machined minimal form, two small LED dot eyes in warm amber, "
        "industrial but friendly, Dyson meets Pixar, "
        f"{STYLE}"
    ),
    "08_pastel_ceramic": (
        f"{CORE}, glazed ceramic body in soft pastel baby blue, "
        "smooth shiny glaze with tiny crackle pattern, "
        "hand-painted features — two black dot eyes, pink circle cheeks, "
        "like a precious ceramic figurine, "
        f"{STYLE}"
    ),
    "09_copper_patina": (
        f"{CORE}, copper body with beautiful green-blue verdigris patina, "
        "the patina creates natural patterns on the surface, "
        "some areas still show bright copper underneath, "
        "aged and beautiful like a weathered statue, two bright copper dot eyes, "
        f"{STYLE}"
    ),
    "10_marble": (
        f"{CORE}, carved from white marble with subtle grey veining, "
        "smooth polished surface that catches light, "
        "classical sculpture feeling but tiny and cute, "
        "features carved in — simple eyes and mouth, "
        "museum quality miniature, "
        f"{STYLE}"
    ),
    "11_cork": (
        f"{CORE}, made of natural cork material with visible cork texture, "
        "warm tan brown tones, lightweight feeling, "
        "features drawn on with dark ink — simple eyes and smile, "
        "bulletin board meets robot, eco-friendly charm, "
        f"{STYLE}"
    ),
    "12_candy_resin": (
        f"{CORE}, made of transparent candy-colored resin in warm amber, "
        "like a piece of hard candy or honey, translucent body, "
        "tiny bubbles visible inside the resin, "
        "features floating inside as darker shapes — eyes and smile, "
        "sweet and warm, "
        f"{STYLE}"
    ),
    "13_concrete": (
        f"{CORE}, made of smooth pale concrete with tiny aggregate speckles visible, "
        "architectural brutalist miniature, matte surface, "
        "features are recessed grooves — two circle eyes and a line smile, "
        "small succulent plant growing from a crack on top of head, "
        "urban and organic, "
        f"{STYLE}"
    ),
    "14_rose_gold": (
        f"{CORE}, polished rose gold metallic body with warm pink-gold reflections, "
        "luxurious but tiny, perfectly smooth, "
        "two small dark eyes with a warm sparkle, "
        "elegant and precious like a piece of jewelry, "
        f"{STYLE}"
    ),
    "15_chalkboard": (
        f"{CORE}, body surface is matte dark green like a chalkboard, "
        "chalk dust on the surface, chalk-drawn features — "
        "wobbly circle eyes and a chalky smile that could be redrawn, "
        "the pencil in its hand is actually chalk, "
        "classroom warmth, "
        f"{STYLE}"
    ),
}


def generate(name, prompt):
    out_path = os.path.join(OUT_DIR, f"walking_{name}.png")
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
    print(f"Generating {total} Walking Scribble material explorations...\n", flush=True)
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
