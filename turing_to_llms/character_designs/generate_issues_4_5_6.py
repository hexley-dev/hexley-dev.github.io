#!/usr/bin/env python3
"""50 curated character design prompts each for Issues 4, 5, and 6."""

BASE = (
    "A cute tiny round robot character with two expressive dark eyes, small feet, "
    "photo-realistic, studio lighting, white seamless background, product photography style, "
    "sharp focus, 8k detail"
)

# =============================================================================
# ISSUE 4: "Pipe" — 1970s-1980s, Small Tools Big Ideas
# Era: Unix, C language, Bell Labs, personal computers, free software, ARPANET
# =============================================================================
ISSUE_04_DESIGNS = [
    ("copper_pipe_modular",
     f"{BASE}. Body made of interconnected copper plumbing pipes and fittings, each pipe segment a different Unix tool, brass elbow joints as shoulders, patina-green oxidation spots, tiny wrench held in one hand."),

    ("bell_labs_walnut",
     f"{BASE}. Body carved from warm walnut wood with Bell Labs logo etched into chest, amber CRT screen for a face, brushed aluminum antenna ears, sitting on a miniature PDP-11 console."),

    ("floppy_disk_stack",
     f"{BASE}. Body assembled from stacked 5.25-inch floppy disks in rainbow colors, metal hub ring as a monocle, magnetic tape ribbon scarf, legs made of disk drive rails, beige plastic trim."),

    ("amber_terminal",
     f"{BASE}. Head is an amber CRT monitor displaying a blinking cursor, body is a chunky beige keyboard with mechanical switches, feet are rubber dome keycaps, warm orange glow emanating from screen."),

    ("corduroy_hacker",
     f"{BASE}. Wearing a tiny brown corduroy jacket with elbow patches, body made of green PCB with visible copper traces, soldering iron tucked behind ear, small breadboard backpack."),

    ("unix_pipe_chain",
     f"{BASE}. Body is a series of chrome pipes connected by | symbols, data flowing as tiny glowing characters through transparent pipe sections, each segment labeled with Unix commands like grep and awk."),

    ("pdp11_minicomputer",
     f"{BASE}. Body shaped like a miniature PDP-11 front panel with rows of toggle switches and blinking LEDs, magnetic core memory visible through chest window, heavy industrial gray metal finish."),

    ("cassette_tape_dj",
     f"{BASE}. Body is a chunky audio cassette tape with visible magnetic tape reels spinning as eyes, pencil stuck through one reel for rewinding, orange shag carpet texture base, 70s wood-grain side panels."),

    ("garage_workshop",
     f"{BASE}. Covered in sawdust and solder flux, wearing safety goggles pushed up on forehead, body made of pegboard with tiny tools hanging off it, workbench apron, single bare lightbulb overhead glow."),

    ("green_pcb_heart",
     f"{BASE}. Torso is a green printed circuit board with a glowing red LED heart at center, copper trace veins branching outward, DIP socket mouth, capacitor arms, resistor stripe belt."),

    ("modem_dialup_70s",
     f"{BASE}. Body is a chunky acoustic coupler modem with rubber cups for ears, telephone handset resting on top, coiled phone cord tail, beige plastic with brown accents, tiny blinking status lights."),

    ("joystick_pilot",
     f"{BASE}. Body is a classic Atari-style joystick with red button nose, black rubber stick as a jaunty hat, molded grip texture body, single thick cable as tail, matte black with chrome accents."),

    ("wire_frame_globe",
     f"{BASE}. Head is a wireframe globe made of thin green phosphor lines representing ARPANET nodes, copper wire body with solder joint knees, tiny packet envelopes orbiting the globe head."),

    ("c_language_concrete",
     f"{BASE}. Body made of poured concrete with curly braces carved into chest, pointer arrows as antennae, wearing a hard hat, industrial brutalist aesthetic mixed with warm amber backlighting."),

    ("vinyl_record_belly",
     f"{BASE}. Round belly is a spinning vinyl record with grooves visible, tonearm as one arm, chrome turntable base as feet, album sleeve peeking out from under arm, warm analog warmth glow."),

    ("orange_shag_retro",
     f"{BASE}. Entirely covered in orange shag carpet texture like a 70s living room, lava lamp antenna on head glowing red-orange, wood-paneled TV screen face showing a smiley, macramé belt."),

    ("soldering_iron_wizard",
     f"{BASE}. Wielding a soldering iron like a magic wand with a wisp of rosin smoke, body made of tin solder wire coils, flux-stained apron, magnifying visor over one eye, warm workshop lighting."),

    ("denim_patches_free",
     f"{BASE}. Body wrapped in worn denim with embroidered patches reading 'GNU' and 'FREE', peace sign button on chest, headband with tiny antenna, 70s counterculture meets computing aesthetic."),

    ("chrome_bumper_muscle",
     f"{BASE}. Body styled like a 70s muscle car with chrome bumper grin, round headlight eyes, hood scoop on top of head, rubber tire feet, Detroit chrome and candy apple red metallic paint."),

    ("beige_pc_tower",
     f"{BASE}. Body is a miniature beige PC tower with 5.25-inch drive bay mouth, power button nose, ventilation grill cheeks, yellowed plastic patina, tiny turbo button on chest glowing green."),

    ("rubber_duck_debugger",
     f"{BASE}. Rubber duck yellow body with circuit board patterns printed on surface, tiny terminal screen monocle, USB port mouth, sitting on a stack of punch cards, debugging companion energy."),

    ("command_line_zen",
     f"{BASE}. Minimalist brushed aluminum body with a single green phosphor terminal screen face showing '$ _', no decoration except a blinking cursor, serene and focused, zen garden of gravel around feet."),

    ("modular_synth_pipes",
     f"{BASE}. Body is a modular synthesizer rack with patch cables connecting different sections like Unix pipes, knobs and sliders on chest, oscilloscope waveform eyes, chrome and walnut wood."),

    ("bell_labs_scientist",
     f"{BASE}. Wearing a tiny white lab coat with Bell Labs badge, body made of brushed stainless steel, holding a miniature transistor between thumb and finger, horn-rimmed glasses, 1970s scientist vibe."),

    ("punched_card_origami",
     f"{BASE}. Body folded origami-style from a Hollerith punched card, rectangular holes creating lace-like patterns, crisp manila cardstock texture, corners slightly dog-eared, geometric and precise."),

    ("copper_plumber_overalls",
     f"{BASE}. Wearing tiny copper-colored overalls with pipe wrench in back pocket, body made of soldered copper pipe fittings, flux-stained hands, pipe thread tape wrapped around one arm, plumber chic."),

    ("amber_and_walnut",
     f"{BASE}. Body split: left half warm walnut wood grain, right half amber translucent resin with tiny circuits embedded inside, visible where wood meets technology, mid-century modern furniture aesthetic."),

    ("arpanet_postman",
     f"{BASE}. Wearing a tiny mail carrier uniform and hat, body made of network cable bundles, carrying a satchel overflowing with data packets (tiny envelopes with IP addresses), cheerful delivery robot."),

    ("toggle_switch_samurai",
     f"{BASE}. Body covered in rows of tiny toggle switches like PDP-11 front panel, each in different positions forming a binary pattern, samurai-style switch-plate armor, industrial gunmetal finish."),

    ("breadboard_baby",
     f"{BASE}. Body is a white breadboard with colorful jumper wires plugged in forming a smiley pattern, LED eyes that glow, resistor arms with color-code bands, 9V battery backpack."),

    ("free_software_bird",
     f"{BASE}. Small mechanical bird-shaped robot with GNU wildebeest horns, wings made of fanned-out source code printouts, freedom bell around neck, open padlock on chest, silver and parchment tones."),

    ("rotary_phone_head",
     f"{BASE}. Head is a vintage rotary phone dial with finger holes as expression, curly cord connecting to body, body made of heavy black Bakelite, chrome accents, satisfying tactile heft."),

    ("calculator_watch",
     f"{BASE}. Body styled as a giant Casio calculator watch, tiny keypad on belly, LCD segment display face, brushed steel band wrapping around as arms, 80s digital precision meets cute."),

    ("wire_wrap_cocoon",
     f"{BASE}. Body wrapped in colorful wire-wrap connections like a cocoon, gold-plated pins poking out at joints, magnifying inspection window on chest revealing neat wire patterns inside, electronics craft."),

    ("trs80_nostalgia",
     f"{BASE}. Body shaped like a miniature TRS-80 with silver keyboard belly, tiny cassette deck on hip, chiclet keys as teeth, Radio Shack price tag dangling from arm, warm gray and silver."),

    ("pipe_wrench_transformer",
     f"{BASE}. Body that transforms from a standard pipe wrench into robot form, jaw as mouth, adjustment wheel on head, heavy chrome vanadium steel texture, oil-stained, industrial tool character."),

    ("patchwork_epoch",
     f"{BASE}. Body made of patchwork squares from each 70s-80s material: one panel copper, one walnut, one green PCB, one beige plastic, one corduroy, one denim, quilted together with solder seams."),

    ("micro_processor_gem",
     f"{BASE}. Body is a giant Intel 4004 microprocessor chip, gold pins as legs, die shot visible through transparent epoxy window showing microscopic circuits, ceramic white package, precious artifact energy."),

    ("dot_matrix_poet",
     f"{BASE}. Dot matrix printer body continuously printing a banner of text that curls around like a scarf, tractor-feed holes along edges, ink-stained face with pixelated dot-matrix expression, paper everywhere."),

    ("oscilloscope_dreamer",
     f"{BASE}. Head is a round oscilloscope screen showing a peaceful sine wave that forms a smile, body is the instrument chassis with knobs and BNC connectors, probe wires as arms, green phosphor glow."),

    ("garage_startup_mess",
     f"{BASE}. Sitting inside a tiny cardboard box garage, surrounded by scattered components and coffee cups, soldering iron in hand, pizza box shelf, bare Edison bulb overhead, passion-project chaos."),

    ("rubber_keypad_bounce",
     f"{BASE}. Body made of squishy rubber membrane keypad material, dome-switch bumps all over creating a bubbly texture, translucent enough to see the PCB underneath, satisfying tactile squish energy."),

    ("magnetic_tape_mummy",
     f"{BASE}. Body wrapped in brown magnetic tape like a mummy, reel-to-reel spools on shoulders, tape slightly unwound and fluttering, data literally wearing its skin, warm oxide brown tones."),

    ("pocket_protector_nerd",
     f"{BASE}. Wearing an oversized white short-sleeve dress shirt with pocket protector full of tiny tools, thick horn-rim glasses, slide rule belt, pocket calculator in hand, endearing 70s engineer aesthetic."),

    ("unix_beard_sage",
     f"{BASE}. Brushed aluminum body with a flowing beard made of cascading terminal text in green, wise ancient eyes, tiny book of K&R C tucked under arm, sandal-wearing philosopher of code, serene."),

    ("cable_spaghetti_chef",
     f"{BASE}. Chef's hat on head, body tangled in a delightful mess of serial cables, parallel cables, and coax, wooden spoon in hand stirring a pot of cable spaghetti, apron stained with thermal paste."),

    ("slide_rule_elegant",
     f"{BASE}. Body is an elegant brass slide rule with logarithmic scales, cursor window as face, sliding center as articulated torso, bamboo and brass materials, mathematical precision meets warm craftsmanship."),

    ("crt_snow_static",
     f"{BASE}. Body is a small CRT television showing static snow, rabbit ear antenna on top, warm vacuum tube glow from back vents, channel knob on side, wood-grain cabinet base, cozy living room relic."),

    ("hacker_hoodie_shadow",
     f"{BASE}. Wearing an oversized dark hoodie with the hood up casting shadow over eyes except for two glowing green terminal-cursor eyes, hands emerging to type on an invisible keyboard, mysterious but friendly."),

    ("counter_culture_van",
     f"{BASE}. Body painted like a 70s VW van with peace signs and circuit diagrams mixed together, flower-power meets technology, tie-dye exhaust, daisy-chain network cables, commune-computing aesthetic."),
]

# =============================================================================
# ISSUE 5: "Link" — 1990s-2000s, The Connected World
# Era: World Wide Web, Linux, open source, dot-com, Google, Wikipedia
# =============================================================================
ISSUE_05_DESIGNS = [
    ("bondi_blue_translucent",
     f"{BASE}. Body made of translucent bondi blue plastic like the original iMac, visible internal components glowing warm orange through the shell, hockey-puck mouse as a pet on a leash, handle on top of head."),

    ("fiber_optic_rainbow_globe",
     f"{BASE}. Body wrapped in fiber optic cables that glow in shifting rainbow colors, head is a small glass globe with tiny light points representing connected cities, data pulses traveling through the fibers."),

    ("hyperlink_chain_knight",
     f"{BASE}. Wearing chain mail armor made of interconnected blue hyperlink chains, each link underlined, shield bearing the HTML anchor tag symbol, noble protector of the open web, chrome and blue."),

    ("dialup_modem_singer",
     f"{BASE}. Body is a chunky beige external modem with status lights as buttons on a vest, mouth open emitting visible sound waves representing the dialup handshake screech, musical notes made of data packets."),

    ("lcd_pixel_mosaic",
     f"{BASE}. Body made of visible LCD subpixels — red green blue stripes at macro scale creating a mosaic robot face when you step back, slight rainbow fringing at edges, digital pointillism aesthetic."),

    ("dot_com_neon_excess",
     f"{BASE}. Covered in garish dot-com era neon signs and flashing banner ads, dollar signs in eyes, riding a tiny rocket labeled 'IPO', gold chains made of stock ticker tape, peak 1999 irrational exuberance."),

    ("penguin_tuxedo_formal",
     f"{BASE}. Wearing a crisp black and white tuxedo styled after Tux the Linux penguin, bow tie is a tiny penguin, belly is white porcelain, flippers replaced with proper robot arms, dignified open-source formal wear."),

    ("ethernet_cable_dancer",
     f"{BASE}. Body woven from colorful Cat5 ethernet cables — blue body, orange arms, green legs, each cable terminating in RJ-45 crystal connectors at hands and feet, dynamic dancing pose, twisted pair energy."),

    ("search_bar_visor",
     f"{BASE}. Head features a Google-style search bar as a visor across the eyes, body made of white minimalist ceramic, single colorful button on chest, 'I'm Feeling Lucky' stamped on one foot, clean and powerful."),

    ("cd_rom_iridescent",
     f"{BASE}. Body is a stack of CD-ROMs creating an iridescent holographic shell, rainbow light refracting off the surface in prismatic patterns, jewel case wings, spiral data track visible, early internet artifact."),

    ("web_under_construction",
     f"{BASE}. Wearing a tiny hard hat, body surrounded by animated GIF-style construction barriers and spinning tools, 'Under Construction' yellow tape across chest, pixelated, nostalgic Web 1.0 charm."),

    ("server_rack_golem",
     f"{BASE}. Body is a miniature black server rack with blinking green LEDs in rows, hot-swap drive bays as pockets, cable management arms on back, cooling fan spinning on top, data center guardian."),

    ("browser_window_frame",
     f"{BASE}. Head framed by a classic Netscape browser window with gray title bar, navigation buttons as a crown, body is the webpage content area showing a loading progress bar at 73%, back button ears."),

    ("wiki_book_stack",
     f"{BASE}. Body is a stack of open books and encyclopedias with pages fanning out like wings, Wikipedia globe puzzle-ball head, tiny citation numbers floating around, knowledge radiating outward, warm paper tones."),

    ("holographic_disc_shield",
     f"{BASE}. Carrying a holographic disc as a captain's shield, body made of brushed titanium like a PowerBook G4, rainbow hologram reflections dancing across surfaces, sleek and futuristic 2001 aesthetic."),

    ("mouse_puck_racer",
     f"{BASE}. Body shaped like the infamous round Apple USB mouse, translucent with visible green PCB inside, single button face, USB cable tail, racing stripes, aerodynamic but intentionally awkward design."),

    ("web_safe_palette",
     f"{BASE}. Body is a grid of the 216 web-safe colors arranged as tiny tiles, each tile a different hue creating a mosaic pattern, head is the classic color picker circle, digital stained glass effect."),

    ("open_source_patchwork",
     f"{BASE}. Body covered in colorful patches like a well-traveled backpack, each patch a different open source project logo (stylized), held together with visible stitching, community quilt aesthetic, warm and loved."),

    ("dot_com_bubble_soap",
     f"{BASE}. Body is a giant iridescent soap bubble with a tiny robot inside, rainbow surface tension, cracks starting to form, dollar bills and stock certificates floating inside, beautiful but fragile, about to pop."),

    ("modem_handshake_duo",
     f"{BASE}. Two tiny robots facing each other reaching out to shake hands, one beige modem-bodied, one server-rack-bodied, connection sparks between their fingers, the internet handshake made physical."),

    ("blue_link_trail",
     f"{BASE}. Body made of stacked blue hyperlinks that have been visited (some turned purple), leaving a trail of breadcrumb links behind as it walks, cursor-pointer hand, the act of browsing made physical."),

    ("translucent_grape",
     f"{BASE}. Body is translucent grape-purple iMac plastic, Bondi-era curves, visible tangerine-orange circuit boards inside, five candy-colored siblings visible in background (blurred), the flavor lineup."),

    ("geocities_collage",
     f"{BASE}. Body is a chaotic collage of GeoCities aesthetic: starfield background texture, spinning email GIF, visitor counter on belly, flame divider belt, comic sans expression, glorious 90s web maximalism."),

    ("wifi_signal_halo",
     f"{BASE}. Minimal white ceramic body with concentric WiFi signal arcs emanating from head like a halo, each arc a different soft color fading outward, floating slightly, wireless ethereal presence."),

    ("netscape_navigator",
     f"{BASE}. Body styled as the Netscape Navigator ship's wheel logo, spokes as limbs, compass rose on chest, wearing a tiny captain's hat, sailing across a sea of blue hypertext, explorer spirit."),

    ("y2k_glitch_panic",
     f"{BASE}. Body glitching between two states — stable robot and scrambled pixel mess, clock on chest stuck at 11:59 PM 1999, sparks and error codes floating around, anxious but ultimately fine."),

    ("google_primary_blocks",
     f"{BASE}. Body assembled from four oversized building blocks in Google primary colors — blue, red, yellow, green — simple and playful, childlike construction, clean white joints, deceptively powerful simplicity."),

    ("optical_mouse_glow",
     f"{BASE}. Body shaped like an optical mouse with red LED glowing underneath, scroll wheel mohawk, two-button face, ergonomic curves, matte black rubber grip sides, precision sensor eye on belly."),

    ("napster_headphones",
     f"{BASE}. Wearing oversized headphones with musical notes leaking out as tiny file icons, body made of stacked jewel cases, cat-face logo tag on shirt, rebellious but cute, early file-sharing era energy."),

    ("html_tag_skeleton",
     f"{BASE}. Body structure is visible HTML tags — head tag for head, body tag for torso, div tags for limbs, styled with inline CSS colors, angle brackets as bones, the source code made physical, developer humor."),

    ("loading_spinner_zen",
     f"{BASE}. Body is a circular loading spinner frozen mid-rotation, gradient segments from gray to blue, perfectly patient expression, surrounded by floating buffering dots, the eternal wait made serene, dial-up patience."),

    ("aol_mail_herald",
     f"{BASE}. Dressed as a tiny mail carrier herald with trumpet, body is a yellow AOL running man silhouette turned robot, 'You've Got Mail' speech bubble, carrying a bulging mailbag of email envelopes, cheerful announcer."),

    ("linux_compile_forge",
     f"{BASE}. Standing at a tiny blacksmith's forge, hammering source code into compiled binaries on an anvil, sparks flying as bits, kernel source printout apron, penguin-shaped forge bellows, open source craftsman."),

    ("portal_site_doorway",
     f"{BASE}. Body is a miniature doorway/portal frame, through which a tiny internet landscape is visible (miniature websites, floating links), standing as a gateway, Yahoo-purple trim, portal to everywhere."),

    ("java_coffee_steam",
     f"{BASE}. Body is a coffee cup with the Java logo, steaming hot, brown ceramic glaze, handle as one arm, coffee bean buttons, steam forming into code snippets above, cozy but enterprise-serious dual nature."),

    ("silicon_valley_gold",
     f"{BASE}. Body made of actual silicon wafer material with iridescent circuit patterns, gold bonding wires as jewelry, standing on a tiny map of the San Francisco Bay Area, tech royalty, venture-capital glow."),

    ("flash_animation_bounce",
     f"{BASE}. Body is a bouncy Flash animation character with visible frame-by-frame motion blur, exaggerated squash-and-stretch proportions, vector-art clean lines, timeline ruler belt, Macromedia-era web cartoon."),

    ("rss_feed_antenna",
     f"{BASE}. Body is a warm orange cube with the RSS broadcast icon on chest, radio wave antenna on head pulsing with updates, newspaper-roll arms delivering fresh content, information syndication personified."),

    ("ebay_auction_gavel",
     f"{BASE}. Holding a tiny gavel, body decorated like a listing page with star ratings on chest, countdown timer on forehead, 'BID NOW' button as nose, surrounded by floating miniature auction items, marketplace energy."),

    ("matrix_rain_cloak",
     f"{BASE}. Wearing a long black cloak with green Matrix-style falling code characters cascading down the fabric, dark sunglasses reflecting code, black leather body, mysterious but the cute round shape undercuts the edge."),

    ("bluetooth_viking",
     f"{BASE}. Wearing a tiny Viking helmet with Bluetooth rune on the front, Nordic knotwork patterns in blue on body, wireless signal waves as a cape, Harald Bluetooth's legacy meets wireless tech, frost and chrome."),

    ("wikipedia_puzzle_globe",
     f"{BASE}. Body is an incomplete jigsaw puzzle sphere with pieces still floating into place, each piece has a different alphabet character, warm white glow from the knowledge inside, collaborative and ever-growing."),

    ("imessage_bubble_plush",
     f"{BASE}. Body shaped like a chat message bubble — blue on one side, green on the other, typing indicator dots as freckles, rounded soft plush texture, conversation made physical, friendly and communicative."),

    ("dial_up_patience",
     f"{BASE}. Sitting cross-legged in meditation pose, body is a telephone with modem sounds visualized as peaceful mandalas around it, progress bar at 2% across forehead, achieving inner peace while waiting to connect."),

    ("web_crawler_spider",
     f"{BASE}. Small mechanical spider-shaped robot with eight delicate chrome legs, magnifying glass as one eye for inspecting web pages, trailing a silk thread of indexed URLs behind it, friendly librarian spider energy."),

    ("mp3_player_retro",
     f"{BASE}. Body is a chunky first-gen MP3 player with tiny LCD screen face showing a waveform smile, single headphone jack port as belly button, 32MB memory badge on chest, chrome click wheel, digital music pioneer."),

    ("popup_ad_gremlin",
     f"{BASE}. Mischievous expression, body is a browser popup window with fake X button, 'CONGRATULATIONS YOU WON' text on belly, flashing borders, tiny but incredibly annoying and somehow endearing, web pest turned mascot."),

    ("broadband_highway",
     f"{BASE}. Body is a miniature highway overpass with data cars zooming through, DSL modem as a toll booth hat, fiber optic road surface glowing, upgrade from dial-up represented as infrastructure, speed and progress."),

    ("open_source_garden",
     f"{BASE}. Body is a tiny terracotta pot with a circuit-board plant growing out of it, branches forking like git branches, leaves are pull request icons, roots visible through glass showing shared code, collaborative growth."),

    ("dotcom_crash_phoenix",
     f"{BASE}. Half the body is charred server wreckage from the crash, the other half is fresh new growth — green shoots of Web 2.0, butterfly wings made of surviving startups' logos, rebirth from the ashes, hopeful."),
]

# =============================================================================
# ISSUE 6: "Neuron" — 2000s-2015, Machines That Learn
# Era: Neural networks, deep learning, ImageNet, GPUs, backpropagation
# =============================================================================
ISSUE_06_DESIGNS = [
    ("bioluminescent_neural",
     f"{BASE}. Body made of translucent bioluminescent neural tissue, glowing blue-green synaptic connections pulsing beneath the surface, dendrite arms branching outward, warm axon glow at core, deep sea creature meets AI."),

    ("gpu_silicon_green",
     f"{BASE}. Body is a massive GPU chip with thousands of tiny CUDA cores visible as a grid of green lights, heat sink fins as a mohawk, PCIe gold finger connector feet, NVIDIA green glow, parallel processing power."),

    ("gradient_descent_skier",
     f"{BASE}. Standing on a mathematical surface (loss landscape), ski poles in hands, carving a path downhill toward the global minimum marked with a flag, contour lines visible on the terrain, optimization as sport."),

    ("imagenet_mosaic_skin",
     f"{BASE}. Body surface is a mosaic of thousands of tiny ImageNet classification images — cats, dogs, cars, birds — all blending together, each tile perfectly labeled, the dataset made flesh, pattern recognition embodied."),

    ("backprop_flow_rivers",
     f"{BASE}. Body is transparent showing internal rivers of gradient flow — red forward pass flowing head to toe, blue backward pass flowing toe to head, mathematical symbols swimming in the currents, learning made visible."),

    ("lab_coat_porcelain",
     f"{BASE}. Body is smooth white porcelain like fine laboratory equipment, wearing a miniature lab coat with 'Deep Learning Lab' badge, holding a pipette filled with training data droplets, clinical precision meets warmth."),

    ("tensorflow_orange_flame",
     f"{BASE}. Body engulfed in warm TensorFlow orange flames that don't burn, computational graph structure visible within the fire, tensor arrows flowing through, framework mascot energy, mathematical fire spirit."),

    ("pytorch_red_forge",
     f"{BASE}. Body is a red-hot forge with PyTorch dynamic computation happening in real-time, sparks as gradient updates, anvil-shaped base, torch (literal) held aloft, artisan approach to AI, hot metal and code."),

    ("crystal_lattice_mind",
     f"{BASE}. Body is a crystalline lattice structure where each node is a tiny neuron, light refracting through the geometric crystal creating rainbow caustics, weight connections as crystal bonds, mineral intelligence."),

    ("weight_matrix_abacus",
     f"{BASE}. Body is a three-dimensional abacus with beads representing neural network weights, some beads glowing hot (high activation), others dark (zeroed out), wooden frame meets mathematical precision, analog computing ancestor."),

    ("synaptic_plasma_orb",
     f"{BASE}. Body is a floating plasma ball with purple-pink electrical arcs jumping between internal nodes, each arc a synaptic connection firing, glass sphere body, touching the surface makes arcs follow, reactive and alive."),

    ("ai_winter_snowman",
     f"{BASE}. Body is a melting snowman — the AI winter thawing — with spring flowers pushing through the slush, scarf made of rejected grant proposals, carrot nose replaced by a tiny GPU, hope in the thaw."),

    ("three_godfathers_tribute",
     f"{BASE}. Body made of three intertwined metals — Hinton-gold, LeCun-silver, Bengio-bronze — braided together, each metal contributing structural patterns (convolutions, Boltzmann, attention), persistence embodied."),

    ("loss_curve_rollercoaster",
     f"{BASE}. Riding a tiny rollercoaster track shaped like a loss curve — steep initial drop, oscillations, eventual convergence to flat minimum, hands raised in excitement, training progress as thrill ride."),

    ("feature_visualization_dream",
     f"{BASE}. Body surface covered in DeepDream-style feature visualizations — swirling eyes, fractal patterns, dog faces emerging from noise, psychedelic but structured, what neural networks see when they dream."),

    ("classification_label_tags",
     f"{BASE}. Body covered in floating classification labels and confidence percentages — 'robot: 97.3%', 'cute: 99.1%', 'round: 94.8%' — each tag with a colored confidence bar, self-aware AI humor."),

    ("neuron_terrarium",
     f"{BASE}. Body is a glass terrarium containing a living neural network garden — dendrites as ferns, axons as vines, synapses as tiny flowers that light up when signals pass, biological meets computational, self-contained ecosystem."),

    ("perceptron_ancestor",
     f"{BASE}. Ancient-looking robot made of brass and vacuum tubes, single-layer perceptron architecture visible, binary weights as physical toggle switches, 1958 date stamp, honored ancestor of deep learning, dignified elder."),

    ("convolution_filter_eye",
     f"{BASE}. Giant magnifying glass eye that shows different convolutional filters — edge detection, blur, sharpen — each filter overlaid creates a different view of the world, seeing in feature maps, multi-layered perception."),

    ("training_data_feast",
     f"{BASE}. Sitting at a tiny banquet table overflowing with data — image plates, text scrolls, audio waveform drinks — voraciously consuming everything, napkin tucked in, insatiable appetite for information, data glutton."),

    ("dropout_mask_mystery",
     f"{BASE}. Parts of the body randomly faded to transparent (dropout regularization), different parts vanishing and reappearing, mask-like face with some features missing, prevents overfitting by being intentionally incomplete."),

    ("epoch_counter_monk",
     f"{BASE}. Zen Buddhist monk appearance, meditation beads where each bead is a training epoch counter incrementing, serene expression deepening with each epoch, loss function mandala on floor, patience of training embodied."),

    ("relu_activation_bolt",
     f"{BASE}. Body has a sharp angular ReLU function shape — flat on the left (zero), angled upward on the right, lightning bolt crack where the function activates, electrical energy on the positive side, dead calm on negative."),

    ("vanishing_gradient_ghost",
     f"{BASE}. Body gradually fading from solid at the output layer (head) to nearly invisible at the input layer (feet), the vanishing gradient problem visualized, ghostly transparent lower half, frustrated expression."),

    ("batch_normalization_spa",
     f"{BASE}. Relaxing in a tiny spa bath, body being normalized — stretched and squeezed to perfect mean-zero unit-variance proportions, statistical charts as bath bubbles, zen normalization treatment, balanced and centered."),

    ("gpu_farm_rancher",
     f"{BASE}. Wearing a cowboy hat, standing before a miniature ranch of GPU server racks arranged like cattle in pens, lasso made of ethernet cables, wrangling compute, silicon rancher of the deep learning frontier."),

    ("attention_spotlight",
     f"{BASE}. Body holding multiple spotlights that illuminate different parts of a sentence floating in air, brighter lights on important words, dimmer on filler, attention mechanism as theatrical lighting, focus made visible."),

    ("overfitting_mirror",
     f"{BASE}. Looking at itself in a mirror, the reflection is a PERFECT memorized copy of training data instead of a generalized robot, narcissistic overfitting, the mirror shows too-specific details, cautionary tale."),

    ("research_paper_origami",
     f"{BASE}. Body folded from arxiv research papers, mathematical equations visible on the white paper surface, precise origami folds along proof lines, bibliography as texture, academic knowledge given physical form."),

    ("sigmoid_squish",
     f"{BASE}. Body shaped like a sigmoid curve — squished flat at extremes, steep in the middle, smooth and continuous, soft rubber-like material that springs back when poked, the classic activation function as a being."),

    ("confusion_matrix_quilt",
     f"{BASE}. Body wrapped in a quilt where each square is a confusion matrix cell — true positives in warm green, false positives in cool red, diagonal of correctness glowing, statistical comfort blanket, ML evaluation metric."),

    ("embedding_space_float",
     f"{BASE}. Floating in a high-dimensional embedding space visualized as a starfield, similar concepts clustered nearby as glowing constellations, body positioned at the intersection of 'robot' and 'cute' clusters."),

    ("data_augmentation_clone",
     f"{BASE}. Surrounded by slightly altered copies of itself — one flipped, one rotated, one color-shifted, one cropped — data augmentation creating training variety from one sample, hall of mirrors with intentional distortions."),

    ("minibatch_lunch_tray",
     f"{BASE}. Carrying a cafeteria lunch tray with exactly 32 tiny data samples arranged in a grid (minibatch), some images some text, walking to the training table, stochastic gradient descent as lunch routine."),

    ("deep_layers_nesting",
     f"{BASE}. Body is a Russian nesting doll (matryoshka) with each layer representing a deeper network layer, outermost layer shows raw pixels, innermost shows abstract features, depth of representation, layers of understanding."),

    ("cat_detector_hero",
     f"{BASE}. Wearing a superhero cape, holding up a photograph of a cat with 'CAT: 99.97%' confidence beam shooting from eyes, the iconic ImageNet moment, proud achievement of correctly classifying internet cats."),

    ("pooling_layer_compress",
     f"{BASE}. Body being squeezed through a max-pooling press — entering large and detailed on one side, emerging smaller but retaining the maximum features on the other, compression as character transformation, efficient."),

    ("softmax_probability_pie",
     f"{BASE}. Body is a pie chart showing softmax probability distribution — one dominant slice (the prediction) and many tiny uncertain slices, confidently leaning toward the largest slice, decision-making visualized."),

    ("cuda_core_army",
     f"{BASE}. Tiny robot standing atop a formation of thousands of even tinier identical CUDA core soldiers in perfect grid formation, general commanding parallel troops, massive parallelism as military organization, scale."),

    ("learning_rate_dial",
     f"{BASE}. Giant dial on chest labeled 'Learning Rate' going from 'too slow' through 'just right' to 'chaos', hand carefully adjusting it, the most important hyperparameter, delicate tuning of a critical control."),

    ("transfer_learning_hand",
     f"{BASE}. Receiving a glowing knowledge orb being handed over from a larger, more experienced robot (partially visible), pre-trained wisdom transferring through touch, mentorship and knowledge transfer visualized."),

    ("local_minima_trap",
     f"{BASE}. Stuck in a bowl-shaped valley (local minimum) looking up at the rim, can see the global minimum as a deeper valley in the distance, tiny ladder and climbing gear, optimization frustration, determined to escape."),

    ("tensor_cube_juggler",
     f"{BASE}. Juggling three-dimensional tensor cubes of different sizes, each cube a different color representing different data dimensions, mathematical circus performer, balancing multidimensional data, computational acrobat."),

    ("ai_spring_bloom",
     f"{BASE}. Body is a tiny tree transitioning from bare winter branches (AI winter) to full spring bloom, cherry blossoms made of neural network diagrams, thawing ice revealing GPU circuits underneath, renaissance moment."),

    ("residual_skip_bridge",
     f"{BASE}. Body has a visible highway/bridge arching over the middle section — the skip connection — allowing gradient traffic to bypass layers, ResNet architecture as infrastructure, engineering solution to vanishing gradients."),

    ("gan_duality_split",
     f"{BASE}. Body split down the middle — left half is a generator creating art, right half is a discriminator with a detective magnifying glass, competing but cooperative, adversarial training as buddy-cop duo."),

    ("kaggle_medal_champion",
     f"{BASE}. Wearing a stack of Kaggle competition medals — gold, silver, bronze — on chest, leaderboard projection behind, holding a trophy shaped like a perfectly tuned model, competitive ML achievement, data science athlete."),

    ("regularization_bonsai",
     f"{BASE}. Body is a bonsai tree carefully pruned (regularized) to prevent overgrowth, tiny scissors in hand trimming excessive branches (parameters), the art of constraining complexity, disciplined beauty."),

    ("arxiv_scroll_scholar",
     f"{BASE}. Ancient scholar appearance with scroll made of arxiv paper printouts unfurling, mathematical proofs as ancient runes, reading glasses perched on nose, quill pen made of a stylus, timeless pursuit of knowledge."),

    ("hardware_lottery_dice",
     f"{BASE}. Rolling oversized dice where each face shows a different hardware accelerator — GPU, TPU, FPGA, CPU — standing on a roulette wheel of compute options, the hardware lottery that shaped which algorithms won."),
]
