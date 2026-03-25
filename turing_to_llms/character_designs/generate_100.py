#!/usr/bin/env python3
"""Generate 10 character design variations per issue (100 total) via Sparky API."""

import json
import time
import urllib.request

API = "http://192.168.6.94:8000/generate"

# Style anchors:
# - Real tech objects as body (not abstract robots)
# - Screen/display faces with simple glowing expressions
# - Tactile, chunky, holdable proportions
# - Warm retro palette: beige plastic, brushed metal, amber glow, green phosphor
# - Visible components: knobs, wires, tubes, resistor stripes
# - MUST match existing comic style: 2D hand-drawn with ink lines and watercolor
STYLE = (
    "cute whimsical approachable character design, chunky tactile proportions, "
    "big friendly expressive face, "
    "comic book style, warm editorial illustration with ink lines and watercolor washes, "
    "warm paper-white background, full body front view"
)

ISSUES = {
    # === ISSUE 1: 1936 — Turing Machine ===
    "I01": {
        "era": "1936 — The Turing Machine",
        "designs": {
            "01_tape_reel": (
                "robot whose body is a reel of punched paper tape with holes visible, "
                "small brass read-write head as one eye, mechanical ticker-tape arms, "
                "copper and brass tones, warm sepia palette"
            ),
            "02_typewriter": (
                "robot made from a vintage mechanical typewriter, keys as teeth in a smile, "
                "paper scroll coming out the top like a hat, ink ribbon spools as ears, "
                "black and chrome with red accents"
            ),
            "03_clockwork": (
                "small wind-up clockwork robot with visible brass gears through glass chest, "
                "large wind-up key on back, tick-tock pendulum tail, "
                "pocket watch face with friendly eyes instead of numbers, antique gold tones"
            ),
            "04_telegraph": (
                "robot made from a brass telegraph key and sounder, "
                "morse code dots and dashes floating around it, "
                "copper wire arms, small bell on head, "
                "warm brass and wood tones, Victorian instrument aesthetic"
            ),
            "05_calculator": (
                "robot made from a vintage mechanical calculator with number wheels, "
                "spinning digit wheels show a smiley face, pull lever as one arm, "
                "heavy cast iron base as feet, cream and black, satisfying chunky build"
            ),
            "06_enigma": (
                "small cute robot made from an Enigma-style rotor cipher machine, "
                "three letter rotors visible on top of head spinning, "
                "plugboard patch cables on chest, keyboard face with letter eyes, "
                "dark green military metal with brass fittings"
            ),
            "07_slide_rule": (
                "robot whose body is a wooden slide rule with sliding center piece, "
                "logarithmic scale markings as decorative patterns, "
                "brass end caps as hands, cursor hairline as a monocle, "
                "warm wood and brass tones"
            ),
            "08_abacus": (
                "small robot made from a wooden abacus frame, "
                "colorful beads on rods form a smiling face pattern, "
                "wooden frame body, bead hands, "
                "bright primary colored beads on warm wood"
            ),
            "09_counter": (
                "robot whose face is a vintage mechanical counter display showing numbers, "
                "flip-digit display eyes that click between expressions, "
                "brushed metal body with rivets, small cranking handle arm, "
                "chrome and dark metal tones"
            ),
            "10_music_box": (
                "tiny robot made from an open music box mechanism, "
                "spinning cylinder with pins as its belly, "
                "small tuned metal comb teeth as a smile, brass frame body, "
                "delicate and intricate, warm gold tones"
            ),
        },
    },
    # === ISSUE 2: 1940s–50s — First Computers ===
    "I02": {
        "era": "1940s–50s — Building the First Brains",
        "designs": {
            "01_vacuum_tube": (
                "robot whose body is a large glowing vacuum tube with warm orange filament inside, "
                "the filament forms a friendly smiling face, thin copper wire limbs, "
                "glass dome head, warm amber glow, bakelite base as feet"
            ),
            "02_patch_panel": (
                "chunky robot whose chest is a telephone patch panel covered in jack ports, "
                "colorful patch cables plugged in everywhere, "
                "one cable arm plugging into its own chest, "
                "black bakelite body with brass jack rings"
            ),
            "03_toggle_switch": (
                "cute boxy robot whose face is a row of toggle switches, "
                "switches flip up and down to make expressions, "
                "indicator lights as eyes that glow red and green, "
                "gray metal front panel body with printed labels"
            ),
            "04_radar_screen": (
                "round robot whose face is a circular green radar display, "
                "sweeping radar line rotates around as a constant smile, "
                "blip dots appear as dimples, chunky military-spec metal body, "
                "olive drab and green phosphor glow"
            ),
            "05_relay": (
                "small robot made from an electromagnetic relay, "
                "clicking armature arm waves hello, electromagnetic coil body, "
                "spark gap smile, copper wire hair, "
                "industrial brass and iron tones"
            ),
            "06_nixie_tube": (
                "robot whose face is a warm glowing nixie tube display showing a smiley, "
                "glass envelope body with visible orange glowing digits inside, "
                "wire pin legs, small and delicate, "
                "warm amber orange glow on dark background"
            ),
            "07_drum_memory": (
                "cylindrical robot whose body is a spinning magnetic drum memory, "
                "read heads as tiny arms reaching toward its own surface, "
                "data tracks as decorative stripes around body, "
                "polished chrome cylinder with warm lighting"
            ),
            "08_oscilloscope": (
                "chunky robot whose face is a vintage oscilloscope screen showing a waveform smile, "
                "rotary knobs as ears, brushed aluminum body, "
                "BNC connector arms, probe tips as hands, "
                "green trace on dark screen, mid-century lab aesthetic"
            ),
            "09_eniac_panel": (
                "robot made from a section of ENIAC computer panel, "
                "grid of indicator lights as eyes and smile pattern, "
                "thick cable bundles as arms, digit ring counters on body, "
                "black panel with warm glowing bulbs"
            ),
            "10_crt_early": (
                "robot whose round face is an early cathode ray tube display, "
                "showing a simple dot-pattern smiley on green phosphor, "
                "heavy glass and metal body, electron gun visible on back, "
                "scientific instrument warmth"
            ),
        },
    },
    # === ISSUE 3: 1950s–60s — Programming Languages ===
    "I03": {
        "era": "1950s–60s — Teaching Machines to Understand Us",
        "designs": {
            "01_punch_card": (
                "robot whose body is a large IBM punch card with rectangular holes punched in pattern, "
                "hole pattern forms a friendly face, ink-stamped label on forehead, "
                "cream and tan card stock colors, holds smaller cards in one hand"
            ),
            "02_tape_drive": (
                "robot with two large magnetic tape reels as eyes on top of head, "
                "tape threading between them, mainframe cabinet body in two-tone gray, "
                "blinking status lights on chest panel"
            ),
            "03_teletype": (
                "robot made from a teletype terminal machine, "
                "keyboard mouth that clacks when talking, paper output scrolling from top, "
                "chunky mechanical body in beige and olive, "
                "bell that dings on its head"
            ),
            "04_core_memory": (
                "small intricate robot whose chest is a visible magnetic core memory grid, "
                "tiny donut-shaped ferrite cores threaded on wires in neat grid pattern, "
                "each core glows softly, delicate wire limbs, "
                "miniature and precious feeling"
            ),
            "05_mainframe_console": (
                "robot shaped like a mainframe operator console, "
                "panel of blinking indicator lights forms a face pattern, "
                "row of switches as a smile, printer output as a scarf, "
                "two-tone blue IBM mainframe colors"
            ),
            "06_card_reader": (
                "chunky robot with a card feed slot as its mouth eating punch cards, "
                "hopper on top full of cards like a hat, "
                "sorting pockets on its sides as arms, "
                "industrial gray with satisfying mechanical feel"
            ),
            "07_line_printer": (
                "wide friendly robot whose body is a chain line printer, "
                "continuous fan-fold paper streaming out as a long tongue or scarf, "
                "print chain visible through window as a smile, "
                "beige and gray with green-bar paper"
            ),
            "08_fortran_card": (
                "cute robot holding a giant FORTRAN program card with code visible, "
                "body is a card deck held together with a rubber band, "
                "pencil behind ear for marking corrections, "
                "cream paper tones with blue grid lines"
            ),
            "09_blinking_panel": (
                "friendly robot whose face is a front panel of blinking lights and switches, "
                "lights blink in patterns to show expressions, "
                "register display on forehead, address switches as eyebrows, "
                "dark panel with colorful indicator lights"
            ),
            "10_paper_tape_reader": (
                "robot feeding paper tape through its own head like a headband, "
                "optical reader sensors as eyes looking at the tape holes, "
                "chad confetti from hole punching floating around, "
                "cream tape with industrial gray body"
            ),
        },
    },
    # === ISSUE 4: 1970s–80s — Unix & PCs ===
    "I04": {
        "era": "1970s–80s — Small Tools Big Ideas",
        "designs": {
            "01_crt_terminal": (
                "robot whose head is a green monochrome CRT monitor showing >_ cursor smile, "
                "beige plastic keyboard as body, floppy disk hands, "
                "chunky beige 1980s computer aesthetic, warm and nostalgic"
            ),
            "02_floppy_disk": (
                "robot whose body is a large 5.25-inch floppy disk with exposed magnetic surface, "
                "write-protect notch as a winking eye, label sticker as name tag, "
                "hub ring as face, thin and flat but charming"
            ),
            "03_acoustic_modem": (
                "robot made from an acoustic coupler modem with two rubber cups on top, "
                "telephone handset resting in cups like antlers, "
                "blinking connection lights as eyes, "
                "beige plastic body with coiled phone cord tail"
            ),
            "04_joystick": (
                "cute robot whose body is a chunky Atari-style joystick base, "
                "joystick stick as a hat or antenna, single red fire button as nose, "
                "black with red button, playful arcade energy"
            ),
            "05_cassette": (
                "robot whose body is an audio cassette tape, "
                "two tape reel hubs as eyes visible through window, "
                "magnetic tape as a scarf trailing behind, "
                "label area shows a friendly drawn face, "
                "TDK or Maxell style coloring"
            ),
            "06_dot_matrix": (
                "wide friendly robot whose body is a dot matrix printer, "
                "perforated tractor-feed paper streaming out as a tongue, "
                "print head zipping back and forth as expression, "
                "beige plastic with satisfying mechanical character"
            ),
            "07_apple_ii": (
                "robot shaped like an Apple II computer with integrated keyboard, "
                "small screen showing a friendly BASIC prompt and smiley, "
                "rainbow stripe across the side, "
                "warm beige plastic with colorful Apple rainbow accent"
            ),
            "08_circuit_board": (
                "robot whose body is an exposed green PCB circuit board, "
                "DIP chip packages as eyes, resistor stripe legs, "
                "colorful capacitors and components sticking up like hair, "
                "solder traces as decorative patterns, maker aesthetic"
            ),
            "09_mouse_early": (
                "cute robot shaped like an early boxy computer mouse, "
                "one big button as a face, cord as a tail, "
                "trackball visible underneath when tipped, "
                "beige plastic with satisfying click feel"
            ),
            "10_unix_pipe": (
                "robot made of connected pipe segments like plumbing, "
                "data flowing through transparent pipe sections as glowing particles, "
                "pipe junction as the head with valve wheel hat, "
                "industrial brass pipes with warm copper fittings"
            ),
        },
    },
    # === ISSUE 5: 1990s–2000s — The Connected World ===
    "I05": {
        "era": "1990s–2000s — The Connected World",
        "designs": {
            "01_dial_up_modem": (
                "robot whose body is an external dial-up modem with blinking LED status lights, "
                "TX RX CD lights as eyes that blink, speaker grille smile, "
                "phone cable tail, making dial-up screech sound, "
                "beige plastic 90s aesthetic"
            ),
            "02_cd_rom": (
                "robot whose round body is a shiny CD-ROM disc, "
                "rainbow light refraction across surface, center spindle hole as nose, "
                "data track rings as decorative spirals, "
                "iridescent holographic shimmer, jewel case as backpack"
            ),
            "03_router": (
                "cute robot shaped like a home WiFi router, "
                "two adjustable antennas as ears that tilt with mood, "
                "row of ethernet port lights as a smile, "
                "blinking activity LEDs as eyes, signal waves emanating"
            ),
            "04_webcam": (
                "small round robot shaped like an early USB webcam on a flexible neck stand, "
                "large camera lens as one big friendly eye, "
                "clip base as feet, LED indicator light on top, "
                "silver and translucent blue iMac-era plastic"
            ),
            "05_ethernet": (
                "tiny robot whose head is an RJ45 ethernet connector plug, "
                "clip tab as a hat brim, eight copper pins as a grin, "
                "long Cat5 cable body in blue, trailing behind like a tail"
            ),
            "06_palm_pilot": (
                "robot shaped like a Palm Pilot PDA, "
                "green LCD touchscreen face showing a pixel smiley, "
                "holding a tiny stylus pen, graffiti handwriting zone as mouth, "
                "dark gray plastic with rounded 90s design"
            ),
            "07_search_engine": (
                "robot holding a large magnifying glass, body covered in index card catalog drawers, "
                "each drawer labeled with a letter, reading glasses on, "
                "warm wood card catalog with brass drawer pulls"
            ),
            "08_globe_browser": (
                "robot whose head is a small spinning globe like the Netscape loading icon, "
                "browser toolbar body with back forward reload buttons as belt buckles, "
                "address bar as headband, bright 90s web colors"
            ),
            "09_imac_g3": (
                "cute robot shaped like a Bondi blue iMac G3, "
                "translucent blue-green plastic body showing colorful internals, "
                "round CRT screen face with friendly expression, "
                "hockey puck mouse as a pet on a leash"
            ),
            "10_server_tower": (
                "friendly robot shaped like a beige desktop PC tower on its side, "
                "CD drive slot as mouth, power button as nose, "
                "cooling fan spinning as a cheek dimple, "
                "beige and dark gray with blinking HDD light eye"
            ),
        },
    },
    # === ISSUE 6: 2000s–2015 — Machines That Learn ===
    "I06": {
        "era": "2000s–2015 — Machines That Learn",
        "designs": {
            "01_gpu_card": (
                "robot whose body is a graphics card GPU with large cooling fan on chest, "
                "heat sink fins as spiky hair, PCIe connector feet, "
                "CUDA cores visible as tiny glowing grid on surface, "
                "dark PCB green with RGB LED accents"
            ),
            "02_server_rack": (
                "tall thin robot made from a server rack unit, "
                "horizontal drive bay lights as eyes and smile, "
                "rails as arms, blinking blue LEDs, "
                "black metal with cool blue data center glow"
            ),
            "03_raspberry_pi": (
                "tiny cute robot whose body is a Raspberry Pi board, "
                "GPIO pins as spiky hair standing up, "
                "Broadcom chip as face with friendly eyes etched on, "
                "USB and HDMI ports as arms, credit-card sized and adorable, "
                "green PCB with silver components"
            ),
            "04_usb_drive": (
                "small robot shaped like a USB flash drive with cap, "
                "cap pops off as a hat it carries, USB connector feet, "
                "LED activity light as a glowing heart on chest, "
                "metallic with translucent colored plastic shell"
            ),
            "05_camera_vision": (
                "robot with a large DSLR camera lens as one big eye, "
                "photo sensor grid visible in the eye, "
                "body covered in small labeled photographs it has classified, "
                "holding up a photo and examining it with curiosity"
            ),
            "06_neural_display": (
                "robot whose chest is a transparent display showing a simple neural network diagram, "
                "nodes light up and connections pulse when thinking, "
                "small and chunky body, antenna with a lightbulb tip for ideas, "
                "dark body with glowing blue-purple network inside"
            ),
            "07_training_bot": (
                "cute robot surrounded by floating labeled data cards and images, "
                "trying to sort cats vs dogs photos into two bins, "
                "confused but determined expression, checkmark and X stamps in hands, "
                "warm and humorous scene"
            ),
            "08_weight_dial": (
                "robot covered in small adjustment dials and sliders, "
                "constantly fine-tuning itself, one hand turning a dial on its own chest, "
                "meter gauge face showing a smile when well-tuned, "
                "analog instrument panel aesthetic"
            ),
            "09_data_funnel": (
                "robot with a large funnel on top of head collecting falling data points, "
                "data flows through its transparent body and comes out organized, "
                "input messy and colorful, output neat and labeled, "
                "glass and chrome, whimsical data pipeline"
            ),
            "10_cuda_core": (
                "tiny robot that is one of thousands — single small green glowing core, "
                "simple dot eyes, shown in a massive grid formation with identical friends, "
                "parallel processing visual, each doing a tiny math operation, "
                "green glow on dark background, strength in numbers"
            ),
        },
    },
    # === ISSUE 7: 2017–2023 — Transformers & LLMs ===
    "I07": {
        "era": "2017–2023 — Attention Is All You Need",
        "designs": {
            "01_token_block": (
                "robot whose body is made of stacked colorful word-piece token blocks like building blocks, "
                "each block has a word fragment printed on it, blocks can rearrange, "
                "friendly face on the top block, "
                "pastel colored blocks like wooden alphabet toys"
            ),
            "02_chat_bubble": (
                "robot shaped like a speech bubble or chat message bubble, "
                "rounded rectangle body with the tail-point as feet, "
                "text cursor blinking as an eye, typing dots animation as expression, "
                "soft blue-white with subtle gradient"
            ),
            "03_attention_head": (
                "small robot with a lighthouse-style head emitting colored attention beams, "
                "beams connect to floating word tokens around it, "
                "each beam a different color for multi-head attention, "
                "warm lantern glow, brass lighthouse body"
            ),
            "04_embedding_bot": (
                "robot floating in a starfield of glowing dots representing embedding space, "
                "similar-meaning dots cluster near it, "
                "small compass in hand pointing toward related concepts, "
                "deep blue space with warm golden dot clusters"
            ),
            "05_context_window": (
                "robot whose body is a scrolling text window or terminal, "
                "text content visible on its surface scrolling slowly, "
                "magnifying glass examining its own text, "
                "frame around body like a display border, warm cream text on dark"
            ),
            "06_softmax": (
                "robot shaped like a probability distribution bar chart, "
                "bars of different heights form its body silhouette, "
                "tallest bar has a glowing confident face, smaller bars look uncertain, "
                "gradient from blue to orange"
            ),
            "07_transformer_block": (
                "robot whose body is a schematic Transformer block diagram made physical, "
                "layer norm as a belt, attention as a glowing chest core, "
                "feed-forward as strong arms, residual connection as a scarf loop, "
                "technical but cute, blueprint blue tones"
            ),
            "08_tokenizer": (
                "robot with scissors and a ruler, actively cutting a long word into subword pieces, "
                "word fragments scattered around like confetti, "
                "meticulous craftsperson energy, apron with pockets full of tokens, "
                "warm workshop aesthetic"
            ),
            "09_scaling_bot": (
                "set of three robots in increasing sizes — small medium and large, "
                "same design but each bigger and glowing brighter, "
                "smallest is simple, largest is complex with more detail, "
                "showing scaling laws visually, warm gradient sizing"
            ),
            "10_prompt_box": (
                "robot whose body is a text input field with blinking cursor, "
                "placeholder text as a subtle face, send button as a heart, "
                "clean minimal design like a chat interface component, "
                "soft rounded corners, modern UI aesthetic with warm tones"
            ),
        },
    },
    # === ISSUE 8: 2024–2025 — AI Agents ===
    "I08": {
        "era": "2024–2025 — The Agent Awakens",
        "designs": {
            "01_terminal_agent": (
                "robot whose body is a dark terminal window with scrolling green code, "
                "blinking cursor as one eye, command prompt face, "
                "tool belt with miniature browser file-icon and database icons, "
                "dark mode aesthetic with syntax highlighting accents"
            ),
            "02_swiss_army": (
                "robot designed like a Swiss Army knife with multiple tool arms folding out, "
                "browser arm, code editor arm, terminal arm, file search arm, "
                "red body with chrome tools, compact when closed, "
                "resourceful and prepared energy"
            ),
            "03_clipboard": (
                "robot holding a clipboard with a checklist, checking items off, "
                "plan-then-execute energy, pencil behind ear, "
                "reading glasses, thoughtful determined expression, "
                "warm wood clipboard with white paper and green checkmarks"
            ),
            "04_debugger": (
                "robot wearing a detective outfit — magnifying glass, deerstalker hat, "
                "examining a glowing red bug caught in tweezers, "
                "code scrolling on monocle lens, "
                "Sherlock Holmes meets robot debugger, warm and whimsical"
            ),
            "05_sandbox": (
                "cute robot sitting inside a sandbox play area but the sand is code, "
                "building castles out of code blocks, "
                "bucket and shovel but the shovel has a cursor icon, "
                "playful experimentation energy, warm sandbox tones"
            ),
            "06_loop_bot": (
                "robot shaped like a circular arrow or loop symbol, "
                "running around its own loop body endlessly, "
                "observe-think-act icons at each curve of the loop, "
                "energetic and iterative, warm orange-blue arrows"
            ),
            "07_file_reader": (
                "robot with large reading glasses examining an open file folder, "
                "documents and code pages spread around, "
                "taking notes in a small notebook, studious expression, "
                "warm office aesthetic with manila folders and paper"
            ),
            "08_api_connector": (
                "robot whose arms are various plugs and connectors — USB, ethernet, API endpoint, "
                "body covered in port icons, adapting and connecting to everything, "
                "universal adapter energy, colorful cables trailing"
            ),
            "09_error_fixer": (
                "small determined robot holding a wrench and soldering iron, "
                "standing next to a red error message it is fixing, "
                "error turning green as it works, sparks flying, "
                "can-do attitude, warm workshop lighting"
            ),
            "10_context_brain": (
                "robot with a transparent dome head showing a glowing brain, "
                "the brain has a progress bar showing context usage filling up, "
                "files and code floating in the dome, "
                "purple glow, slightly worried expression as bar fills"
            ),
        },
    },
    # === ISSUE 9: 2025–2026 — The Swarm ===
    "I09": {
        "era": "2025–2026 — The Swarm",
        "designs": {
            "01_mini_cluster": (
                "group of 5 tiny identical cute round one-eyed robots in a V formation, "
                "glowing connection lines between them forming a network, "
                "one slightly in front as leader, others following, "
                "silver and emerald green, collective movement"
            ),
            "02_hive_hex": (
                "cluster of small hexagonal robots that tessellate together like honeycomb, "
                "each hex has a simple face, together they form a larger face pattern, "
                "warm honey-gold and dark amber tones, "
                "organic colony structure"
            ),
            "03_git_branch": (
                "robot whose body is a git branch diagram with diverging and merging paths, "
                "small agent bots working at each branch tip, "
                "merge commit points glow green, conflict points glow red, "
                "flowing organic tree structure"
            ),
            "04_conductor": (
                "robot orchestra conductor with a baton, conducting a group of 6 tiny worker bots, "
                "each worker bot plays a different instrument-tool, "
                "musical coordination metaphor, tuxedo and baton, "
                "warm concert hall lighting"
            ),
            "05_matryoshka": (
                "set of nesting robots like Russian matryoshka dolls, "
                "largest orchestrator contains medium specialist which contains small worker, "
                "shown partially opened revealing the layers, "
                "painted wooden doll aesthetic with robot features"
            ),
            "06_constellation": (
                "group of small glowing robot-stars arranged in a constellation pattern in dark sky, "
                "connection lines drawn between them like star chart, "
                "each star-bot has a tiny face, constellation forms a larger shape, "
                "deep blue with warm golden star-bots"
            ),
            "07_ant_colony": (
                "group of tiny mechanical ant robots carrying data blocks together, "
                "forming an assembly line, each ant simple but together building something complex, "
                "organized trail patterns, warm copper mechanical ants"
            ),
            "08_network_hub": (
                "central hub robot connected by glowing lines to 6 orbiting specialist bots, "
                "hub is larger with a coordinator expression, "
                "each satellite bot has a different tool icon, "
                "star topology layout, cool blue connections"
            ),
            "09_puzzle_pieces": (
                "group of 6 jigsaw puzzle piece robots that fit together into one complete picture, "
                "shown partially assembled, each piece has its own face and color, "
                "satisfying interlocking connections, warm colorful pastel pieces"
            ),
            "10_swarm_cloud": (
                "cloud-shaped formation of dozens of tiny identical simple dot-bots, "
                "moving together like a murmuration of starlings, "
                "the swarm shape forms a friendly face, individual bots barely visible, "
                "emergent behavior, silver dots with blue glow trails"
            ),
        },
    },
    # === ISSUE 10: 1936–2026 — The Whole Stack ===
    "I10": {
        "era": "1936–2026 — The Whole Stack",
        "designs": {
            "01_layer_cake": (
                "robot shaped like a layer cake where each layer is a computing era, "
                "bottom layer brass gears, then vacuum tubes, then chips, then screens, "
                "top layer is glowing AI, candle antenna on top, "
                "colorful layers, each in its era's palette"
            ),
            "02_evolution_line": (
                "lineup of 7 robots showing evolution from simple mechanical to complex AI, "
                "leftmost is tiny brass clockwork, rightmost is glowing modern, "
                "shown in evolution march pose, each a different era, "
                "warm gradient from sepia to blue"
            ),
            "03_telescope": (
                "robot looking through a telescope that shows the future while standing on a stack of history books, "
                "each book spine labeled with an era, brass telescope, "
                "explorer and historian energy, warm library lighting"
            ),
            "04_time_capsule": (
                "robot whose body is an open time capsule filled with computing artifacts, "
                "vacuum tube, punch card, floppy disk, CD, GPU chip visible inside, "
                "robot presenting the collection proudly, "
                "warm museum display lighting"
            ),
            "05_stacked_blocks": (
                "robot made of stacked building blocks where each block is a different technology, "
                "binary at bottom, transistors, code, internet, AI at top, "
                "colorful educational toy aesthetic, "
                "wooden blocks with tech icons printed on them"
            ),
            "06_tree_of_computing": (
                "robot shaped like a small bonsai tree, "
                "roots are circuits, trunk is code, branches are networks, "
                "leaves are AI nodes that glow, fruit are applications, "
                "organic tech hybrid, warm earthy tones with tech glow"
            ),
            "07_museum_guide": (
                "robot dressed as a museum guide with a lanyard and badge, "
                "flashlight pointing at a wall timeline of computing milestones, "
                "friendly educational pose, surrounded by display artifacts, "
                "warm museum lighting, enthusiastic expression"
            ),
            "08_gradient_bot": (
                "robot whose body color gradient transitions from sepia at the feet to modern blue at the head, "
                "design details evolve upward — gear feet, tube legs, chip torso, screen chest, AI head, "
                "smooth blended transition, walking timeline"
            ),
            "09_backpack": (
                "small cute robot with an enormous overflowing backpack, "
                "computing artifacts poking out — tape reels, cables, cards, a tiny laptop, "
                "cheerful despite heavy load, collecting all of computing history, "
                "warm adventurer energy"
            ),
            "10_prism": (
                "robot holding a glass prism that splits a white beam of light into rainbow layers, "
                "each color represents a computing era labeled subtly, "
                "the spectrum fans out beautifully, "
                "Dark Side of the Moon meets computing history, dramatic lighting"
            ),
        },
    },
}


def generate(name, prompt):
    out_path = f"images/{name}.png"
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
    return elapsed, len(data)


def main():
    total = sum(len(iss["designs"]) for iss in ISSUES.values())
    print(f"Generating {total} character designs via Sparky API...\n", flush=True)
    t_start = time.time()
    count = 0

    for issue_key, issue_data in ISSUES.items():
        era = issue_data["era"]
        designs = issue_data["designs"]
        print(f"\n{'='*60}", flush=True)
        print(f"  {issue_key}: {era} ({len(designs)} designs)", flush=True)
        print(f"{'='*60}", flush=True)

        for name, prompt in designs.items():
            count += 1
            full_name = f"{issue_key}_{name}"
            print(f"  [{count}/{total}] {full_name}...", end=" ", flush=True)
            try:
                elapsed, size = generate(full_name, prompt)
                print(f"done ({elapsed:.0f}s, {size//1024}KB)", flush=True)
            except Exception as e:
                print(f"FAILED: {e}", flush=True)

    elapsed = time.time() - t_start
    print(f"\nAll done! {count} images in {elapsed/60:.1f} minutes", flush=True)


if __name__ == "__main__":
    main()
