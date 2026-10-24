# LearnRobot

Learning robotics with the goal of founding a robotics startup.

**Profile:** math + ML background · ~5 h/week · hardware budget US$200–500
**Working thesis:** AI is getting very good at bits; the open opportunity is AI that acts in the physical world.

## How this repo works

Open this folder as an **Obsidian vault**. Set up Python once with `uv sync`, then run any module code with `uv run python <script>`.

- [[CLAUDE]]: our working agreement (session types, rules)
- [[PROGRESS]]: where we are and what's next
- `modules/NN-product/`: product modules (a teardown plus hands-on work)
- `insights/`: first-principles insight sessions
- [[forecasts]]: dated predictions, checked later for calibration
- [[startup-ideas]]: opportunities, theses and doubts
- [[english]]: English corrections log
- `notes/`: your own notes (Claude doesn't edit these)
- `interactive/`: HTML demos (open in a browser)

## Learning path: products first, technology on demand

Each module takes **one real product** and asks the same six questions:

1. **Job:** what work does it do, and who pays for it?
2. **Economics:** what does it cost compared with a human doing the job? Why do customers buy it, or not?
3. **How it works:** its stack, from perception and policy down to control and hardware.
4. **Hands-on:** a small simulation, or later a real arm, that rebuilds the hardest part. This is where the technology lives.
5. **Limits:** what breaks it today, and what would make it 10× better.
6. **Foresight:** one dated prediction for [[forecasts]].

Product facts (companies, prices, deployments) are researched and cited in each module. A module takes about 2–3 weeks at ~5 h/week.

The sequence moves from *tool* to *tool-user* (see [[01-what-is-a-robot]]) and stays centred on AI plus robot arms.

| # | Product (type) | Why it's here | Technology pulled in |
|---|---|---|---|
| 1 | **Industrial arm** (welding / assembly) | The baseline: why classic automation works and where it stops | Kinematics, PD control |
| 2 | **Warehouse picking robot** | The first big market for "coping with variability" | Perception, grasp planning, suction vs. fingers |
| 3 | **Soft grippers for food and produce** | The material does the control work | Compliance, soft mechanics |
| 4 | **Robot foundation models** (VLA companies) | The bet on general intelligence | Imitation learning, data collection, VLAs |
| 5 | **Humanoids** | Open tension: tool use vs. cost | Locomotion; steelman vs. critique |
| 6 | **Teleoperated and surgical robots** | Autonomy as a dial, and a business model | Teleoperation, shared autonomy |
| 7 | **Your own prototype** (SO-101 arm) | A product thesis, tested on real hardware | Everything above, on a real arm |

Insight sessions run alongside the modules, with questions drawn from the products.

## Hardware plan

Stay in simulation through Modules 1–3. Order a **leader–follower pair of SO-101 arms** (open-source, from Hugging Face LeRobot) around Module 4, when imitation learning needs real demonstrations. Check current prices when ordering; the rough estimate was US$250–350 for the pair.

## Progress
See [[PROGRESS]].
