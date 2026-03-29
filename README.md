# From Turing to LLMs and Beyond

An educational comic series that tells the story of computing from 1936 to 2026 — and imagines what comes next.

**Live at [hexley.dev](https://hexley.dev/turing_to_llms/)**

## What's here

- **10-issue comic series** — from Turing's paper tape to modern AI, each issue a self-contained HTML comic with AI-generated art and inline SVG diagrams
- **16 interactive labs** — hands-on explorations (build a Turing machine, train a neural net, etc.)
- **Future Canvas** — concept art exploring four futures worth building: discovery, learning, sustainability, exploration
- **Behind-the-scenes documentary** — how the series was made, including the multi-agent pipeline, character design process, and lessons learned

## How it's made

The series is produced by a constellation of AI agents orchestrated through [Claude Code](https://claude.com/product/claude-code):

- **Writer, Editor, Red Team** — content creation and review
- **Layout Designer** — panel composition and image prompts
- **CREA Critic** — challenges concepts before committing to generation
- **Science Educator** — connects breakthroughs into narrative threads
- **Visual Reviewer** — screenshot-based rendering quality checks

Art generated with [FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev) running on DGX Spark, quality-scored with [PickScore](https://github.com/yuvalkirstain/PickScore) and HPSv2.

## Repo structure

```
turing_to_llms/
  issues/
    v1/ ... v2/          Published comic versions
    staging/             Active workspace
  experiments/           Visual style explorations + Future Canvas concept art
  documentary/           Behind-the-scenes site
  interactive/           16 interactive labs
  illustrations/         Standalone illustrations
```

The production pipeline (scripts, agents, prompts) lives in a separate workflow repo.

## Philosophy

We believe understanding computing matters — not just using it. This series exists to educate the next generation about how we got here and to inspire them to build what comes next. We don't end at "here's how LLMs work." We end with a vision of the future worth building.

Read more: [Why We Build](https://hexley.dev/turing_to_llms/documentary/why_we_build.html)
