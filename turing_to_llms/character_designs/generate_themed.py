#!/usr/bin/env python3
"""Generate era-themed robot guide character designs via Sparky API."""

import json
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

CHARACTERS = {
    "T01_ticker": (
        "Character design sheet, cute robot character named Ticker themed around 1936 Turing machines, "
        "body is a reel of punched paper tape wrapped in a coil shape, brass and copper mechanical parts, "
        "a read-write head mechanism as its single eye, mechanical typewriter key fingertips, "
        "small brass gears visible, warm sepia and gold tones, Victorian-era scientific instrument aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T02_valvie": (
        "Character design sheet, cute robot character named Valvie themed around 1940s vacuum tube computers, "
        "chest and torso made of large glowing glass vacuum tubes with warm orange filaments inside, "
        "face is a vintage rotary telephone dial with friendly eyes above it, "
        "arms made of thick rubber-insulated electrical cables with plug connectors as hands, "
        "patch cable panel on back, warm amber glow, ENIAC-era electronics aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T03_punchy": (
        "Character design sheet, cute robot character named Punchy themed around 1950s-60s programming, "
        "body is a large IBM punch card rectangular shape with actual punched hole patterns visible, "
        "friendly face ink-stamped onto the card surface, holding a stack of punch cards under one arm, "
        "wearing a small Navy officer cap like Grace Hopper, cream and tan card colors, "
        "small sturdy legs, mid-century office aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T04_shell": (
        "Character design sheet, cute robot character named Shell themed around 1970s-80s personal computers, "
        "head is a vintage green monochrome CRT monitor displaying a command prompt cursor >_ as a smile, "
        "body is a beige plastic computer keyboard with chunky keys, "
        "hands are 3.5 inch floppy disks, small boxy legs, "
        "green phosphor glow from screen, 1980s beige computer aesthetic, dust and warmth, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T05_dotcom": (
        "Character design sheet, cute robot character named Dotcom themed around 1990s-2000s World Wide Web, "
        "body is a vintage Netscape-era web browser window frame with navigation buttons and address bar, "
        "head is a spinning globe like the old Netscape loading animation, "
        "blue hyperlink text visible across its surface body, "
        "small antenna shaped like HTML angle bracket tags, "
        "bright 90s web colors blue purple and teal, early internet aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T06_neuron": (
        "Character design sheet, cute robot character named Neuron themed around deep learning and neural networks, "
        "translucent glass-like body showing a glowing neural network inside with bright nodes and connections, "
        "pulsing colored signals traveling along the pathways inside its body, "
        "friendly face formed by two large node-like eyes and a curved connection smile, "
        "soft blue and purple bioluminescent glow, gradient colors flowing through connections, "
        "scientific and ethereal aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T07_attn": (
        "Character design sheet, cute robot character named Attn themed around transformer AI and attention mechanism, "
        "geometric angular head with multiple colored light beams radiating outward like attention connections, "
        "body surface covered in matrix-like patterns of numbers and symbols, "
        "small floating token blocks orbiting around its head like electrons, "
        "sleek modern design, electric blue and warm orange color scheme, "
        "futuristic but friendly, glowing attention rays, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T08_cursor": (
        "Character design sheet, cute robot character named Cursor themed around AI coding agents, "
        "body is a dark terminal window with live scrolling green code text on its surface, "
        "one eye is a blinking text cursor, the other a normal friendly eye, "
        "wearing a tool belt with miniature icons of a web browser file folder and database, "
        "hands appear to be typing, keyboard keys on fingertips, "
        "dark mode color scheme with syntax highlighting accents green blue orange, "
        "Pixar 3D render style, soft studio lighting, white background, full body view"
    ),
    "T09_hivemind": (
        "Character design sheet, cute multi-agent swarm robot named Hivemind, "
        "NOT one robot but a cluster of 5 to 7 tiny identical mini-robots moving in formation, "
        "each mini-robot is a small simple sphere with one eye, "
        "glowing connection lines between them like a network graph, "
        "they occasionally merge together into a larger composite robot form shown alongside, "
        "git branch diagram patterns glowing between them, "
        "emerald green and silver color scheme, collective intelligence aesthetic, "
        "Pixar 3D render style, soft studio lighting, white background, full group view"
    ),
    "T10_stack": (
        "Character design sheet, cute layered robot named Stack representing all eras of computing history, "
        "body is made of distinct horizontal layers stacked on top of each other like geological strata, "
        "bottom layer is paper tape and brass gears for 1936, "
        "next layer up is vacuum tubes glowing orange for 1940s, "
        "middle layers are punch cards then green CRT screen then web browser elements, "
        "upper layer is neural network nodes, top is glowing AI attention beams, "
        "each layer in its era's color palette, walking timeline of computing, warm orange tones overall, "
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
    print(f"  Done ({elapsed:.0f}s, {len(data)//1024}KB)", flush=True)


def main():
    total = len(CHARACTERS)
    print(f"Generating {total} era-themed character designs via Sparky API...\n", flush=True)
    t_start = time.time()

    for i, (name, prompt) in enumerate(CHARACTERS.items(), 1):
        print(f"[{i}/{total}] {name}", flush=True)
        try:
            generate(name, prompt)
        except Exception as e:
            print(f"  FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nDone! Total time: {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
