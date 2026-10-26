---
date: 2026-10-09
status: in progress
lenses: [first principles]
---
# Insight 01: What is a robot?

## 1. Question
Define "robot". Then classify six edge cases.

## 2. Owner's answers (unedited)
- No clear definition yet.
- Dishwasher, thermostat → **not** robots
- Tesla with FSD → **robot**
- ChatGPT in a browser → **not**: "it is unable to control physical things"
- Venus flytrap → **not**: it's a creature
- da Vinci surgical system → **not**: a human controls it

## 3. Implicit definition (extracted by Claude from the answers)
The answers use four criteria, three of them stated and one hidden:

| Criterion | Excludes | Stated? |
|---|---|---|
| **Embodied:** acts on the physical world | ChatGPT-in-browser | yes |
| **Artificial:** made, not evolved | Venus flytrap | yes |
| **Autonomous:** the machine makes the decision, not a human | da Vinci | yes |
| **Copes with variability:** perceives an open, changing environment and chooses among many possible actions | dishwasher, thermostat | **hidden** |

Draft definition:
> A robot is an artificial system that perceives an open, changing physical environment and decides for itself how to act on it.

## 4. Challenges
- **The factory welding arm.** It repeats one programmed path without perceiving anything. Under the draft definition it is *not* a robot, yet it is the original "industrial robot", installed in the millions. Is the definition wrong, or is the industry's word covering two different things?
- **Autonomy as a dial.** FSD is supervised by a human, and da Vinci is fully teleoperated. Is autonomy a switch or a spectrum? Note that some new robot companies deliberately use teleoperation as a business strategy.
- **The Roomba.** It is embodied, artificial and autonomous, and it handles a messy home, but with very simple logic. Is it a robot?
- **The flytrap.** Functionally it is a thermostat: it senses touch, applies a fixed rule (two touches within seconds), and acts physically. Excluding it by *origin* rather than *function* is fine, but it shows that biology already solves "cheap, robust, physical decisions", which is the core idea behind soft robotics.

### Owner's responses (unedited)
1. "'machines that cope with variability' meets more my imagination. I think the 'variability' include opportunity. Just like human, different problems require different tools. Even robots replace the role of operating machines, robots still need different tools."
2. "da Vinci is controlled by human. Without human, it does not contain intelligence. I would not consider screwdriver or sophisticated watch as robot. Tesla with FSD, though supervised by human, is intelligent enough to drive."
3. Roomba: "Robot. Since it already shows enough intelligence."

## 5. Synthesis (draft v2)
**Two meanings of "robot".** The industry uses one word for two things:
- *Programmable automation*: the welding arm. Mature, installed in the millions, works in structured, controlled environments. It is a **tool**.
- *Machines that cope with variability*: the owner's meaning. The new frontier. It is a **tool-user**: it picks how to act, and with what tool, for each new problem.

**The criterion is intelligence, not independence.** Mechanical sophistication doesn't count (a watch is not a robot). Human supervision doesn't disqualify (FSD counts). What matters is whether the machine itself carries enough intelligence for the variability it faces. Autonomy is a dial, not a switch.

**Definition v2:**
> A robot is an artificial, embodied system with enough intelligence of its own to handle variable physical problems: choosing how to act, and with which tools. Human supervision does not disqualify it.

**Open tensions (carried forward):**
- *Where does the intelligence live?* With remote assistance and training on human data, intelligence is spread across the machine, the people, and the data. Does the customer care, as long as the job gets done?
- *Tool-use argues for humanoids.* If robots must use many different tools, and most existing tools are designed for human hands, that is the strongest argument for human-like hands, and possibly humanoids. That challenges the owner's earlier skepticism → [[startup-ideas]].
- *Is "enough" intelligence relative?* A thermostat's intelligence fully matches its near-zero variability. Is the real measure intelligence *relative to the variability of the task*?

## 6. Prediction
Skipped (2026-10-26): a definition question doesn't produce a natural bet. Predictions now come mainly from each module's Foresight question.

## Links
[[startup-ideas]] · [[forecasts]] · [[english]]
