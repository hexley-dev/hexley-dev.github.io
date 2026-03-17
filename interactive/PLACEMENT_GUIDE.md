# Interactive Labs — Placement Guide

Where each interactive visualization fits within the original comic series.
These are standalone HTML files in `interactive/` — they do **not** modify any issue files.

---

## 1. Turing Machine Sandbox → Issue 1, Pages 4-5

**File:** `interactive/turing_machine_sandbox.html`
**Complements:** The Turing Machine introduction (Page 4) and the step-by-step 1+1 trace (Page 5)

**Why it adds value:** The issue has a fixed 6-step walkthrough. The sandbox lets readers write their own rules, define custom tapes, and run arbitrary programs — turning passive observation into active experimentation.

**Suggested placement:** After Page 5's walkthrough, a callout box could say:
> "Want to build your own Turing Machine? Try the [Turing Machine Sandbox](../interactive/turing_machine_sandbox.html) — write rules, load a tape, and watch it compute!"

**Pre-loaded examples:**
- Unary Addition (2+2=4) — extends the comic's 1+1 example
- Binary Increment — adds 1 to a binary number
- Palindrome Checker — demonstrates decision problems
- Busy Beaver (3-state) — the famous complexity benchmark

---

## 2. Logic Gates Lab → Issue 2, Pages 4-8

**File:** `interactive/logic_gates_lab.html`
**Complements:** Vacuum tubes as switches (Page 4), von Neumann architecture (Pages 7-8), transistors (Page 8)

**Why it adds value:** Issue 2 explains that vacuum tubes are ON/OFF switches but doesn't show how switches compose into logic. The lab bridges the gap from "a switch" to "a calculator" with interactive AND/OR/NOT gates, a half-adder, full-adder, and a working 4-bit binary calculator.

**Suggested placement:** After Page 4 (vacuum tubes as switches), a callout could say:
> "Switches can do math? See it for yourself in the [Logic Gates Lab](../interactive/logic_gates_lab.html) — build a calculator from nothing but ON/OFF switches!"

---

## 3. Compiler Explorer → Issue 3, Pages 4-7

**File:** `interactive/compiler_explorer.html`
**Complements:** Grace Hopper's compiler (Page 4), FORTRAN (Page 5), the abstraction ladder (Page 7)

**Why it adds value:** Issue 3's abstraction ladder is a static diagram. The Explorer makes it live — users type real code and watch it transform through 4 layers (source → AST → assembly → binary) with mapping lines showing how each element corresponds across levels.

**Suggested placement:** After Page 7 (the abstraction ladder), a callout could say:
> "See the abstraction ladder in action! Type code in the [Compiler Explorer](../interactive/compiler_explorer.html) and watch it transform all the way down to binary."

**Includes Grace Hopper's quote** from 1952 about nobody believing she had a working compiler.

---

## 4. Unix Pipe Playground → Issue 4, Pages 3-5

**File:** `interactive/unix_pipe_playground.html`
**Complements:** Unix philosophy (Page 3), piping small tools together (Pages 4-5)

**Why it adds value:** Issue 4 has a fixed 5-step walkthrough of `sort | uniq | wc -l`. The playground gives users a real command palette with 13 tools, 5 sample files, and a visual pipeline showing data transforming at each stage. Users can build multi-step pipelines and see the data flow column by column.

**Suggested placement:** After Page 5 (piping tools together), a callout could say:
> "Build your own Unix pipelines! Try the [Unix Pipe Playground](../interactive/unix_pipe_playground.html) — chain small tools together and watch data flow through each stage."

**Pre-loaded challenges:**
- Count unique names — `sort | uniq | wc -l`
- Find the most common name — `sort | uniq -c | sort -n | tail -n 1`
- Extract IPs from logs — `cut -d" " -f1 | sort | uniq`
- Reverse a poem — `rev`

---

## 5. Neural Network Playground → Issue 6, Pages 3-5

**File:** `interactive/neural_network_playground.html`
**Complements:** Neural networks 101 (Page 3), backpropagation (Page 4), the three godfathers (Page 5)

**Why it adds value:** Issue 6 has step-through animations of backprop and CNN hierarchies. The playground lets readers actually TRAIN a network: place data points, configure the architecture, adjust learning rate, and watch the decision boundary evolve in real-time. The "aha moment" is seeing the network discover a pattern entirely on its own.

**Suggested placement:** After Page 4 (backpropagation), a callout could say:
> "Want to train your own neural network? Open the [Neural Network Playground](../interactive/neural_network_playground.html) — place dots, hit Train, and watch it learn!"

**Pre-loaded datasets:** Circle, XOR, Spiral, Linear, Gaussian — each demonstrates different things a network can (or struggles to) learn.

---

## 6. Attention Visualizer → Issue 7, Pages 3-6

**File:** `interactive/attention_visualizer.html`
**Complements:** Self-attention mechanism (Pages 3-4), QKV transformation (Page 5), the Transformer architecture (Page 6)

**Why it adds value:** Issue 7's step-through shows attention on one fixed sentence. The Visualizer lets users type ANY sentence and explore 4 simulated attention heads (positional, syntactic, semantic, global), see an NxN heatmap matrix, and watch beam arcs connect tokens. The QKV panel makes the math tangible.

**Suggested placement:** After Page 4 (self-attention), a callout could say:
> "Type your own sentence and see attention in action! The [Attention Visualizer](../interactive/attention_visualizer.html) shows which words pay attention to which."

**Pre-loaded examples:** Pronoun resolution, word sense disambiguation, Winograd schema — each reveals how attention captures different linguistic relationships.

---

## 7. Agent Sandbox → Issue 8, Pages 4-8

**File:** `interactive/agent_sandbox.html`
**Complements:** The tool-use revolution (Page 4), ReAct loop (Pages 5-6), Claude Code demo (Page 7), error recovery (Page 8)

**Why it adds value:** Issue 8 has a fixed step-through of the ReAct loop. The sandbox lets users give a simulated agent a task and watch it reason through THINK/PLAN/ACT/OBSERVE cycles in real-time. The "Fix the Bug" task demonstrates error recovery — the agent hits a failing test, re-reads the code, finds a second bug, and fixes it. Manual Mode lets users play the agent themselves, discovering that choosing the right tool is the hard part.

**Suggested placement:** After Page 6 (ReAct loop), a callout could say:
> "Want to see an agent in action? The [Agent Sandbox](../interactive/agent_sandbox.html) lets you watch an AI agent think, plan, and recover from mistakes — or play the agent yourself!"

**Pre-built tasks:**
- Fix the Bug — two bugs in calculator.js, error recovery after first fix
- Add Dark Mode — add CSS rules and pass tests
- Count the Words — read a file and run a script
- Find the Secret — search across 3 files for a hidden message

---

## 8. Swarm Simulator → Issue 9, Pages 3-8

**File:** `interactive/swarm_simulator.html`
**Complements:** Multi-agent architectures (Pages 4-5), the Constellation Pattern (Page 5), watching a swarm build a web app (Page 8)

**Why it adds value:** Issue 9's step-through shows a fixed timeline. The simulator lets readers BE the orchestrator: assign tasks to agents, watch parallel execution on a real Gantt chart, see file-based communication in a terminal log, and compare sequential vs. parallel completion time. The "Create a Comic Issue" template is a meta-moment — it mirrors the exact pipeline that produced the comic.

**Suggested placement:** After Page 5 (Constellation Pattern), a callout could say:
> "Try orchestrating a swarm yourself! The [Swarm Simulator](../interactive/swarm_simulator.html) lets you assign tasks, watch agents work in parallel, and see why teams beat solo agents."

**Project templates:**
- Build a Weather App (default)
- Create a Comic Issue (mirrors this series' production pipeline!)
- Deploy a Website

---

## 9. Full Stack Elevator → Issue 10, Pages 2-3

**File:** `interactive/full_stack_elevator.html`
**Complements:** The full stack diagram (Page 2), abstraction as superpower (Page 3)

**Why it adds value:** Issue 10's stack diagram is a static overview. The Full Stack Elevator makes it explorable — an animated elevator moves between 8 floors (Physics through Swarms), and each floor has its own mini-interactive demo: toggle a transistor, wire an AND gate, schedule processes, compile code, drag an ML decision boundary, predict text like an LLM, run an agent's ReAct cycle, or race a swarm. The "aha moment" comes after visiting 3+ floors, when a callout reveals that every layer hides the complexity below — that's abstraction.

**Suggested placement:** After Page 3 (abstraction as superpower), a callout could say:
> "Ride the elevator yourself! The [Full Stack Elevator](../interactive/full_stack_elevator.html) lets you explore all 8 layers of computing — each floor has a hands-on demo."

**Floors:**
- Floor 1 — Physics: Transistor ON/OFF toggle with electron flow animation
- Floor 2 — Hardware: AND gate with interactive truth table
- Floor 3 — Operating Systems: Round-robin process scheduler
- Floor 4 — Programming Languages: Mini code editor with Python/Assembly/Binary comparison
- Floor 5 — Machine Learning: Draggable decision boundary on 2D data
- Floor 6 — Large Language Models: Text completion widget with probabilities
- Floor 7 — Agents: Animated ReAct (Think/Act/Observe) cycle
- Floor 8 — Swarms: Parallel vs sequential agent race with live timers

---

## Index Page

**File:** `interactive/index.html`

A landing page with cards linking to all 10 labs, color-coded to match their companion issues. Can be linked from the series' main navigation or shared as an entry point.
