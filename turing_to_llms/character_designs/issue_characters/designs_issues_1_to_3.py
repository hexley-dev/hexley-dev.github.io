"""
Character design prompts for Issues 1-3 of "From Turing to Swarms".
50 curated multi-vector prompts per issue. Each blends 2-3 creative vectors.
"""

BASE = (
    "A cute tiny round robot character with two expressive dark eyes, "
    "small feet, photo-realistic, studio lighting, white seamless background, "
    "product photography style, sharp focus, 8k detail"
)

def _p(detail: str) -> str:
    return f"{BASE}, {detail}"


# ═══════════════════════════════════════════════════════════════════════════════
# ISSUE 1: "Scribble" — 1936, The Birth of Computing
# Era: Turing machines, Cambridge, mathematical foundations
# ═══════════════════════════════════════════════════════════════════════════════

ISSUE_01_DESIGNS = [
    # --- Brass & Clockwork family ---
    ("brass_clockwork_wonder",
     _p("body made of warm polished brass with visible clockwork gears turning inside a glass chest panel, holding a tiny magnifying glass, Victorian scientific instrument aesthetic.")),

    ("brass_orrery_thinker",
     _p("body of brushed brass with miniature orrery arms orbiting its head like a planetary model, etched with mathematical equations, contemplative pose.")),

    ("brass_compass_navigator",
     _p("warm brass shell with an inlaid compass rose on its belly, holding a protractor in one hand and a fountain pen in the other, Cambridge explorer energy.")),

    ("brass_telescope_dreamer",
     _p("golden brass body with a tiny telescope extending from one eye, surface engraved with Fibonacci spirals, standing on a stack of aged paper.")),

    ("brass_pocket_watch",
     _p("round body designed as a hinged pocket watch case in warm brass, face visible through a glass door in its chest showing spinning cogs, dangling a gold chain.")),

    # --- Parchment & Paper family ---
    ("parchment_scroll_sage",
     _p("body wrapped in aged yellowed parchment with visible handwritten equations in faded ink, a tiny wax seal on its shoulder, holding a quill pen.")),

    ("paper_tape_wanderer",
     _p("body made of layered strips of Turing machine paper tape, ones and zeros printed across the surface, trailing a long tape ribbon behind it like a scarf.")),

    ("origami_proof_bot",
     _p("body folded from cream-colored mathematical proof paper, crisp geometric origami folds forming its round shape, pencil-drawn diagrams visible on its surface.")),

    ("vellum_manuscript_keeper",
     _p("translucent vellum body with calligraphic mathematical notation visible inside like illuminated manuscript marginalia, gold leaf accents at the edges.")),

    ("aged_notebook_companion",
     _p("body textured like a worn leather-bound notebook, brass corner protectors, pages fanning out from its back like wings, graphite smudges on its surface.")),

    # --- Chalkboard & Cambridge family ---
    ("chalkboard_green_professor",
     _p("deep chalkboard-green body covered in chalk dust and half-erased equations, holding a stub of white chalk, wooden frame border around its face like a blackboard.")),

    ("cambridge_limestone_scholar",
     _p("body carved from pale Cambridge limestone with gothic arch details, tiny gargoyle-like feet, ivy tendrils curling around one arm, warm afternoon light.")),

    ("gothic_window_illuminated",
     _p("body inspired by Cambridge gothic stained glass, translucent colored glass panels forming its round shell, casting colored light shadows, lead came details.")),

    ("mahogany_study_dweller",
     _p("rich dark mahogany wood body with brass inlay mathematical symbols, green leather writing surface on its belly, inkwell balanced on its head.")),

    ("cambridge_don_tweed",
     _p("body wrapped in tiny Harris tweed fabric patches with leather elbow pads, wearing a miniature mortarboard, holding a chalk-dusted eraser.")),

    # --- Mathematical Concepts family ---
    ("golden_ratio_spiral",
     _p("body shape following the golden ratio spiral, shell made of mother-of-pearl with Fibonacci sequence numbers spiraling outward, iridescent finish.")),

    ("infinity_mirror_bot",
     _p("chrome and glass body with an infinity mirror effect in its chest, endless recursive reflections of itself getting smaller and smaller, mesmerizing glow.")),

    ("recursion_nesting_doll",
     _p("translucent resin body revealing a smaller version of itself inside, which contains an even smaller one, Russian nesting doll recursion concept, amber tint.")),

    ("decision_tree_branching",
     _p("walnut wood body with tiny brass branches growing from its head like a decision tree, yes/no labels on copper leaf tags hanging from each branch.")),

    ("halting_problem_frozen",
     _p("half warm brass and half blue crystalline ice, caught mid-step as if frozen in a decision, one foot hovering, expression of perpetual contemplation.")),

    # --- Typewriter & Mechanical Writing family ---
    ("typewriter_key_mosaic",
     _p("body covered in vintage circular typewriter keys, each showing a different letter, arms ending in tiny typebars, ink-ribbon spool on its back.")),

    ("fountain_pen_knight",
     _p("sleek body made of marbled fountain pen resin in deep blue and gold, nib-shaped feet, tiny ink cartridge visible through a clear chest panel.")),

    ("pencil_graphite_artist",
     _p("body made of cedar wood pencil material with a graphite tip on its head like a hat, yellow paint with green ferrule band, eraser-pink cheeks.")),

    ("wax_seal_diplomat",
     _p("deep burgundy wax body with an embossed mathematical seal on its chest, brass stamp handle on its back, dripping wax texture at the edges.")),

    ("telegraph_morse_messenger",
     _p("copper wire-wrapped body with a tiny telegraph key mounted on its arm, paper tape emerging from a slot in its side with dots and dashes.")),

    # --- Glass & Scientific Instrument family ---
    ("glass_bell_jar_specimen",
     _p("delicate blown glass body like a Victorian bell jar, visible copper and brass mechanism inside, sitting on a polished mahogany base with a brass nameplate.")),

    ("magnifying_lens_detective",
     _p("body made of polished optical glass and brass rings like a compound magnifying lens, light refracting through its torso, rainbow caustics on the surface below.")),

    ("porcelain_lab_instrument",
     _p("white porcelain body with hand-painted blue mathematical diagrams in Delft pottery style, brass measurement markings along its sides, clinical precision aesthetic.")),

    ("copper_electroscope_charged",
     _p("copper body with thin gold leaf antennae that spread apart as if electrically charged, glass insulator base, amber static electricity sparks.")),

    ("barometer_weather_oracle",
     _p("polished brass and glass barometer body with a mercury column visible inside, dial face on its belly with 'DECIDABLE' and 'UNDECIDABLE' instead of weather.")),

    # --- Surreal & Abstract Concept family ---
    ("turing_tape_infinite",
     _p("body seemingly unraveling into an infinite paper tape that spirals outward in all directions, symbols being written by a tiny mechanical arm, existential wonder.")),

    ("thought_experiment_cloud",
     _p("lower half solid brass machinery, upper half dissolving into ethereal cloudy thought-bubble material, equations floating in the mist, dreamy yet mechanical.")),

    ("binary_split_duality",
     _p("body split vertically — left side polished ivory with engraved zeros, right side ebony wood with engraved ones, thin brass dividing line, balanced perfectly.")),

    ("entscheidungsproblem_maze",
     _p("body surface is an intricate etched brass labyrinth with no exit, tiny mechanical pencil tracing the path endlessly, German gothic lettering on its base.")),

    ("universal_machine_chameleon",
     _p("body made of liquid mercury-like chrome that reflects and mimics the shapes of objects around it, currently mid-morph between a calculator and a typewriter.")),

    # --- Leather & Vintage Material family ---
    ("leather_satchel_explorer",
     _p("body made of worn tan leather like a Cambridge professor's satchel, brass buckle on its chest, paper documents peeking out from seams, patina of age.")),

    ("ivory_chess_strategist",
     _p("carved ivory-colored body like a chess piece, Staunton knight shape influence, standing on a tiny chessboard base, strategic contemplation in its eyes.")),

    ("tin_automaton_vintage",
     _p("painted tin body in the style of a 1930s wind-up toy, lithographed mathematical patterns, visible winding key on its back, slight rust patina at joints.")),

    ("walnut_cabinet_curious",
     _p("body shaped like a miniature walnut wood curiosity cabinet with tiny brass-handled drawers, some slightly open revealing mathematical symbols inside.")),

    ("copper_pipe_steampunk",
     _p("body assembled from copper plumbing fittings and pipe joints, pressure gauge on its chest, tiny steam wisps rising from a valve on its head, warm patina.")),

    # --- Light & Energy family ---
    ("candle_wax_illuminator",
     _p("body made of dripping cream-colored candle wax with a tiny brass candleholder on its head, warm flame glowing, mathematical shadows cast on the surface below.")),

    ("phosphorescent_equation",
     _p("dark navy body with phosphorescent green mathematical equations that glow like radium paint on a watch dial, 1930s luminous instrument aesthetic.")),

    ("prism_rainbow_logician",
     _p("crystal prism body splitting a beam of white light into a spectrum, each color band carrying a different mathematical symbol, Newton meets Turing.")),

    # --- Hybrid & Unexpected Combinations ---
    ("music_box_mathematician",
     _p("body is a tiny brass music box with a hand-crank, when opened reveals a paper cylinder with punched mathematical sequences instead of musical notes, melody of logic.")),

    ("snow_globe_cambridge",
     _p("sitting inside a glass snow globe with tiny Cambridge spires behind it, mathematical symbols falling like snowflakes, wooden base with brass plaque reading '1936'.")),

    ("beeswax_honeycomb_computer",
     _p("warm golden beeswax body with hexagonal honeycomb cells visible in cross-section, each cell containing a tiny brass gear or symbol, organic computation.")),

    ("chalk_dust_ghost",
     _p("body appears to be made of compressed chalk dust in various pastel colors, slightly dissolving at the edges, leaving a trail of equations in its wake.")),

    ("compass_rose_voyager",
     _p("body engraved like an antique nautical compass rose in brass and silver, cardinal directions replaced with logical operators AND/OR/NOT/IF, adventurer spirit.")),

    ("bookend_guardian",
     _p("body shaped like an ornate cast-iron bookend, supporting a tiny stack of leather-bound mathematics texts, Art Nouveau vine patterns, scholarly protector.")),

    ("abacus_ribcage_counter",
     _p("translucent body revealing an internal skeleton made of tiny wooden abacus frames, colored beads sliding along brass rods as it moves, computation made visible.")),
]


# ═══════════════════════════════════════════════════════════════════════════════
# ISSUE 2: "Valvie" — 1940s-1950s, Building the First Brains
# Era: Vacuum tubes, WWII, ENIAC, von Neumann, Colossus
# ═══════════════════════════════════════════════════════════════════════════════

ISSUE_02_DESIGNS = [
    # --- Vacuum Tube & Glass family ---
    ("vacuum_tube_heart",
     _p("body built around a large central glass vacuum tube glowing warm orange, visible tungsten filament inside its chest, bakelite base for feet, 1940s electronics aesthetic.")),

    ("glass_tube_cathedral",
     _p("body made of multiple miniature vacuum tubes arranged like cathedral organ pipes, each glowing a slightly different amber shade, chrome tube sockets visible.")),

    ("nixie_tube_display",
     _p("chest features a functioning nixie tube display showing binary digits in warm orange neon, glass envelope body with visible wire cathodes, retro-futuristic warmth.")),

    ("oscilloscope_face",
     _p("round green phosphor oscilloscope screen as its face showing a sine wave that curves into a smile, military-spec olive drab metal housing, chunky rubber feet.")),

    ("cathode_ray_dreamer",
     _p("body shaped like a miniature cathode ray tube, electron beam visible inside painting patterns of light on its face, magnetic deflection coils as ears.")),

    # --- Military & Wartime family ---
    ("military_olive_drab_soldier",
     _p("riveted steel body painted in military olive drab with stenciled serial numbers, wearing a tiny field cap, canvas strap across its chest, wartime urgency.")),

    ("bletchley_park_codebreaker",
     _p("dark bakelite body with brass rotors visible through a window like an Enigma machine, wearing a tiny wool scarf, secret intelligence aesthetic, understated heroism.")),

    ("radar_dish_sentinel",
     _p("body topped with a spinning miniature radar dish, military green and chrome finish, tiny signal waves emanating outward, coastal defense station vibe.")),

    ("ammunition_box_tough",
     _p("body shaped like a WWII ammunition box in olive green steel, stenciled 'CLASSIFIED' and 'HANDLE WITH CARE', thick rubber gasket seams, utilitarian beauty.")),

    ("paratrooper_signals_bot",
     _p("olive canvas body with miniature parachute silk draped from its back, field radio strapped to its chest with copper wire antenna, Morse key on its arm.")),

    # --- Bakelite & Early Plastics family ---
    ("bakelite_radio_crooner",
     _p("body made of rich dark-brown marbled bakelite with Art Deco ridges, chrome dial on its chest, fabric speaker grille on its belly, 1940s living room warmth.")),

    ("phenolic_circuit_board",
     _p("body made of amber phenolic resin with visible copper circuit traces running across its surface, point-to-point hand-soldered joints, warm translucent glow.")),

    ("bakelite_telephone_operator",
     _p("body shaped like a 1940s bakelite telephone handset, rotary dial on its belly, cloth-wrapped cord as a tail, chrome finger stop details.")),

    ("rubber_insulation_bouncy",
     _p("body made of black rubber insulation material with embossed voltage ratings, flexible and slightly squeezable appearance, copper wire peeking from joints.")),

    ("switch_panel_commander",
     _p("body covered in rows of miniature chrome toggle switches and indicator lamps, each in a different state (up/down, red/green), industrial control panel aesthetic.")),

    # --- Copper & Wiring family ---
    ("copper_wire_wrapped",
     _p("body wrapped in tightly coiled bare copper wire like an electromagnet, magnetic field lines suggested by iron filing patterns on its surface, industrial magnetism.")),

    ("patch_cable_octopus",
     _p("body bristling with colorful patch cables plugged into sockets all over its surface, banana plugs and alligator clips at the ends, telephone switchboard energy.")),

    ("soldering_iron_craftsman",
     _p("body made of nickel-plated steel with a tiny soldering iron built into one arm, wisps of rosin flux smoke, solder blob joints visible, maker aesthetic.")),

    ("relay_switch_clicker",
     _p("body built from stacked electromagnetic relay switches, tiny armatures clicking open and closed, visible spring contacts, the sound of early computing made physical.")),

    ("wiring_diagram_blueprint",
     _p("flat cream-colored body printed with a detailed wiring diagram in blue ink, blueprint aesthetic, component callouts and measurement annotations, engineering precision.")),

    # --- Room-Sized Computer family ---
    ("eniac_panel_fragment",
     _p("body is a miniature section of ENIAC's front panel, covered in digit wheels and function switches, thick bundles of cables emerging from its back, monumental scale made tiny.")),

    ("computer_room_miniature",
     _p("transparent body revealing a complete miniature room-sized computer inside, tiny blinking lights and spinning tape reels, like a ship in a bottle but with ENIAC.")),

    ("punch_card_armor",
     _p("body armored in overlapping ivory punch cards like dragon scales, rectangular holes creating patterns of light through its shell, IBM card stock texture.")),

    ("tape_reel_backpack",
     _p("chrome and military green body carrying two large magnetic tape reels on its back like a backpack, tape threading between them across its chest.")),

    ("blinking_light_constellation",
     _p("dark steel body covered in dozens of tiny incandescent bulbs arranged in grid patterns, each blinking in sequence like a computation in progress, mesmerizing.")),

    # --- Chrome & Industrial Metal family ---
    ("chrome_rivet_tank",
     _p("thick riveted steel plate body in gunmetal grey with chrome accent rivets, industrial flanges at joints, chunky and indestructible, American heavy industry aesthetic.")),

    ("nickel_plate_elegant",
     _p("body plated in mirror-finish nickel with Art Deco geometric patterns etched into the surface, streamlined 1940s industrial design, chrome accents.")),

    ("cast_iron_foundry",
     _p("heavy cast iron body with visible mold seams and a rough sand-cast texture, painted in enamel red and black, hand-filed edges, brutalist charm.")),

    ("aluminum_aircraft_skin",
     _p("body made of riveted aircraft aluminum skin panels, flush rivets in neat rows, military aircraft insignia roundel on its chest, lightweight but strong.")),

    ("steel_filing_cabinet",
     _p("body shaped like a miniature grey steel filing cabinet with tiny drawers labeled MEMORY, ACCUMULATOR, CONTROL, brass handles, von Neumann architecture made physical.")),

    # --- Wartime Code & Secrecy family ---
    ("enigma_rotor_stack",
     _p("body made of three stacked brass rotors with alphabet rings, visible contact points and wiring between layers, military field grey housing, secrets within secrets.")),

    ("cipher_text_encrypted",
     _p("body covered in seemingly random five-letter cipher groups stamped in military typeface, MOST SECRET header at the top, red wax security seal, one-time pad texture.")),

    ("colossus_paper_tape_reader",
     _p("body built around a miniature paper tape reader mechanism, tape threading through at high speed, photoelectric reading head glowing, Bletchley Park secret weapon.")),

    ("blackout_curtain_shadow",
     _p("dark navy body with blackout curtain fabric texture, tiny pinpricks of light showing through like stars or indicator lamps behind heavy drapes, wartime London mood.")),

    ("carrier_pigeon_hybrid",
     _p("steel and canvas body with tiny mechanical wings folded at its sides, a miniature message capsule strapped to its leg, wartime communications romance.")),

    # --- Von Neumann & Architecture family ---
    ("von_neumann_architecture_bot",
     _p("body clearly divided into labeled sections: MEMORY drum on top, CONTROL unit face, ARITHMETIC chest, INPUT left arm, OUTPUT right arm, architecture diagram made physical.")),

    ("stored_program_library",
     _p("body like a tiny revolving bookshelf filled with miniature program cards, each slot labeled with a different instruction, the concept of stored programs as a library.")),

    ("mercury_delay_line",
     _p("body containing a visible glass tube filled with liquid mercury, acoustic pulses traveling back and forth as glowing dots, exotic early memory technology.")),

    ("williams_tube_memory",
     _p("body featuring a small CRT screen showing a grid of glowing dots representing stored bits, phosphor green on dark glass, the first random access memory.")),

    ("accumulator_register",
     _p("body made of a row of mechanical decade counters like an adding machine, digits visible through windows, carry propagation in progress, the heart of arithmetic.")),

    # --- Energy & Heat family ---
    ("overheating_tube_bank",
     _p("body glowing hot with visible heat shimmer, array of vacuum tubes running at maximum, tiny cooling fans spinning desperately, red-hot filaments, controlled chaos.")),

    ("power_supply_humming",
     _p("massive transformer body with laminated steel core visible through vents, thick power cables, vibrating slightly with 60Hz hum, the unsung hero of computing.")),

    ("lightning_strike_genesis",
     _p("dark stormy bakelite body with a bright electric arc jumping between two brass terminals on its head, Frankenstein's monster meets ENIAC, creation moment.")),

    # --- Hybrid & Unexpected family ---
    ("rosie_riveter_compute",
     _p("chrome and red enamel body wearing a tiny polka-dot bandana, flexing one arm showing a vacuum tube bicep, 'We Can Compute It!' attitude, wartime worker spirit.")),

    ("war_bond_poster_bot",
     _p("flat body styled like a 1940s war bond propaganda poster, bold red-white-blue patriotic colors, Art Deco typography, 'Buy Compute Bonds' energy, lithograph texture.")),

    ("jukebox_calculator",
     _p("body shaped like a miniature 1940s Wurlitzer jukebox, chrome and colored glass, but instead of records the selection bubbles show mathematical operations.")),

    ("neon_diner_sign",
     _p("body made of bent glass neon tubing in warm pink and blue, glowing steadily, chrome mounting brackets, 1950s American diner sign aesthetic, nostalgic computing.")),

    ("bomb_disposal_careful",
     _p("heavily armored body with thick steel plating, tiny mechanical gripper arms for delicate work, stenciled warnings, the precision of codebreaking as bomb disposal metaphor.")),

    ("slide_rule_precision",
     _p("body made of ivory and mahogany like a precision slide rule, logarithmic scales engraved along its sides, brass cursor sliding across its belly, analog elegance.")),

    ("geiger_counter_nervous",
     _p("body incorporating a Geiger-Müller tube, clicking frantically when near anything radioactive (or interesting), mica window on its chest, atomic age anxiety.")),

]


# ═══════════════════════════════════════════════════════════════════════════════
# ISSUE 3: "Compiler" — 1950s-1960s, Teaching Machines to Understand Us
# Era: Programming languages, Grace Hopper, compilers, FORTRAN, COBOL, LISP
# ═══════════════════════════════════════════════════════════════════════════════

ISSUE_03_DESIGNS = [
    # --- Punch Card & Data Processing family ---
    ("punch_card_couture",
     _p("body clad in overlapping ivory-colored punch cards arranged like haute couture fashion scales, rectangular chad confetti at its feet, IBM 80-column precision.")),

    ("card_sorter_librarian",
     _p("body shaped like a miniature card sorting machine, intake hopper on its head, twelve output pockets across its body, cards flying into sorted positions.")),

    ("chad_confetti_celebration",
     _p("cream-colored body covered in tiny rectangular punch card chads like confetti, some still falling, manila folder texture, joyful data processing party.")),

    ("keypunch_operator_nimble",
     _p("cream plastic body with miniature keypunch keys for fingers, IBM blue accent stripe, a fresh punch card emerging from a slot in its chest, rapid-fire precision.")),

    ("hollerith_tabulator",
     _p("heavy cast-iron base with a body of brass counting mechanisms, mercury cup contacts on its feet, census data era, Herman Hollerith's legacy in miniature.")),

    # --- Phosphor Green & Terminal family ---
    ("phosphor_green_glow",
     _p("dark body with a round phosphor-green CRT screen for a face, blinking cursor waiting for input, scan lines visible, the iconic green-on-black terminal aesthetic.")),

    ("teletype_chatterbox",
     _p("body built around a miniature teletype mechanism, paper continuously printing from its mouth, mechanical typebars striking, the sound of early programming.")),

    ("terminal_cursor_blink",
     _p("matte black body with a single bright green square cursor blinking on its forehead, '>_' prompt displayed, patient and waiting, minimalist terminal energy.")),

    ("green_screen_matrix",
     _p("body surface covered in cascading phosphor-green characters like a green-screen waterfall, FORTRAN code fragments visible, the Matrix before the Matrix.")),

    ("paper_printout_scroll",
     _p("body wrapped in continuous-feed green-bar printer paper, tractor-feed holes along the edges, COBOL program listing printed across its surface, accordion-folded.")),

    # --- Grace Hopper & Navy family ---
    ("navy_dress_uniform",
     _p("body clad in miniature navy blue dress uniform fabric with gold buttons and tiny rank insignia, white officer's cap perched on top, Grace Hopper's determination.")),

    ("moth_bug_detective",
     _p("magnifying glass in hand, examining a tiny real moth stuck to its chest with a strip of tape labeled 'First actual case of bug being found', forensic curiosity.")),

    ("admirals_hat_coder",
     _p("navy blue and gold body wearing an oversized admiral's bicorne hat, holding a tiny COBOL manual, stern but approachable, translating human language to machine.")),

    ("navy_signal_flags",
     _p("body festooned with miniature international maritime signal flags spelling out a message in code, navy blue base, brass naval telescope tucked under one arm.")),

    ("hopper_nanosecond_wire",
     _p("holding a tiny 11.8-inch piece of copper wire in one hand — Hopper's famous nanosecond demonstration — navy uniform body, teaching pose, making the abstract tangible.")),

    # --- Compiler & Translation family ---
    ("rosetta_stone_translator",
     _p("body carved from dark granite like the Rosetta Stone, three bands of text: English on top, assembly in the middle, binary at the bottom, the compiler as decoder ring.")),

    ("dictionary_spine_tower",
     _p("body made of stacked miniature leather-bound dictionaries (FORTRAN, COBOL, LISP, ALGOL), each a different color, bookmarks poking out, polyglot translator.")),

    ("babel_fish_compiler",
     _p("translucent aquatic-blue body with text entering one ear in English and exiting the other ear as machine code, the universal translator concept, whimsical.")),

    ("red_pencil_editor",
     _p("body made of red pencil material with an eraser cap hat, holding a manuscript with crossed-out syntax errors and correction marks, the compiler as strict editor.")),

    ("carbon_copy_duplicator",
     _p("body layered in carbon paper sheets — white original on top, blue copy beneath — text transferring between layers, the compilation as carbon copying from high to low.")),

    # --- LISP & Parentheses family ---
    ("parentheses_nested_deep",
     _p("body constructed entirely from nested brass parentheses of decreasing size, like Russian nesting dolls made of punctuation, LISP philosophy incarnate.")),

    ("s_expression_tree",
     _p("body with a tiny binary tree growing from its head, each node a polished wooden sphere containing a symbol, cons cells visible as brass connectors, LISP data structure.")),

    ("lambda_calculus_greek",
     _p("marble body carved in Greek classical style with a large lambda symbol on its chest like a superhero emblem, laurel wreath of parentheses, functional programming deity.")),

    ("garbage_collector_janitor",
     _p("body wearing a tiny janitor's apron, pushing a miniature cart collecting discarded memory cells, broom in hand sweeping up unused pointers, LISP memory management.")),

    ("recursive_spiral_shell",
     _p("body shaped like a nautilus shell in opalescent mother-of-pearl, each chamber containing a smaller function call, recursive descent made beautiful, Fibonacci proportions.")),

    # --- IBM & Mainframe family ---
    ("ibm_blue_executive",
     _p("body in brushed aluminum with IBM blue accent panels, tiny white shirt collar detail, corporate precision, mainframe room air conditioning hum, buttoned-up elegance.")),

    ("mainframe_room_tiny",
     _p("body containing a miniature visible mainframe room behind glass panels — tape drives, card readers, raised floor tiles — all working at tiny scale, data center in a bottle.")),

    ("magnetic_tape_wrapped",
     _p("body wrapped in brown magnetic tape like a mummy, reels on shoulders spinning to unspool and re-spool, oxide coating shimmer, sequential access storytelling.")),

    ("raised_floor_tile",
     _p("body textured like pale yellow perforated raised floor tiles from a 1960s computer room, visible cable bundles underneath, air conditioning grate on top.")),

    ("ibm_selectric_ball",
     _p("body shaped like an IBM Selectric typing element (golf ball), chrome with raised character faces, spinning to find the right letter, mechanical precision poetry.")),

    # --- Abstraction & Language Concepts family ---
    ("abstraction_ladder_climber",
     _p("standing on a tiny ladder where each rung is labeled from bottom to top: BINARY, ASSEMBLY, FORTRAN, ENGLISH — climbing upward toward human language, aspirational.")),

    ("syntax_tree_bonsai",
     _p("body of polished mahogany tending a miniature bonsai tree whose branches form a parse tree diagram, leaf nodes are terminal symbols, careful cultivation of grammar.")),

    ("stack_frame_tower",
     _p("body made of stacked transparent acrylic frames, each containing local variables and a return address, the call stack visualized as a physical tower, about to pop.")),

    ("flowchart_diamond_bot",
     _p("body shaped like a flowchart decision diamond, YES and NO paths extending from its sides as tiny brass arrows, perpetually at a branching point, decisive expression.")),

    ("bootstrap_paradox",
     _p("body lifting itself by its own bootstraps — literally pulling on tiny leather boot straps attached to its feet while hovering, the compiler compiling itself, impossible but real.")),

    # --- Manila & Office Supply family ---
    ("manila_folder_filed",
     _p("body made of manila folder cardstock with a typed label tab on its head, metal brad fasteners at joints, coffee ring stain on one side, government bureaucracy charm.")),

    ("carbon_ribbon_typewriter",
     _p("body threaded with carbon typewriter ribbon in a figure-eight path, inked letters transferring to its surface as it moves, mechanical text processing.")),

    ("rubber_stamp_bureaucrat",
     _p("body made of red rubber with carved reversed text on its base, holding a tiny ink pad, stamping APPROVED and COMPILED on everything it touches, official business.")),

    ("filing_cabinet_organized",
     _p("body shaped like a miniature four-drawer filing cabinet in battleship grey, tiny labeled tabs visible: SUBROUTINES, VARIABLES, CONSTANTS, ERRORS, organized mind.")),

    ("interoffice_memo_courier",
     _p("cream plastic body carrying a stack of yellow interoffice memos, routing slip attached with multiple department stamps, the message-passing paradigm as office mail.")),

    # --- Debugging & Bug family ---
    ("moth_wings_debugger",
     _p("body with delicate translucent moth wings spread wide, antennae twitching, holding a magnifying glass and tweezers, the spirit of debugging, nocturnal problem-solver.")),

    ("bug_jar_collector",
     _p("carrying a glass mason jar containing tiny glowing bugs, each labeled with an error type (SYNTAX, RUNTIME, LOGIC), entomologist of errors, curious collector.")),

    ("tape_and_logbook_forensic",
     _p("body holding a tiny spiral-bound logbook open to a page reading 'Bug #1: Moth found in relay', actual moth specimen taped to the page, historical documentation.")),

    # --- Hybrid & Unexpected family ---
    ("cocktail_party_protocol",
     _p("wearing a tiny 1960s cocktail dress made of punch card material, holding a martini glass containing phosphor-green liquid, the social networking of early programming culture.")),

    ("jukebox_subroutine",
     _p("body shaped like a miniature Seeburg jukebox, but selection buttons labeled with subroutine names instead of songs, selecting CALL and RETURN, structured programming as playlist.")),

    ("knitting_pattern_programmer",
     _p("body made of knitted wool in Fair Isle patterns, but the pattern is actually binary code, holding tiny knitting needles, the textile origins of computing, warm and algorithmic.")),

    ("chess_engine_thinker",
     _p("body made of alternating black and white chess board squares, tiny chess pieces orbiting its head in evaluation, Shannon's chess program, deep artificial thought.")),

    ("time_sharing_splitter",
     _p("body appearing in three slightly transparent overlapping copies of itself, each doing a different task simultaneously, time-sharing the same physical space, ghostly multitasking.")),

    ("core_memory_weaver",
     _p("body made of a grid of tiny magnetic ferrite cores threaded with fine copper wire in X-Y patterns, the intricate handmade craft of magnetic core memory, artisanal computing.")),

    ("fortran_formula_alchemist",
     _p("body of brushed copper with alchemical symbols that morph into FORTRAN keywords, philosopher's stone on its chest glowing, transforming mathematical formulas into machine instructions.")),
]


# --- Validation ---
assert len(ISSUE_01_DESIGNS) == 50, f"Issue 1 has {len(ISSUE_01_DESIGNS)} designs, expected 50"
assert len(ISSUE_02_DESIGNS) == 50, f"Issue 2 has {len(ISSUE_02_DESIGNS)} designs, expected 50"
assert len(ISSUE_03_DESIGNS) == 50, f"Issue 3 has {len(ISSUE_03_DESIGNS)} designs, expected 50"

# All names unique within each issue
for name, designs in [("Issue 1", ISSUE_01_DESIGNS), ("Issue 2", ISSUE_02_DESIGNS), ("Issue 3", ISSUE_03_DESIGNS)]:
    names = [d[0] for d in designs]
    assert len(names) == len(set(names)), f"{name} has duplicate design names: {[n for n in names if names.count(n) > 1]}"

if __name__ == "__main__":
    total = len(ISSUE_01_DESIGNS) + len(ISSUE_02_DESIGNS) + len(ISSUE_03_DESIGNS)
    print(f"Total designs: {total}")
    for i, designs in enumerate([ISSUE_01_DESIGNS, ISSUE_02_DESIGNS, ISSUE_03_DESIGNS], 1):
        print(f"\nIssue {i}: {len(designs)} designs")
        for name, prompt in designs[:3]:
            print(f"  {name}: {prompt[:80]}...")
