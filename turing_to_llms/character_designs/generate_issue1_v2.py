#!/usr/bin/env python3
"""Generate 10 adorable Turing machine character concepts for Issue 1."""

import json
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

STYLE = (
    "comic book style, warm editorial illustration with ink lines and watercolor washes, "
    "adorable cute kawaii appeal, big expressive eyes, warm paper-white background, "
    "full body front view, character design sheet"
)

CHARACTERS = {
    "scribble": (
        "A tiny round adorable robot with a long paper tape scarf trailing behind it like a kite tail, "
        "symbols and zeros and ones printed on the tape scarf, "
        "wearing a magnifying glass as a monocle over one big curious eye, "
        "clutching a tiny pencil in one hand like a child learning to write, "
        "round pudgy body in warm brass and cream tones, small stubby legs, "
        "curious excited toddler energy, head tilted with wonder"
    ),
    "ticker": (
        "A small adorable robot sitting inside a tape reel like a hamster in a wheel, "
        "peeking over the top edge of the reel with enormous curious eyes, "
        "paper tape with symbols printed on it wrapping around the reel, "
        "tiny hands gripping the reel edge, feet dangling inside, "
        "the tape reel is its cozy home and vehicle, warm copper and cream tones, "
        "playful and snug like a kid in a cardboard box fort"
    ),
    "peeka": (
        "A round adorable robot whose belly has a small circular porthole window, "
        "through the window you can see paper tape with binary symbols scrolling past inside, "
        "enormous curious eyes always looking down at the next symbol in its belly window, "
        "tiny antenna with a lightbulb tip that lights up when it reads something, "
        "pudgy round body in soft blue and cream, stubby arms and legs, "
        "fascinated by its own inner workings"
    ),
    "zippy": (
        "A tiny adorable robot surfing on a strip of paper tape like a skateboard, "
        "leaning forward with oversized aviator goggles pushed up on forehead, "
        "the paper tape has binary symbols and the robot reads them as it zooms along, "
        "tiny scarf flying behind in the wind, excited grin, "
        "warm brass and red goggles, dynamic fun pose, "
        "sense of speed and adventure and discovery"
    ),
    "nibble": (
        "A small adorable robot shaped like a tiny vintage typewriter but with huge kawaii eyes, "
        "feeding paper tape into its mouth from one side and outputting tape from the other side, "
        "tiny circular paper chad confetti scattered around it like cookie crumbs, "
        "satisfied happy munching expression, rosy cheeks, "
        "warm beige and dark keys with cream paper tape, "
        "like a baby eating spaghetti but with paper tape"
    ),
    "spool": (
        "A tiny adorable baby robot wrapped snugly in paper tape like a swaddled newborn, "
        "peeking out of the tape wrapping with enormous round curious eyes, "
        "one tiny hand reaching out to touch a binary symbol printed on the tape, "
        "tape has ones and zeros printed along its length, "
        "soft warm cream tape wrapping on a small round brass and blue body, "
        "newborn wonder and innocence energy, very small and precious"
    ),
    "stampy": (
        "A small pudgy adorable robot with rubber stamp feet that leave symbol impressions, "
        "trail of stamped zeros and ones behind it on the ground, "
        "paper tape ribbon tied in a bow on top of its head like a gift ribbon, "
        "ink-smudged rosy cheeks, proud of the marks its making, "
        "carrying a tiny ink pad under one arm, "
        "warm brass body with red ink stains, happy waddling pose"
    ),
    "reely": (
        "A small adorable robot wearing a comically oversized tape reel as a backpack, "
        "the reel is much bigger than the robot and paper tape unwinds behind it as a trail, "
        "robot is leaning forward under the weight with determined happy expression, "
        "like a tiny kid wearing a parent's enormous hiking backpack, "
        "stubby legs taking big steps, warm brass and cream tones, "
        "adventurous and determined despite being tiny"
    ),
    "blinky": (
        "A small adorable robot whose single large eye is a glowing read-head lens, "
        "the eye projects a warm golden spotlight beam down onto a paper tape below, "
        "illuminating one symbol at a time on the tape strip, "
        "the robot leans forward studying the illuminated symbol intently, "
        "lighthouse meets firefly energy, warm golden glow from the eye, "
        "dark blue round body with brass accents, fascinated curious expression"
    ),
    "munch": (
        "A cute adorable caterpillar-shaped robot inching along a strip of paper tape, "
        "each body segment is a different color representing a different state, "
        "reading the symbols on the tape as it crawls along with big curious front eyes, "
        "tiny mechanical legs on each segment, antenna bobbing, "
        "cute inchworm energy, green and brass segments, "
        "the tape is its little road and it follows it happily"
    ),
}


def generate(name, prompt):
    out_path = f"images/I01v2_{name}.png"
    full_prompt = f"{prompt}, {STYLE}"
    payload = json.dumps({
        "prompt": full_prompt,
        "width": 1024,
        "height": 1024,
    }).encode()

    req = urllib.request.Request(
        API, data=payload, headers={"Content-Type": "application/json"}
    )

    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        data = resp.read()
    elapsed = time.time() - t0

    with open(out_path, "wb") as f:
        f.write(data)
    print(f"  done ({elapsed:.0f}s, {len(data)//1024}KB)", flush=True)


def main():
    total = len(CHARACTERS)
    print(f"Generating {total} Issue 1 character concepts (v2)...\n", flush=True)
    t_start = time.time()

    for i, (name, prompt) in enumerate(CHARACTERS.items(), 1):
        print(f"[{i}/{total}] {name}...", end=" ", flush=True)
        try:
            generate(name, prompt)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nDone! {total} images in {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
