#!/usr/bin/env python3
"""Generate 10 Scribble-on-a-onewheel variations."""

import json
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

STYLE = (
    "comic book style, warm editorial illustration with ink lines and watercolor washes, "
    "adorable cute kawaii appeal, big expressive eyes, warm paper-white background, "
    "full body view, character design"
)

# Core identity: tiny round robot, paper tape scarf, pencil (write head),
# monocle/magnifying glass (read head), riding a onewheel on a tape strip
CHARACTERS = {
    "01_cruiser": (
        "A tiny adorable round brass robot riding a onewheel electric skateboard along a strip of paper tape, "
        "casual confident surf stance with one arm out for balance, "
        "long paper tape scarf with binary symbols streaming behind in the wind, "
        "magnifying glass monocle over one big curious eye, pencil tucked behind antenna like behind an ear, "
        "warm brass and cream body, rosy cheeks, cool relaxed grin, "
        "the paper tape is the road stretching into the distance"
    ),
    "02_explorer": (
        "A tiny adorable round brass robot riding a onewheel electric board along paper tape like a trail, "
        "leaning forward excitedly pointing ahead with pencil hand at something it discovered, "
        "paper tape scarf with ones and zeros flying behind, "
        "magnifying glass monocle glinting with reflected light over one big amazed eye, "
        "wearing a tiny explorer satchel bag, warm brass body with copper accents, "
        "sense of adventure and discovery, the tape trail winds ahead into the unknown"
    ),
    "03_thinker": (
        "A tiny adorable round brass robot standing on a onewheel electric board balanced on paper tape, "
        "completely still and balanced, one hand on chin thinking deeply, "
        "pencil held loosely in other hand with eraser end tapping its head, "
        "magnifying glass monocle over one squinting thoughtful eye, "
        "paper tape scarf draped still around neck with visible symbols, "
        "warm brass body, peaceful contemplative expression, "
        "tiny thought bubbles with binary symbols floating above"
    ),
    "04_speedster": (
        "A tiny adorable round brass robot zooming fast on a onewheel electric board along paper tape, "
        "deep low crouch speed stance leaning hard forward, "
        "paper tape scarf stretched fully horizontal behind from sheer speed, "
        "magnifying glass monocle has a speed-streak gleam, pencil gripped like a sword pointing forward, "
        "motion blur lines behind, warm brass body with red racing stripe, "
        "thrilled fearless grin, the paper tape road blurs underneath"
    ),
    "05_reader": (
        "A tiny adorable round brass robot slowly rolling on a onewheel along paper tape, "
        "holding the paper tape scarf up to its magnifying glass monocle reading the symbols carefully, "
        "completely absorbed in reading while riding, pencil in other hand making notes on the tape, "
        "studious concentrated expression with tongue sticking out slightly, "
        "warm brass and cream body, oversized round glasses in addition to monocle, "
        "gentle rolling motion, the tape feeds through its hands as it rides and reads"
    ),
    "06_dancer": (
        "A tiny adorable round brass robot doing a trick on a onewheel electric board on paper tape, "
        "one foot on the board doing a graceful spin with arms wide, "
        "paper tape scarf twirling around it in a beautiful spiral, "
        "magnifying glass monocle catching light with a sparkle, pencil conducting the air like a baton, "
        "joyful laughing expression, warm brass body with gold highlights, "
        "paper tape curling in elegant loops around the spinning figure"
    ),
    "07_nightrider": (
        "A tiny adorable round brass robot riding a onewheel along paper tape at night, "
        "the magnifying glass monocle projects a warm golden spotlight beam ahead illuminating the tape symbols, "
        "pencil held like a tiny torch leaving a faint glowing trail, "
        "paper tape scarf has glowing luminescent symbols visible in the dark, "
        "warm brass body with subtle internal glow, determined brave expression, "
        "riding through darkness with its own light, starry deep blue background"
    ),
    "08_writer": (
        "A tiny adorable round brass robot riding a onewheel along BLANK paper tape, "
        "actively writing new symbols onto the blank tape with its pencil as it rides forward, "
        "behind it the tape has fresh symbols it just wrote, ahead the tape is blank and empty, "
        "magnifying glass monocle focused on the writing point, concentrated creative expression, "
        "warm brass body with ink-stained fingers, paper tape scarf with completed symbols behind, "
        "the act of creation while moving forward"
    ),
    "09_teacher": (
        "A tiny adorable round brass robot on a onewheel electric board, stopped and turned toward the viewer, "
        "pointing at a section of paper tape with its pencil like a teacher at a blackboard, "
        "magnifying glass monocle raised up on forehead, big warm inviting eyes making eye contact, "
        "paper tape scarf arranged to show clear readable binary symbols as a teaching aid, "
        "warm friendly open posture, brass body with a tiny bow tie, "
        "welcoming and encouraging expression, like saying come learn with me"
    ),
    "10_legend": (
        "A tiny adorable round brass robot doing a heroic pose standing tall on a onewheel electric board, "
        "paper tape scarf billowing dramatically behind like a superhero cape in the wind, "
        "pencil raised high like a tiny sword of knowledge, "
        "magnifying glass monocle gleaming with determination, "
        "warm brass body polished to a shine with golden highlights, "
        "confident inspiring expression looking toward the horizon, "
        "dramatic warm backlighting creating a silhouette glow, legendary and epic but still tiny and cute"
    ),
}


def generate(name, prompt):
    out_path = f"images/scribble_{name}.png"
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
    print(f"Generating {total} Scribble variations...\n", flush=True)
    t_start = time.time()

    for i, (name, prompt) in enumerate(CHARACTERS.items(), 1):
        print(f"[{i}/{total}] scribble_{name}...", end=" ", flush=True)
        try:
            generate(name, prompt)
        except Exception as e:
            print(f"FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nDone! {total} images in {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
