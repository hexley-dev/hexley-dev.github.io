#!/usr/bin/env python3
"""Generate all character design concepts via Sparky API."""

import json
import sys
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

CHARACTERS = {
    "A_spark": (
        "Character design sheet, cute retro-futurist spherical robot named Spark, "
        "single large expressive eye lens in center of face, small Sputnik-style antenna on top, "
        "warm copper and brushed bronze metal body, tiny blue hover jets underneath, "
        "friendly and curious expression, Pixar 3D render style, soft studio lighting, "
        "white background, full body view, multiple angle turnaround"
    ),
    "B_byte": (
        "Character design sheet, cute boxy companion robot named Byte, "
        "rectangular body shaped like a miniature vintage CRT television set, "
        "friendly face displayed on the screen with pixel-style eyes and smile, "
        "stubby rounded legs, small arms, green phosphor glow accents on edges, "
        "warm gray plastic body, retro 1980s tech aesthetic, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "C_ada": (
        "Character design sheet, cute sleek modern robot assistant named Ada, "
        "smooth white teardrop-shaped body, two large expressive blue eyes, "
        "no visible arms but two small floating hands nearby, soft blue glow effects "
        "around body edges, minimal and elegant design like Baymax meets Eve from Wall-E, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "D_coil": (
        "Character design sheet, cute steampunk tinker robot named Coil, "
        "stocky build with visible brass gears and copper pipes on body, "
        "aviator goggles pushed up on forehead, small tool belt around waist, "
        "warm amber and brass tones, big friendly eyes, slightly sooty, "
        "inventor workshop aesthetic, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "E_pip": (
        "Character design sheet, tiny adorable round robot named Pip, "
        "extremely round spherical body very small in size, huge expressive eyes "
        "taking up most of the face, single bouncy spring antenna on top with glowing ball, "
        "soft pastel lavender body color, tiny stubby feet, no visible arms, "
        "Kirby meets robot aesthetic, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "F_relay": (
        "Character design sheet, cute origami paper robot named Relay, "
        "body made of folded kraft paper and cardboard with visible fold creases and edges, "
        "warm cream and brown paper tones, triangular pointed ears folded from paper, "
        "face drawn on with black marker - simple dot eyes and line smile, "
        "handcrafted DIY aesthetic, slightly crumpled and imperfect, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "G_nixie": (
        "Character design sheet, cute robot made from a vintage vacuum tube named Nixie, "
        "body is a large glass vacuum tube with warm orange glowing filament inside, "
        "the filament forms a simple friendly smiling face, thin delicate wire limbs, "
        "glass dome head with visible internal components, warm amber glow, "
        "retro electronics aesthetic, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "H_patch": (
        "Character design sheet, cute stitched plushie robot named Patch, "
        "soft felt and fabric textured body with visible hand stitching along seams, "
        "mismatched button eyes one blue one green, different colored fabric patches "
        "sewn onto body in red yellow blue green, slightly lopsided and asymmetric, "
        "stuffed toy aesthetic, warm and huggable, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "I_hex": (
        "Character design sheet, cute holographic crystal robot named Hex, "
        "translucent blue-white geometric faceted body like a cut crystal or gem, "
        "visible glowing light source in center of chest, floats slightly above ground, "
        "trailing small sparkle particles below, simple friendly face features "
        "etched into crystal surface, minimal and elegant, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "J_rune": (
        "Character design sheet, cute chalkboard robot teacher named Rune, "
        "body surface is a dark green chalkboard with chalk equations and doodles on it, "
        "round friendly face with small round glasses, holds a tiny wooden pointer stick, "
        "chalk dust particles floating around, warm wood frame edges on body, "
        "professor aesthetic but cute, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "K_toggle": (
        "Character design sheet, cute split-personality switch robot named Toggle, "
        "compact boxy body with heavily rounded edges, literal ON OFF toggle switch on top, "
        "left half of body is bright sunny yellow, right half is deep calm blue, "
        "very expressive thick eyebrows, wide friendly eyes, small sturdy legs, "
        "playful duality design, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "L_sprout": (
        "Character design sheet, cute circuit board seedling robot named Sprout, "
        "small plant-like form growing up from a green circuit board base, "
        "stem and leaves made of copper traces and wires, small LED lights as flowers "
        "in red yellow green, tiny friendly face on the main bud, "
        "combines organic plant growth with electronic circuit aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "M_blip": (
        "Character design sheet, cute oscilloscope-faced robot named Blip, "
        "round vintage CRT oscilloscope screen as face showing green waveform that forms "
        "a happy smile expression, chunky rotary knobs on sides as ears, "
        "brushed aluminum and beige plastic body, mid-century laboratory instrument aesthetic, "
        "stocky and solid build, small sturdy feet, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "N_kit": (
        "Character design sheet, cute breadboard robot named Kit, "
        "body is a white electronics breadboard with colorful jumper wires and components "
        "plugged in visibly, legs made of resistors with color stripe bands, "
        "bright LED eyes that glow, small capacitors and chips visible on body, "
        "DIY electronics maker project aesthetic, Pixar 3D render style, "
        "soft studio lighting, white background, full body view"
    ),
    "O_moth": (
        "Character design sheet, cute mechanical moth robot named Moth, "
        "small moth-like silhouette but clearly mechanical and robotic, "
        "translucent wings with visible circuit board trace patterns glowing softly, "
        "two long antenna on head that glow at the tips, large gentle compound eyes, "
        "soft dusty purple and silver color scheme, delicate and curious, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
}


def generate(name, prompt):
    out_path = f"images/{name}.png"
    payload = json.dumps({
        "prompt": prompt,
        "width": 1024,
        "height": 1024,
    }).encode()

    req = urllib.request.Request(
        API, data=payload, headers={"Content-Type": "application/json"}
    )

    print(f"  Generating {name}...", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = resp.read()
    elapsed = time.time() - t0

    with open(out_path, "wb") as f:
        f.write(data)
    print(f"  ✓ {name} ({elapsed:.0f}s, {len(data)//1024}KB)", flush=True)


def main():
    total = len(CHARACTERS)
    print(f"Generating {total} character designs via Sparky API...\n", flush=True)
    t_start = time.time()

    for i, (name, prompt) in enumerate(CHARACTERS.items(), 1):
        print(f"[{i}/{total}] {name}", flush=True)
        try:
            generate(name, prompt)
        except Exception as e:
            print(f"  ✗ FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nDone! Total time: {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
