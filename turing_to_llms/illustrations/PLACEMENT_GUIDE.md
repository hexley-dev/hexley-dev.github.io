# Illustrations — Placement Guide

Where each illustration fits within the original comic series.
These are standalone HTML files in `illustrations/` — they do **not** modify any issue files.

---

## 1. The Halting Problem → Issue 1, Page 7

**File:** `illustrations/halting_problem_proof.html`
**Complements:** The Halting Problem — some things are provably unsolvable

**Why it adds value:** The issue explains the halting problem in a few panels with a basic flow diagram. This illustration presents the full proof by contradiction in 6 beautifully laid-out panels with the PARADOX machine, contradictions shown as explosions, and Tera guiding the reader through the logic.

**Suggested callout:** "Want to see the full proof? The [Halting Problem Proof](../illustrations/halting_problem_proof.html) walks through every step of Turing's most famous argument."

---

## 2. Hardware Evolution: Room to Pocket → Issue 2, Pages 4 & 8-9

**File:** `illustrations/hardware_evolution.html`
**Complements:** Vacuum tubes as switches, transistors, integrated circuits

**Why it adds value:** The issue mentions the transition from vacuum tubes to transistors to ICs but doesn't show them at relative scale. This illustration draws ENIAC, a vacuum tube, a transistor, an IC, and a modern FinFET all to the same scale with a human figure reference. Includes cross-sections of each "switch" technology and the "if transistors were people" analogy.

**Suggested callout:** "See the incredible shrinking machine — the [Hardware Evolution](../illustrations/hardware_evolution.html) poster shows every era drawn to the same scale."

---

## 3. Von Neumann Architecture → Issue 2, Pages 6-7

**File:** `illustrations/von_neumann_blueprint.html`
**Complements:** Von Neumann's insight — store the program IN memory

**Why it adds value:** The issue has a before/after comparison but lacks a detailed architectural diagram. This blueprint shows full CPU internals (ALU, Control Unit, Registers), memory layout with mixed program/data cells, the bus system, I/O connections, FDE cycle inset, and memory hierarchy pyramid. Available in blueprint (dark) and light modes.

**Suggested callout:** "For the full technical diagram, see the [Von Neumann Architecture Blueprint](../illustrations/von_neumann_blueprint.html) — every component labeled and explained."

---

## 4. The Physical Internet → Issue 5, Pages 2-3

**File:** `illustrations/internet_physical_map.html`
**Complements:** Tim Berners-Lee, HTML, HTTP, the World Wide Web

**Why it adds value:** Issue 5 covers the Web as a concept but doesn't show the physical infrastructure. This illustration maps the entire path from your device to a data center across the ocean — routers, ISPs, exchange points, undersea cables, landing stations, and data centers. Includes a protocol stack envelope analogy and an undersea cable cross-section with shark armor.

**Suggested callout:** "The internet is physical! See the [Physical Internet Map](../illustrations/internet_physical_map.html) — from your device to a data center across the ocean."

---

## 5. Neural Network Anatomy → Issue 6, Pages 3-9

**File:** `illustrations/neural_network_anatomy.html`
**Complements:** Neural networks 101, backpropagation, CNNs, what networks "see"

**Why it adds value:** Issue 6 has step-through animations but no comprehensive labeled anatomy chart. This poster covers: the perceptron with labeled weights/bias/activation, 4 activation function plots (sigmoid, tanh, ReLU, softmax), a full MLP diagram with weight encoding, a CNN pipeline from pixels to classification with feature hierarchy, the training loop, and a key terms glossary.

**Suggested callout:** "For the complete anatomy chart, see the [Neural Network Anatomy Poster](../illustrations/neural_network_anatomy.html) — every part labeled like a biology textbook."

---

## 6. The Transformer Blueprint → Issue 7, Page 6

**File:** `illustrations/transformer_blueprint.html`
**Complements:** The Transformer architecture — a visual walkthrough

**Why it adds value:** Issue 7 walks through the Transformer floor by floor but doesn't have a single comprehensive reference diagram. This blueprint shows the full decoder-only architecture: tokenizer, embeddings, positional encoding (with sine waves), the Transformer block (LayerNorm, multi-head attention with 4 heads, FFN, residual connections), and the output head with softmax predictions. A detailed QKV mechanism inset shows the actual matrix operations.

**Suggested callout:** "See every component at once in the [Transformer Blueprint](../illustrations/transformer_blueprint.html) — the full architecture labeled and explained."

---

## 7. The Embedding Galaxy → Issue 7, Pages 5-6

**File:** `illustrations/embedding_galaxy.html`
**Complements:** Tokenization, the Transformer architecture

**Why it adds value:** Issue 7 mentions embeddings but doesn't visualize the space itself. This illustration maps ~67 words as glowing dots in a dark galaxy, with 6 visible clusters (animals, countries, professions, emotions, food, technology). Shows the famous vector arithmetic (king - man + woman = queen), word similarity as distance with gauges, the full embedding matrix, and how multimodal models embed images/audio/code into the same space.

**Suggested callout:** "Explore the word embedding space in the [Embedding Galaxy](../illustrations/embedding_galaxy.html) — see why similar words live near each other."

---

## 8. Agent Architecture Blueprint → Issue 8, Pages 4-8

**File:** `illustrations/agent_architecture.html`
**Complements:** Tool-use revolution, ReAct loop, Claude Code, error recovery

**Why it adds value:** Issue 8 has a ReAct step-through but no comprehensive system diagram. This blueprint shows the full agent pipeline: user prompt → system prompt → LLM core (with context window visualization) → tool router → 6 tools → ReAct loop → response. Includes a detailed tool call anatomy, error recovery flow, and agent vs. chatbot vs. autocomplete comparison table.

**Suggested callout:** "For the full system diagram, see the [Agent Architecture Blueprint](../illustrations/agent_architecture.html) — every component from prompt to tool execution."

---

## 9. The Pioneers → All Issues (especially Issue 10, Page 4)

**File:** `illustrations/pioneers_gallery.html`
**Complements:** Issue 10's visual timeline of all key figures

**Why it adds value:** Many key figures are mentioned in the text but don't have robot character representations. This gallery presents 19+ pioneers as robot characters across 7 eras, each with unique accent colors and distinguishing props (Turing's tape, Hopper's admiral hat, Thompson & Ritchie's pipe characters, Torvalds' penguin, Fei-Fei Li's camera, etc.).

**Suggested callout:** "Meet all the pioneers as robot characters in [The Pioneers Gallery](../illustrations/pioneers_gallery.html) — 7 eras, 19+ figures, each with their story."

---

## 10. The Computing Family Tree → Issue 10, Pages 2-4

**File:** `illustrations/computing_family_tree.html`
**Complements:** The full stack diagram, abstraction as superpower, the people who built it

**Why it adds value:** Issue 10 shows the stack as vertical layers but doesn't map the web of connections between all the series' concepts. This panoramic family tree has 37 nodes across 9 eras, showing direct influence (solid lines) and cross-era conceptual influence (dashed lines). The highlighted "Unix Echo" connection shows how "small tools piped together" (1969) echoes in "specialist agents coordinated" (2025).

**Suggested callout:** "See how every idea connects in the [Computing Family Tree](../illustrations/computing_family_tree.html) — 37 nodes, 90 years, one incredible lineage."

---

## Index Page

**File:** `illustrations/index.html`

A landing page with cards linking to all 10 illustrations, color-coded to match their companion issues.
