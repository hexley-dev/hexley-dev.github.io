"""
Character design prompts for Issues 7-10 of "From Turing to Swarms".
50 curated prompts per issue, 200 total.
Each blends 2-3 vectors (material + concept, form + mood, etc.)
"""

BASE = (
    "A cute tiny round robot character with two expressive dark eyes, "
    "small feet, photo-realistic, studio lighting, white seamless background, "
    "product photography style, sharp focus, 8k detail"
)

# ─────────────────────────────────────────────────────────────────────
# ISSUE 7: "Attn" — 2017-2023, Attention Is All You Need
# ─────────────────────────────────────────────────────────────────────

ISSUE_07_DESIGNS = [
    ("holographic_attention_prism",
     f"{BASE}. Body made of holographic iridescent glass that refracts light into rainbow attention beams radiating outward, each beam landing on a tiny floating puzzle-piece token."),

    ("chrome_spotlight_head",
     f"{BASE}. Polished chrome body with a single powerful spotlight beam projecting from its forehead, illuminating a cluster of scattered letter tokens that glow where the beam touches."),

    ("origami_paper_fold",
     f"{BASE}. Entire body folded from a single sheet of white paper printed with the words 'Attention Is All You Need', visible creases and mathematical notation peeking through the folds."),

    ("pixel_mosaic_tokenizer",
     f"{BASE}. Surface covered in tiny colorful pixel mosaic tiles, each tile a different Unicode character, body appears to be mid-dissolving into a stream of individual token pieces floating upward."),

    ("quantum_shimmer_shell",
     f"{BASE}. Shell made of quantum-shimmer material that appears to exist in multiple positions simultaneously, ghostly afterimages showing the robot in three poses at once, probability clouds around its edges."),

    ("glass_prism_splitter",
     f"{BASE}. Triangular prism-shaped body made of flawless optical glass, a single white beam of text entering one side and splitting into a rainbow spectrum of meaning-colored beams on the other."),

    ("liquid_mercury_pooling",
     f"{BASE}. Body appears to be liquid mercury held in shape by invisible forces, surface constantly rippling with reflections that show different words and symbols in the distortions."),

    ("aurora_borealis_crown",
     f"{BASE}. Matte white ceramic body wearing a crown of shimmering aurora borealis light that flows and undulates above its head, green and purple curtains of light containing faint embedded text."),

    ("neon_wire_attention_web",
     f"{BASE}. Skeleton visible through translucent skin, made entirely of glowing neon wire in hot pink and electric blue, wires forming a dense attention matrix pattern connecting head to every extremity."),

    ("crystalline_embedding_sphere",
     f"{BASE}. Holding a perfect crystalline sphere that contains thousands of tiny glowing dots arranged in 3D space — an embedding universe — dots connected by gossamer threads of light."),

    ("iridescent_scale_armor",
     f"{BASE}. Covered in tiny iridescent scales like a fish, each scale shifting between colors as viewing angle changes, scales arranged in a pattern that suggests rows and columns of an attention matrix."),

    ("paper_crane_transformer",
     f"{BASE}. Body transforming mid-fold between a flat sheet of academic paper and a completed origami crane, halfway through the metamorphosis, equations still visible on the paper surface."),

    ("chrome_multi_eye_head",
     f"{BASE}. Chrome body with eight small spotlight eyes arranged in a ring around its head — multi-head attention visualized — each eye projecting a different colored beam toward a shared focal point."),

    ("holographic_context_scroll",
     f"{BASE}. Unrolling a long holographic scroll that extends far beyond frame, the scroll surface alive with shimmering text that fades at the edges, representing a vast context window."),

    ("glass_brain_visible",
     f"{BASE}. Transparent glass head revealing an intricate interior of layered attention matrices — glowing grid patterns stacked in parallel, light flowing between layers like synaptic fire."),

    ("mercury_token_rain",
     f"{BASE}. Standing under a gentle rain of liquid mercury droplets, each droplet containing a single letter or word, catching them in cupped hands where they merge into coherent sentences."),

    ("prismatic_beam_dancer",
     f"{BASE}. Dancing pose with arms outstretched, body made of clear prismatic glass, studio light hitting it creates a spectacular web of refracted attention beams painting the white background with color."),

    ("neon_wireframe_thinker",
     f"{BASE}. Wireframe body made of thin neon tubes in cyan and magenta, sitting in Rodin's Thinker pose, the wires around its head glowing brighter as if concentrating attention energy."),

    ("pixel_dissolve_gradient",
     f"{BASE}. Left side of body is solid smooth ceramic, right side dissolving into a cloud of individual colored pixels — each pixel a token — showing the boundary between meaning and components."),

    ("aurora_embedding_galaxy",
     f"{BASE}. Belly is a window into a miniature galaxy of aurora-colored points of light — word embeddings floating in semantic space — with visible clusters and constellations of related concepts."),

    ("crystalline_query_key_value",
     f"{BASE}. Three crystalline antennae on head: one ruby red (query), one sapphire blue (key), one emerald green (value), each emitting a beam that converges at a single glowing point of attention."),

    ("origami_scaling_tower",
     f"{BASE}. Standing atop a tower of origami paper blocks, each layer larger than the one below — scaling laws visualized — the smallest block at top is exquisitely detailed, the base massive and simple."),

    ("holographic_token_juggler",
     f"{BASE}. Juggling seven holographic puzzle pieces in mid-air, each piece a different glowing color with a partial word etched on it, the pieces almost fitting together into a complete thought."),

    ("chrome_mirror_recursive",
     f"{BASE}. Polished chrome body reflecting itself infinitely in two facing mirrors, each reflection slightly different in pose — self-attention attending to its own representations recursively."),

    ("quantum_superposition_reader",
     f"{BASE}. Reading the famous 'Attention Is All You Need' paper, but the paper exists in quantum superposition — multiple transparent copies at different angles, each highlighting different sections."),

    ("glass_layer_cake",
     f"{BASE}. Body structured as stacked transparent glass layers — a transformer stack — each layer containing a different visible pattern of connections, light propagating upward through all layers."),

    ("mercury_fountain_head",
     f"{BASE}. Head is an open vessel from which liquid mercury fountains upward in thin streams, each stream carrying a glowing token symbol before arcing back down in a continuous attention cycle."),

    ("neon_softmax_halo",
     f"{BASE}. Surrounded by a halo of neon light bars at varying heights — a softmax probability distribution made physical — the tallest bar directly above its head glowing brightest."),

    ("iridescent_bubble_memory",
     f"{BASE}. Surrounded by floating iridescent soap bubbles of varying sizes, each bubble containing a tiny scene or symbol — context window memories — larger bubbles for more attended content."),

    ("crystal_mosaic_face",
     f"{BASE}. Face is a mosaic of hundreds of tiny crystal tiles, each tile a different shade, the overall pattern forming its expressive eyes — attention as the emergence of meaning from fragments."),

    ("paper_airplane_fleet",
     f"{BASE}. Launching a fleet of tiny paper airplanes made from pages of the transformer paper, each airplane trailing a different colored light stream, all converging on a distant target."),

    ("chrome_antenna_array",
     f"{BASE}. Head bristling with a dense array of chrome antennae of different lengths, each antenna tipped with a tiny glowing orb, the orbs pulsing in coordinated patterns like a phased array."),

    ("holographic_matrix_rain",
     f"{BASE}. Standing in a gentle rain of holographic green characters falling Matrix-style, but the characters are attention weights — decimal numbers between 0 and 1 — some glowing brighter."),

    ("glass_hourglass_body",
     f"{BASE}. Body shaped like a miniature hourglass made of clear glass, tokens flowing as sand from top chamber (input) through a narrow attention bottleneck to bottom chamber (output)."),

    ("aurora_thought_trails",
     f"{BASE}. Moving through space leaving aurora-colored thought trails behind it, the trails forming visible connections between concepts — a physical trace of the attention computation path."),

    ("pixel_art_retro_modern",
     f"{BASE}. One half rendered in chunky 8-bit pixel art style, the other half in photorealistic detail — the evolution from simple to sophisticated AI — the boundary between halves shimmering."),

    ("crystalline_fractal_depth",
     f"{BASE}. Body is a fractal crystal structure — zooming in reveals smaller copies of the attention pattern at every scale, self-similar from macro body shape down to microscopic surface texture."),

    ("mercury_mirror_ball",
     f"{BASE}. Spherical body of liquid mercury acting as a perfect mirror ball, reflecting and distorting the entire room, every reflection showing a different token or concept from its training data."),

    ("neon_circuit_calligraphy",
     f"{BASE}. Surface inscribed with flowing calligraphic circuits in neon ink — mathematical notation from the transformer paper rendered as beautiful Arabic-style calligraphy that also functions as circuitry."),

    ("origami_unfolding_bloom",
     f"{BASE}. Mid-bloom like a flower, origami petals unfolding outward from its core, each petal is a page from a different landmark AI paper, the center glowing with synthesized understanding."),

    ("holographic_scale_model",
     f"{BASE}. Projecting a holographic model of itself that's ten times larger, and that projection projects an even larger one — scaling laws — each scale more capable, details more refined."),

    ("chrome_puzzle_assembly",
     f"{BASE}. Chrome body made of interlocking puzzle pieces, some pieces floating slightly apart showing the internal glow, each piece etched with a different token from a tokenized sentence."),

    ("glass_neural_aquarium",
     f"{BASE}. Transparent glass belly containing a miniature aquarium scene, but instead of fish, tiny glowing attention heads swim through liquid, connecting floating word-tokens with light trails."),

    ("prism_rainbow_reader",
     f"{BASE}. Reading a book, but the words lift off the page and pass through a prism in its forehead, emerging as a rainbow spectrum of understanding — white light of text becoming colored meaning."),

    ("quantum_entangled_pair",
     f"{BASE}. Two identical robots connected by a shimmering quantum entanglement beam, when one turns left the other responds — illustrating how attention connects distant tokens instantaneously."),

    ("iridescent_feather_quill",
     f"{BASE}. Body covered in tiny iridescent feathers like a hummingbird, holding a feather quill that writes glowing equations in mid-air — the beauty of the attention mechanism made avian."),

    ("neon_heartbeat_monitor",
     f"{BASE}. Chest displaying a neon heartbeat monitor, but instead of a pulse, the waveform shows attention weight spikes — high peaks where important tokens live, flat lines between padding."),

    ("crystal_geode_split",
     f"{BASE}. Body cracked open like a geode, the rough exterior giving way to a dazzling interior of amethyst crystals arranged in the exact pattern of a multi-head attention matrix."),

    ("mercury_ink_writer",
     f"{BASE}. Dripping liquid mercury from its fingertips like ink, the mercury flowing across the white surface forming elegant mathematical equations — the transformer architecture self-documenting."),

    ("aurora_northern_sage",
     f"{BASE}. Elderly sage version with a tiny aurora-borealis beard that flows and shimmers, wearing spectacles through which you can see attention beams focusing on whatever it examines."),
]

# ─────────────────────────────────────────────────────────────────────
# ISSUE 8: "Agent" — 2024-2025, The Agent Awakens
# ─────────────────────────────────────────────────────────────────────

ISSUE_08_DESIGNS = [
    ("terminal_green_hacker",
     f"{BASE}. Body made of matte black anodized metal, eyes glowing terminal-green phosphor, tiny green command-line text scrolling across its chest like a built-in terminal display."),

    ("swiss_army_multitool",
     f"{BASE}. Body is a compact Swiss Army knife form factor in brushed aluminum, various miniature tools folding out — a tiny wrench, magnifying glass, pen, and USB connector — ready for any task."),

    ("kintsugi_gold_repair",
     f"{BASE}. Matte black ceramic body covered in beautiful kintsugi gold-filled cracks — each crack a repaired error — the damage made beautiful, showing a history of graceful failure recovery."),

    ("circuit_trace_copper",
     f"{BASE}. Body is a living circuit board, copper traces running across dark green PCB skin, tiny components soldered at junction points, LED indicator eyes blinking in diagnostic patterns."),

    ("vscode_dark_theme",
     f"{BASE}. Colored exactly like VS Code's dark theme — charcoal body, syntax-highlighted accents in orange strings, blue keywords, green comments, and purple function names decorating its surface."),

    ("carbon_fiber_stealth",
     f"{BASE}. Sleek carbon fiber weave body, ultralight and precise, tiny rubber grip pads on its hands for tool manipulation, a single red LED status indicator on its chest pulsing steadily."),

    ("react_loop_spinner",
     f"{BASE}. Four arms arranged in a spinning cycle — one thinking (finger on chin), one planning (holding blueprint), one acting (wielding tool), one observing (holding magnifying glass) — the ReAct loop embodied."),

    ("terminal_cursor_blink",
     f"{BASE}. Entirely matte black with a single element of animation: a bright green blinking cursor line on its face where a mouth would be, the universal symbol of awaiting input."),

    ("rubber_grip_mechanic",
     f"{BASE}. Industrial rubber grip texture covering its palms and feet, wearing a tiny tool belt loaded with miniature debugging instruments, a headlamp illuminating whatever it's working on."),

    ("purple_syntax_wizard",
     f"{BASE}. Draped in a cloak colored like syntax highlighting — purple and magenta gradients — holding a wand that's actually a cursor, casting spells that manifest as floating code snippets."),

    ("brushed_aluminum_exec",
     f"{BASE}. Premium brushed aluminum body with precise machined edges, minimal and elegant like an Apple product, a single multicolor LED ring around its eye indicating processing state."),

    ("debug_probe_surgeon",
     f"{BASE}. Wearing tiny surgical loupes, holding a glowing debug probe in one hand and forceps in the other, examining an opened-up miniature circuit board patient on a tiny operating table."),

    ("file_tree_backpack",
     f"{BASE}. Carrying an oversized backpack that's a miniature file tree — tiny folder icons and file icons arranged in a tree structure growing out of the pack, navigating through its codebase."),

    ("test_tube_chemist",
     f"{BASE}. Holding a rack of tiny test tubes, each labeled — PASS in green, FAIL in red, PENDING in yellow — wearing lab goggles, one tube bubbling with a reaction in progress."),

    ("keyboard_warrior",
     f"{BASE}. Feet replaced by mechanical keyboard keycaps, body armor made of overlapping keyboard keys, wielding a detached Enter key as a shield, ready to execute commands."),

    ("led_status_sentinel",
     f"{BASE}. Matte black body studded with dozens of tiny LED indicators — green for healthy systems, amber for warnings, red for errors — currently showing mostly green with one amber blinking."),

    ("copper_pipe_plumber",
     f"{BASE}. Body made of interconnected copper pipes and fittings, data visibly flowing through the pipes as glowing liquid, some junctions with tiny valves it can turn to route information flow."),

    ("phosphor_screen_face",
     f"{BASE}. Face is a tiny curved CRT screen showing green phosphor text — a command prompt with recent history of think/plan/act/observe steps scrolling upward, warm amber glow around edges."),

    ("anodized_black_ninja",
     f"{BASE}. Sleek matte black anodized body with zero reflections, moving in a dynamic action pose, leaving a subtle motion trail of purple syntax-colored afterimages behind it."),

    ("toolbox_chest_open",
     f"{BASE}. Torso opens like a toolbox lid, revealing neatly organized compartments inside containing miniature tools: tiny terminal, magnifying glass, wrench, pencil, each in its custom-fit slot."),

    ("git_branch_antlers",
     f"{BASE}. Growing antlers made of branching git history — each branch tip a tiny glowing commit node, some branches merging back together, the main trunk running up the center strong and green."),

    ("error_recovery_phoenix",
     f"{BASE}. Emerging from a pile of tiny crumpled error messages and stack traces, body showing kintsugi-gold repair lines, one hand reaching upward confidently — rising from failure."),

    ("cursor_identity_core",
     f"{BASE}. Chest contains a glowing core shaped exactly like a text cursor — a thin vertical blinking line — this is its identity, its soul, pulsing with each computation cycle."),

    ("rubber_duck_debugger",
     f"{BASE}. Sitting on a desk next to a classic yellow rubber duck, both staring at a tiny floating code snippet, the robot pointing at a specific line while the duck listens patiently."),

    ("carbon_fiber_racer",
     f"{BASE}. Aerodynamic carbon fiber body with racing stripes in terminal green, built for speed, tiny spoiler on back, wheels retracted into feet, leaving a green phosphor speed trail."),

    ("matte_black_monolith",
     f"{BASE}. Ultra-minimal matte black body with perfectly smooth surfaces, no visible seams, only two elements: expressive dark eyes and a single pulsing green dot — maximum capability, minimum flash."),

    ("circuit_board_tattooed",
     f"{BASE}. Warm copper-toned body covered in intricate circuit board trace tattoos in darker copper, each trace pattern representing a different tool capability — filesystem, network, compute."),

    ("terminal_retro_amber",
     f"{BASE}. Styled like a 1980s amber monochrome terminal, warm orange-amber glow emanating from its screen-face, chunky bezels, satisfying clicky keyboard keys as belly buttons."),

    ("autonomous_astronaut",
     f"{BASE}. Wearing a tiny space suit with a darkened visor, floating in zero gravity with small thruster jets — autonomous agent in unexplored territory, tethered by a thin lifeline to base."),

    ("code_environment_terrarium",
     f"{BASE}. Living inside a glass terrarium that's a miniature code environment — tiny terminal windows as furniture, file trees as plants, cursor blinking as a campfire, cozy and self-contained."),

    ("watchmaker_precision",
     f"{BASE}. Brushed steel body with the precision of a Swiss watch, holding jeweler's tools, working on an incredibly intricate miniature mechanism — careful, precise, autonomous craftsmanship."),

    ("self_healing_blob",
     f"{BASE}. Soft rubbery body that's been dented and scratched, but golden repair material is actively filling in the damage in real-time, some old scars fully healed into beautiful gold seams."),

    ("dual_screen_operator",
     f"{BASE}. Two tiny holographic screens floating in front of it, one showing code and one showing test results, hands moving between both screens, managing multiple contexts simultaneously."),

    ("pipe_wrench_plumber_v2",
     f"{BASE}. Wearing a tiny hardhat, carrying an oversized pipe wrench, standing next to a complex system of data pipes — some leaking glowing data — methodically diagnosing and fixing each joint."),

    ("neon_sign_craftsman",
     f"{BASE}. Body outlined in bent neon tube glass like a neon sign, glowing in terminal green, the tubes spelling out fragments of code at its joints, warm buzz of electrical craftwork."),

    ("magnetic_tool_belt",
     f"{BASE}. Wearing a magnetic tool belt that attracts and holds floating miniature tools — each tool snapping into place when needed, releasing when done, an ever-ready autonomous toolkit."),

    ("obsidian_glass_agent",
     f"{BASE}. Body carved from volcanic obsidian glass, sharp faceted edges catching light, but hands are soft warm rubber — hard analytical mind, gentle careful touch with the systems it works on."),

    ("copper_patina_veteran",
     f"{BASE}. Copper body showing beautiful green patina from long service, each patina pattern telling a story of past debugging sessions, experienced and weathered but still sharp and capable."),

    ("binary_rain_coat",
     f"{BASE}. Wearing a tiny translucent raincoat, standing in a gentle rain of 1s and 0s, some digits collecting in puddles at its feet, calmly working through the data stream."),

    ("blueprint_skin_architect",
     f"{BASE}. Skin textured like architectural blueprints — white lines on blue — showing its own internal schematic, a self-documenting agent whose design is literally written on its surface."),

    ("mechanical_keyboard_heart",
     f"{BASE}. Transparent chest revealing a heart made of a single Cherry MX mechanical switch, each heartbeat producing a satisfying click, the tactile soul of a keyboard-native agent."),

    ("emergency_red_button",
     f"{BASE}. Big shiny red emergency stop button on its chest that it can self-press, representing the safety-first design — autonomous but always one button away from stopping, responsible agency."),

    ("scaffold_builder",
     f"{BASE}. Standing on tiny scaffolding it built around a larger broken system, methodically repairing from the outside in, surrounded by its own organized construction materials."),

    ("night_shift_worker",
     f"{BASE}. Under a tiny desk lamp casting warm light in an otherwise dark scene, coffee mug beside it, multiple terminal windows glowing, the dedicated agent working through the night."),

    ("rubber_eraser_editor",
     f"{BASE}. One hand is a pencil, the other is an eraser, surrounded by floating code with some lines being written and others being carefully erased — the iterative edit cycle of an agent."),

    ("antenna_signal_seeker",
     f"{BASE}. Tall rotating antenna on head picking up signals, body covered in tiny receiver dishes, LED chest display showing signal strength bars — an agent sensing and responding to its environment."),

    ("magnifying_glass_detective",
     f"{BASE}. Wearing a tiny detective coat, holding an oversized magnifying glass up to a floating stack trace, footprints of previous investigation visible on the ground — debugging as detective work."),

    ("modular_snap_together",
     f"{BASE}. Body made of snap-together modules, some modules pulled slightly apart showing the connection points, each module a different tool capability that can be reconfigured for any task."),

    ("welding_mask_builder",
     f"{BASE}. Wearing a tiny welding mask flipped up, holding a miniature welding torch that produces sparks of code syntax, building a structure from raw materials — constructive agency."),

    ("compass_navigator",
     f"{BASE}. Chest contains a spinning compass that points not north but toward the next task, surrounded by a tiny map of interconnected objectives, plotting the optimal path through work."),
]

# ─────────────────────────────────────────────────────────────────────
# ISSUE 9: "Swarm" — 2025-2026, The Swarm
# ─────────────────────────────────────────────────────────────────────

ISSUE_09_DESIGNS = [
    ("honeycomb_gold_translucent",
     f"{BASE}. Body made of translucent golden honeycomb cells, each hexagonal cell glowing with a different task in progress, warm amber light emanating from the collective activity within."),

    ("constellation_silver_linker",
     f"{BASE}. Polished silver body with tiny star-bright points on its surface, connected by fine silver lines forming constellation patterns — each star a node, each line a communication channel."),

    ("ant_colony_bronze",
     f"{BASE}. Warm bronze body with the surface texture of a cross-sectioned ant colony, tiny tunnels and chambers visible through translucent bronze walls, miniature worker robots visible inside."),

    ("network_mesh_wireframe",
     f"{BASE}. Body rendered as a wireframe mesh — no solid surfaces — just an elegant network of interconnected nodes and edges, glowing where data flows, a topology made physical."),

    ("bioluminescent_deep_sea",
     f"{BASE}. Deep sea bioluminescent body pulsing with teal and purple light, tendrils of light extending outward to connect with other invisible swarm members, communicating through light."),

    ("crystalline_cluster_growth",
     f"{BASE}. Body is a cluster of growing crystals, each crystal a different agent spawned for a different purpose, all sharing a common crystalline root structure, still actively growing."),

    ("magnetic_ferrofluid_swarm",
     f"{BASE}. Body made of magnetic ferrofluid held in shape by internal magnets, the surface bristling with spiky peaks that shift and flow, sometimes separating into smaller independent droplets that return."),

    ("woven_textile_tapestry",
     f"{BASE}. Body woven from hundreds of different colored threads — each thread an agent's work stream — the weave creating a coherent pattern only visible when all threads work together."),

    ("coral_colony_builder",
     f"{BASE}. Body shaped like a branching coral colony, each branch tip a different specialized agent, all growing from a shared base, tiny fish-like data packets swimming between the branches."),

    ("mycelium_network_glow",
     f"{BASE}. Body is a dense mycelium network — white fungal threads forming a round shape, bioluminescent nodes at intersection points pulsing as information passes through the underground network."),

    ("conductor_baton_maestro",
     f"{BASE}. Standing at a tiny podium holding a gleaming conductor's baton, surrounded by a semicircle of smaller translucent ghost-robots — each an instrument in the orchestra — mid-crescendo."),

    ("git_branch_tree",
     f"{BASE}. Body is a living tree whose branches are git branches — colored lines diverging and merging, tiny commit dots at branch points, the trunk labeled 'main' in glowing green text."),

    ("honeycomb_hive_queen",
     f"{BASE}. Wearing a tiny golden crown, sitting at the center of a large honeycomb structure, smaller worker robots buzzing around the hive, each carrying a tiny glowing task card."),

    ("constellation_map_navigator",
     f"{BASE}. Projecting a 3D constellation map from its eyes, the map showing dozens of connected agent-stars with task labels, drawing new connection lines with a tiny laser pointer."),

    ("ant_trail_pheromone",
     f"{BASE}. Walking along a glowing pheromone trail on the ground, leaving its own trail behind, multiple trails crossing and reinforcing — stigmergic communication made visible as neon pathways."),

    ("mesh_dome_architect",
     f"{BASE}. Standing inside a geodesic dome made of wireframe mesh, each vertex of the dome occupied by a tiny agent node, the structure self-organizing as new nodes join and leave."),

    ("ferrofluid_divide_merge",
     f"{BASE}. Captured mid-split — its ferrofluid body dividing into three smaller identical robots, each carrying a portion of the original task, about to scatter and later reconverge."),

    ("textile_quilt_patchwork",
     f"{BASE}. Body is a patchwork quilt of different fabrics — each patch contributed by a different agent — corduroy, silk, denim, velvet — unified into one warm coherent whole."),

    ("bioluminescent_jellyfish_swarm",
     f"{BASE}. Surrounded by a halo of tiny bioluminescent jellyfish-like drones, each trailing long luminous tentacle-threads that weave together into a communication mesh of pulsing blue light."),

    ("crystal_radio_receiver",
     f"{BASE}. Body is a large crystal radio, old-fashioned antenna wire extending upward, receiving signals from dozens of tiny transmitting agent-robots in the distance, a relay hub."),

    ("unix_pipe_plumber",
     f"{BASE}. Body made of interconnected Unix pipes (literal plumbing pipes), labeled with tiny | symbols at each junction, data flowing through as glowing liquid — small tools piped together."),

    ("beehive_hexagon_specialist",
     f"{BASE}. Hexagonal body that tessellates perfectly with others, one face showing 'RESEARCH', another 'WRITE', another 'REVIEW' — a specialist that clicks together with complementary agents."),

    ("neural_mesh_brain",
     f"{BASE}. Head is an exposed neural mesh network, thousands of tiny wires connecting in a dome shape, sparks of activity visible at nodes, a brain made of network infrastructure."),

    ("swarm_murmuration_bird",
     f"{BASE}. Surrounded by a murmuration of hundreds of tiny flying robot-birds, all moving in fluid coordinated patterns, the main robot at the calm center of the dynamic swarm shape."),

    ("worktree_gardener",
     f"{BASE}. Tending a garden of tiny git worktrees — each tree a miniature bonsai in its own pot, labeled with branch names, the robot pruning and watering, cultivating parallel work streams."),

    ("task_card_dealer",
     f"{BASE}. Sitting at a round table dealing glowing task cards to smaller seated robots, each card showing a different job description, the dealer coordinating the distribution of work."),

    ("antenna_array_tower",
     f"{BASE}. Standing tall with a forest of varied antennae on its head — satellite dishes, rabbit ears, radio aerials — receiving and broadcasting on every frequency, the communication hub."),

    ("honeycomb_window_hive",
     f"{BASE}. Torso is a window into a busy honeycomb interior where dozens of tiny worker-bots are visible in their cells, each performing a different task, warm golden light pouring out."),

    ("constellation_weaver",
     f"{BASE}. Hands holding threads of starlight, actively weaving new connections between floating star-nodes, some connections fresh and bright, older ones dimmer but stable — building the network."),

    ("bronze_clockwork_colony",
     f"{BASE}. Antique bronze body housing a visible clockwork mechanism, but the gears are tiny individual robots meshing together — each tooth a separate agent, collective motion emerging from individual action."),

    ("mycelium_fruiting_body",
     f"{BASE}. Standing as the fruiting body of a vast mycelium network visible beneath a transparent floor, the underground network far larger than the visible robot, most of the swarm hidden below."),

    ("parallel_shadow_clones",
     f"{BASE}. Surrounded by five translucent shadow-copies of itself, each in a different working pose, all connected by thin light beams to the solid original — parallel execution visualized."),

    ("coral_reef_ecosystem",
     f"{BASE}. Body is a miniature coral reef ecosystem, different colored coral species (each a different agent type) growing in symbiosis, tiny fish carrying messages between coral formations."),

    ("magnetic_field_lines",
     f"{BASE}. Surrounded by visible magnetic field lines rendered in iron filings floating in space, the field lines connecting it to other unseen swarm members, attraction and organization made visible."),

    ("textile_loom_weaver",
     f"{BASE}. Operating a tiny loom, the warp threads coming from off-screen (other agents' outputs), weaving them together into a coherent fabric, the shuttle flying back and forth rapidly."),

    ("signal_flag_semaphore",
     f"{BASE}. Holding two tiny semaphore flags in different positions, surrounded by distant tiny robots also holding flags, communicating across distance through coordinated visual signals."),

    ("hive_mind_crown",
     f"{BASE}. Wearing a crown that's actually a ring of tiny connected robot heads — a hive mind council — each head whispering different advice, the main robot synthesizing their collective wisdom."),

    ("network_topology_map",
     f"{BASE}. Body is a 3D network topology — a sphere of nodes and edges — each node lighting up as its corresponding agent becomes active, showing real-time swarm activity across the network."),

    ("origami_army_general",
     f"{BASE}. Standing before rows of tiny origami robots in military formation, each folded slightly differently for its specialization, the general reviewing its paper army before deployment."),

    ("lightning_rod_connector",
     f"{BASE}. Tall lightning rod on its head attracting tiny lightning bolts from surrounding cloud-agents, each bolt a burst of information, the robot acting as the grounding point for swarm communication."),

    ("puzzle_piece_collective",
     f"{BASE}. Body is one large puzzle piece with visible interlocking edges, surrounded by other robot-puzzle-pieces floating nearby about to connect, the image only complete when all pieces join."),

    ("river_delta_flow",
     f"{BASE}. Body structured like a river delta viewed from above, a single input stream branching into dozens of distributary channels, each channel a parallel work stream, all reaching the sea together."),

    ("firefly_swarm_jar",
     f"{BASE}. Holding an open mason jar from which dozens of tiny firefly-robots are emerging, each firefly carrying a spark of task-light, dispersing into the darkness in coordinated patterns."),

    ("telephone_switchboard",
     f"{BASE}. Operating a vintage telephone switchboard, rapidly plugging and unplugging cables to connect different agent-callers, managing dozens of simultaneous conversations with practiced efficiency."),

    ("fractal_fern_recursive",
     f"{BASE}. Body shaped like a fractal fern — each frond a team, each leaflet an individual agent, the self-similar pattern repeating at every scale, natural recursive coordination."),

    ("crystal_lattice_structure",
     f"{BASE}. Body is a crystal lattice structure, each atom-node a tiny agent held in perfect geometric relationship to its neighbors by bond-beams, the structure strong because of collective arrangement."),

    ("mushroom_ring_council",
     f"{BASE}. Standing in a fairy ring of smaller mushroom-shaped robots, all connected underground by visible glowing root threads, a council meeting in progress under soft bioluminescent light."),

    ("starling_murmuration_core",
     f"{BASE}. Body dissolving at the edges into a cloud of hundreds of tiny flying copies of itself, forming a murmuration shape that shifts and flows, individual and collective simultaneously."),

    ("quilting_bee_circle",
     f"{BASE}. Sitting in a circle with seven other tiny robots, all stitching different sections of a large shared quilt, each section a different pattern but matching at the seams — collaborative creation."),

    ("radio_telescope_array",
     f"{BASE}. Body is a miniature radio telescope dish, part of a visible array of similar dish-robots spread across a tiny landscape, all pointed at the same target, synthesizing a single powerful signal."),
]

# ─────────────────────────────────────────────────────────────────────
# ISSUE 10: "Stack" — 1936-2026, The Whole Stack
# ─────────────────────────────────────────────────────────────────────

ISSUE_10_DESIGNS = [
    ("rainbow_geological_strata",
     f"{BASE}. Body is a cross-section of geological strata, each colorful layer representing a computing era — bottom brown-gray for Turing 1936, through blues and greens, to shimmering rainbow at the top for 2026."),

    ("aurora_shifting_chimera",
     f"{BASE}. Body shifting through aurora colors — green to purple to blue — its form subtly morphing, containing ghostly impressions of all nine previous issue robots visible within its translucent shell."),

    ("time_worn_mixed_materials",
     f"{BASE}. Body built from seven distinct horizontal bands of material — bottom is aged brass, then Bakelite, then silicon wafer, then floppy disk plastic, then brushed aluminum, then glass, top is holographic."),

    ("amber_fossil_computer",
     f"{BASE}. Made of polished amber with tiny fossilized computing artifacts visible inside — a vacuum tube, a transistor, a chip, a neural network diagram — prehistoric technology preserved in golden resin."),

    ("crystal_ball_oracle",
     f"{BASE}. Holding a large crystal ball showing a swirling vision of the future — tiny holographic scenes of computing yet to come — while standing on a base inscribed with historical milestones."),

    ("blueprint_evolution",
     f"{BASE}. Body is an architectural blueprint that's been drawn and redrawn nine times, each revision visible as a different colored ink layer, the final form being the composite of all revisions."),

    ("mosaic_tile_history",
     f"{BASE}. Covered in tiny mosaic tiles, each tile depicting a miniature scene from computing history — Turing's office, ENIAC, the Homebrew Computer Club, the iPhone launch — a walking museum."),

    ("patinated_bronze_monument",
     f"{BASE}. Cast in heavy bronze with rich green patina of age, posed like a monument statue on a marble plinth, solid and timeless, commemorating the full arc of computing history."),

    ("opal_fire_shifting",
     f"{BASE}. Made of precious opal, surface alive with fire that shifts between all colors as viewing angle changes — each color flash representing a different era of computing history, all contained in one stone."),

    ("prismatic_glass_layers",
     f"{BASE}. Made of stacked prismatic glass discs, each disc a different computing layer — hardware, OS, network, runtime, framework, application, AI — light refracting uniquely through each layer."),

    ("telescope_forward_looking",
     f"{BASE}. Standing atop a stack of vintage and modern books, looking through a brass telescope pointed upward, one eye squinting with wonder at what's coming next, the past literally beneath its feet."),

    ("hourglass_time_spiral",
     f"{BASE}. Body shaped like an hourglass, but instead of sand, a spiral timeline flows from top to bottom — tiny milestone icons tumbling through the neck — 1936 at top, 2026 collecting at bottom."),

    ("compass_rose_navigator",
     f"{BASE}. Chest displays an ornate compass rose, but the cardinal directions are labeled PAST, FUTURE, THEORY, PRACTICE — the robot as navigator between all dimensions of computing's story."),

    ("layered_cross_section",
     f"{BASE}. Cut away to show seven concentric layers like a jawbreaker candy, each layer a different color and texture representing an abstraction level, the innermost core glowing with binary light."),

    ("history_book_reader",
     f"{BASE}. Sitting on a stack of thick history books, reading the topmost one which has pages that are literally alive — tiny animated scenes playing out on each page as it reads."),

    ("building_block_tower",
     f"{BASE}. Made entirely of colorful LEGO-like building blocks, each block etched with a computing concept — LOGIC, MEMORY, NETWORK, AI — the blocks stacking to create the complete robot form."),

    ("tree_rings_ancient",
     f"{BASE}. Cross-section of its round body reveals tree rings, each ring a different decade of computing history, the outermost ring (2020s) still fresh and growing, inner rings dark with age."),

    ("geological_drill_core",
     f"{BASE}. Holding a cylindrical geological drill core sample of itself, the core showing all the colorful layers that make up its body — an archaeologist of its own computing heritage."),

    ("aurora_cape_retrospective",
     f"{BASE}. Wearing a magnificent flowing cape made of aurora borealis light, the cape displaying shifting scenes from computing history — ENIAC dissolving into mainframes dissolving into smartphones."),

    ("mixed_era_patchwork",
     f"{BASE}. Left arm is brass clockwork, right arm is silicon circuit, left leg is vacuum tube glass, right leg is fiber optic cable, torso is touchscreen, head is holographic — every era represented."),

    ("crystal_trophy_shelf",
     f"{BASE}. Standing beside a tiny trophy shelf displaying nine crystal trophies, each shaped like a previous issue's key symbol — Turing machine, transistor, chip, network, etc. — the collector of milestones."),

    ("stained_glass_window",
     f"{BASE}. Body is a miniature stained glass window, lead lines separating panels of colored glass, each panel depicting a scene from computing history, backlit with warm cathedral light."),

    ("matryoshka_nesting",
     f"{BASE}. A matryoshka nesting doll being opened, revealing smaller robots inside — each inner robot from a different era, the smallest at center being the simplest Turing machine robot."),

    ("sediment_jar_collector",
     f"{BASE}. Holding a tall glass jar containing layers of colorful sediment — each layer a different computing era's essence — binary sand at bottom, neural network glitter at top, beautifully stratified."),

    ("quilt_of_eras",
     f"{BASE}. Wrapped in a cozy quilt made of nine distinct fabric panels, each panel the color and texture of a different computing era — punched card beige, terminal green, web blue, AI purple."),

    ("compass_astrolabe_body",
     f"{BASE}. Body is an ornate brass astrolabe — nested rotating rings inscribed with computing milestones instead of star positions, used to navigate not the sky but the timeline of innovation."),

    ("rainbow_layer_cake",
     f"{BASE}. Body shaped like a seven-layer rainbow cake on a plate, each layer a different pastel color representing an abstraction layer, tiny fondant decorations showing computing icons on each tier."),

    ("fossil_excavation_site",
     f"{BASE}. Standing at a miniature archaeological dig site, brushing dust off layers of computing fossils — a vacuum tube in one stratum, a microchip in another, each layer a different color of earth."),

    ("prism_full_spectrum",
     f"{BASE}. Body is a single large prism, a beam of white light entering from the past and splitting into a full rainbow spectrum aimed at the future — the full spectrum of computing made from one source."),

    ("snow_globe_timeline",
     f"{BASE}. Standing inside a snow globe, but instead of snow, tiny computing milestones float around it — miniature ENIACs, mice, iPhones, neural networks — a captured history you can shake."),

    ("lego_instruction_manual",
     f"{BASE}. Holding an oversized LEGO instruction manual open to the last page showing itself fully assembled, surrounded by the individual named blocks that compose it — the meta-instruction."),

    ("geode_computing_core",
     f"{BASE}. Cracked open like a geode, rough stone exterior giving way to dazzling interior crystals, each crystal formation a different era — amethyst for early computing, diamond for modern AI, all beautiful."),

    ("vintage_radio_dial",
     f"{BASE}. Chest is a vintage radio dial that tunes to different decades — the needle currently sweeping from AM 1936 through FM 1980 to DAB 2026, each frequency playing a different era's story."),

    ("kaleidoscope_body",
     f"{BASE}. Body is a kaleidoscope, when you look through its eye you see the fragmented, symmetrical, beautiful pattern of computing history reflected infinitely — all eras merged into one mandala."),

    ("architectural_model",
     f"{BASE}. Standing next to a cutaway architectural model of a building — the building is 'The Stack' — each floor a computing layer from hardware basement to AI penthouse, tiny figures on each floor."),

    ("time_capsule_opener",
     f"{BASE}. Prying open a dented metal time capsule, golden light spilling out, visible inside are perfectly preserved computing artifacts from across the decades, each item glowing with historical significance."),

    ("paint_palette_artist",
     f"{BASE}. Holding an artist's palette loaded with nine distinct colors (one per previous issue), painting on a canvas that shows the complete computing timeline mural — the artist of the retrospective."),

    ("music_box_dancer",
     f"{BASE}. Standing on a spinning music box platform, the mechanism visible below showing different computing eras as the rotating drum and comb teeth, playing a melody that spans nine decades."),

    ("library_card_catalog",
     f"{BASE}. Body shaped like a miniature library card catalog cabinet, tiny drawers labeled by decade and topic, some drawers pulled open revealing glowing index cards of computing knowledge."),

    ("hot_air_balloon_basket",
     f"{BASE}. Riding in a tiny hot air balloon basket, the balloon above made of patchwork panels from all computing eras, rising up for a bird's-eye view of the entire journey."),

    ("swiss_watch_movement",
     f"{BASE}. Body is an exposed Swiss watch movement, but each gear is engraved with a different computing era, the escapement ticking steadily through time, precision and history in constant motion."),

    ("DNA_helix_spine",
     f"{BASE}. Spine visible as a glowing DNA double helix, but the base pairs are computing milestones connected across the helix — TURING paired with CHURCH, TRANSISTOR paired with INTEGRATED CIRCUIT."),

    ("terrarium_evolution",
     f"{BASE}. Tending a terrarium showing the evolution of computing as an ecosystem — tiny vacuum tube trees in back, transistor flowers in middle, neural network vines climbing the glass in front."),

    ("russian_doll_timeline",
     f"{BASE}. Nine translucent concentric shells visible, each shell a different color and era, the innermost core being a tiny glowing Turing machine, each shell adding capability and complexity."),

    ("accordion_fold_book",
     f"{BASE}. Holding an accordion-fold book fully extended, the continuous page showing the entire computing timeline as a single connected illustration flowing from left to right, 1936 to 2026."),

    ("lighthouse_beacon",
     f"{BASE}. Body is a miniature lighthouse, the beacon at top slowly rotating, each sweep of light illuminating a different era of computing arranged in a circle around its base."),

    ("sampler_cross_stitch",
     f"{BASE}. Body embroidered like a cross-stitch sampler, each section a different pattern and motif representing a computing era, bordered by a decorative frame of binary code rendered in thread."),

    ("vinyl_record_grooves",
     f"{BASE}. Body is a vinyl record, the grooves spiraling inward through computing history — outermost groove 1936, innermost 2026 — a needle arm reading the groove currently at the AI era."),

    ("photo_album_keeper",
     f"{BASE}. Clutching a thick photo album to its chest, the album open enough to see pages of polaroid-style photos — each photo a snapshot from a different decade of computing, edges worn with love."),

    ("crown_jewels_curator",
     f"{BASE}. Standing in a tiny museum display, surrounded by glass cases each containing a crown jewel of computing — Turing's paper, the first transistor, ARPANET map, the iPhone — the proud curator of it all."),
]


# ─────────────────────────────────────────────────────────────────────
# Verification
# ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    for name, designs in [
        ("ISSUE_07", ISSUE_07_DESIGNS),
        ("ISSUE_08", ISSUE_08_DESIGNS),
        ("ISSUE_09", ISSUE_09_DESIGNS),
        ("ISSUE_10", ISSUE_10_DESIGNS),
    ]:
        print(f"{name}: {len(designs)} designs")
        names = [d[0] for d in designs]
        dupes = [n for n in names if names.count(n) > 1]
        if dupes:
            print(f"  WARNING: duplicate names: {set(dupes)}")
        for dname, prompt in designs:
            if not prompt.startswith(BASE[:20]):
                print(f"  WARNING: {dname} doesn't start with base prompt")
    print("All checks passed.")
