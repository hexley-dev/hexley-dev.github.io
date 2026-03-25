#!/usr/bin/env python3
"""Generate 10 Scribble v2 variations — magnifying glass hand, pencil hand, symbol tape."""

import json
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

STYLE = (
    "comic book style, warm editorial illustration with ink lines and watercolor washes, "
    "adorable cute kawaii appeal, big expressive eyes, warm paper-white background, "
    "full body view, character design"
)

# Core identity v2:
# - Tiny round brass robot on a onewheel riding along paper tape
# - One hand holds a magnifying glass (read head) — examining symbols
# - Other hand holds a pencil (write head) — writing symbols
# - NO monocle — magnifying glass is held, not worn
# - Paper tape has diverse symbols (not just binary): letters, shapes, marks, ə, x, 0, 1, ∀, □
# - Paper tape as scarf/trail streaming behind

CORE = (
    "A tiny adorable round brass robot riding a onewheel electric board along a strip of paper tape, "
    "one hand holding a magnifying glass examining the tape symbols, "
    "other hand holding a small pencil ready to write, "
    "the paper tape has diverse mathematical symbols and marks printed on it "
    "including letters shapes zeros ones and abstract notation marks, "
    "long paper tape scarf with symbols streaming behind in the wind, "
    "warm brass and cream colored body, big expressive curious eyes, "
)

CHARACTERS = {
    "01_cruiser": (
        CORE +
        "casual confident surf stance balanced on the onewheel, "
        "relaxed happy grin, magnifying glass held out to the side casually, "
        "pencil tucked behind antenna, wind in the tape scarf, "
        "the paper tape road stretches into the distance ahead"
    ),
    "02_explorer": (
        CORE +
        "leaning forward excitedly on the onewheel, eyes wide with wonder, "
        "holding magnifying glass up to examine a new symbol on the tape ahead, "
        "pencil poised ready to note something down, tiny explorer satchel on back, "
        "sense of adventure and discovery, tape trail winds into unknown"
    ),
    "03_thinker": (
        CORE +
        "balanced perfectly still on the onewheel, deep in thought, "
        "magnifying glass lowered thoughtfully, pencil eraser end tapping chin, "
        "eyes looking up and to the side pondering, tiny thought bubbles above, "
        "peaceful contemplative expression, tape scarf draped gently"
    ),
    "04_speedster": (
        CORE +
        "deep low crouch racing stance on the onewheel going fast, "
        "magnifying glass held forward like a shield cutting through wind, "
        "pencil gripped tight pointing back, tape scarf fully horizontal from speed, "
        "motion blur lines, thrilled fearless grin, red racing stripe on body"
    ),
    "05_reader": (
        CORE +
        "rolling slowly on the onewheel completely absorbed in reading, "
        "magnifying glass held right up to the tape examining each symbol closely, "
        "pencil in other hand making tiny annotations on the tape margin, "
        "studious concentrated expression tongue sticking out slightly, oversized round glasses"
    ),
    "06_dancer": (
        CORE +
        "doing a graceful spin trick balanced on the onewheel, "
        "magnifying glass raised high catching a sparkle of light, "
        "pencil sweeping through air leaving a faint trail like a baton, "
        "tape scarf twirling in a beautiful spiral around the figure, "
        "joyful laughing expression, pure delight and grace"
    ),
    "07_nightrider": (
        CORE +
        "riding the onewheel through darkness at night, brave and determined, "
        "magnifying glass glowing with warm golden light illuminating the tape ahead, "
        "pencil leaving a faint luminescent trail behind, "
        "tape scarf has softly glowing symbols visible in the dark, "
        "starry deep blue background, riding through mystery with its own light"
    ),
    "08_writer": (
        CORE +
        "riding the onewheel along BLANK paper tape, actively creating, "
        "magnifying glass tucked under arm momentarily, "
        "pencil hand busy writing fresh new symbols onto the blank tape as it rides, "
        "behind the robot the tape has newly written symbols, ahead the tape is blank and empty, "
        "ink-stained fingers, concentrated creative expression, the act of creation"
    ),
    "09_teacher": (
        CORE +
        "stopped on the onewheel turned toward the viewer making eye contact, "
        "magnifying glass held up invitingly to show a symbol to the reader, "
        "pencil pointing at a section of tape like a teacher at a chalkboard, "
        "warm friendly open posture, tiny bow tie, welcoming encouraging smile, "
        "saying come learn with me energy"
    ),
    "10_legend": (
        CORE +
        "heroic pose standing tall on the onewheel silhouetted against warm golden light, "
        "magnifying glass raised like a torch of discovery, "
        "pencil held high like a tiny sword of knowledge, "
        "tape scarf billowing dramatically behind like a superhero cape, "
        "dramatic warm backlighting, confident inspiring expression, "
        "legendary and epic but still tiny and adorable"
    ),
}


def generate(name, prompt):
    out_path = f"images/scribblev2_{name}.png"
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
    print(f"Generating {total} Scribble v2 variations...\n", flush=True)
    t_start = time.time()

    for i, (name, prompt) in enumerate(CHARACTERS.items(), 1):
        print(f"[{i}/{total}] scribblev2_{name}...", end=" ", flush=True)
        try:
            generate(name, prompt)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nDone! {total} images in {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
