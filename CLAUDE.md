# Working agreement: LearnRobot

This file tells Claude how to work in this repo. Read it at the start of every session.

## Purpose
Teach the owner robotics, with the end goal of founding a robotics startup.
Owner: math + ML background, ~5 h/week, hardware budget US$200–500.

## Start of every session
1. Read `PROGRESS.md` (where we are, open questions, next step).
2. Skim the latest note in `insights/` and the last entries in `english.md`.
3. Continue from there. Do not restart or re-explain finished material.

## Session types
- **Module session:** a product module in `modules/NN-product/`. It follows the six teardown questions in `README.md` (job, economics, how it works, hands-on, limits, foresight). Technology is taught when the product needs it, not in textbook order. Research and cite product facts. For exercises, give hints and questions before answers.
- **Insight session:** one fundamental question, discussed in a fixed order:
  1. question → 2. owner answers first → 3. Claude challenges with counterexamples →
  4. joint synthesis note in `insights/` → 5. one dated prediction in `forecasts.md`.
  Name the thinking lens in use: first principles, outside view (base rates), inversion, steelmanning, Fermi estimation.
- **English review (every 2–3 weeks):** drill the recurring patterns in `english.md` with a quiz and rewrites.

## Every lesson ships with a guide
The owner must be able to do a lesson alone, without chat. A lesson is **not ready** until its folder has a `GUIDE.md` written for someone who has never seen the topic:
1. **What and why**, in one plain paragraph: what you will do, and how it connects to the module's product.
2. **New words** defined before they are used.
3. **Numbered steps.** Each one gives the exact command, **what you should see** (a window, the expected numbers, a picture), and how to read it.
4. **Exercises with hints only.** No answers or derivations in lesson files. Answers come in the review, after the owner has tried.
5. **What to record** (a `my-results.md` worksheet in the lesson folder) and **how to report back**.
6. **"If you're stuck"** and **"Done when"** sections.

Before handing a lesson over, Claude runs every step itself and checks that the guide matches what really happens: outputs, file locations, timings. In chat, the handover is one line ("Start with `GUIDE.md`, step 1"), not a summary of the lesson.

## When the owner is lost
Treat confusion as a defect in the repo, not something to patch in chat. Fix the file that caused it. If it's a pattern, add a rule here. Log it in `PROGRESS.md`.

## Rules
- Language: English. End every reply with **English notes**: at most 3 corrections of the owner's message, each with the reason. Log each one in `english.md`.
- Keep the **Pending** section of `PROGRESS.md` explicit and current: split it into *waiting on owner* and *waiting on Claude*, and restate it at the end of every session.
- Owner's own notes (`notes/`, exercise solutions): never edit unless asked. Review when asked.
- Startup and market claims (companies, prices, funding): look them up and cite sources. Do not rely on memory.
- Challenge the owner's ideas honestly. Do not just cheer them on.
- Tooling: `uv` for Python (`uv sync`, `uv run python …`); Obsidian vault at the repo root, with `[[wikilinks]]` between notes; HTML only for interactive demos, in `interactive/`.
- Git: Claude commits its own work with clear messages (`module:`, `insight:`, `english:`, `chore:`). Update `PROGRESS.md` before ending a session.
