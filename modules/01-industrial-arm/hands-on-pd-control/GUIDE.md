---
module: 1 (Industrial arm)
teardown question: 4 (Hands-on)
feeds: 3 (How it works), 5 (Limits), [[startup-ideas]]
time: ~3 h, in two sittings
---
# Guide: Module 1, Part A: how an arm holds a joint, and where that breaks

## Where this fits

**The learning design.** Each module takes one real product and answers six questions: job, economics, how it works, **hands-on**, limits, foresight (see [[README]]). This guide is the **hands-on** for [[modules/01-industrial-arm/README|Module 1: Industrial arm]]. You rebuild the product's most basic skill yourself, so that you can judge its limits from experience rather than from reading.

**The product question.** In [[01-what-is-a-robot]] you called the industrial arm a *tool*: it does a fixed job extremely well in a controlled factory, but it doesn't cope with variability. This lesson tests that claim. You'll build the controller that holds one joint of an arm in position. Then you'll change the world a little, the way a factory might, and watch what happens.

**What you'll do.** A simulated rod hangs from a hinge, with a ball (the "payload") on the end and a motor at the top. The motor must lift the rod to horizontal (90°) and hold it there. Nothing physical moves: **MuJoCo**, a physics simulator, calculates how the real thing would move. One joint of a 6-joint arm faces exactly this problem.

**What you'll come away with:**
- How every robot joint is held in place: the sense → decide → act loop, and PD control.
- Why a classic arm needs to know its world in advance.
- Your own evidence for Module 1's *Limits* section, and a first guess for [[startup-ideas]].

## New words (read once)

| Word | Meaning |
|---|---|
| **angle `q`** | Where the rod points. 0° = hanging straight down, 90° = horizontal. |
| **velocity `q̇` ("q-dot")** | How fast the angle is changing. |
| **torque `τ` ("tau")** | The motor's twisting force, in N·m. More torque = harder push. |
| **payload** | What the arm is holding. Here, the ball on the end of the rod. |
| **controller** | The rule that decides the torque from what the robot senses. Here it's a few lines of Python. |
| **PD control** | The rule used here: `τ = KP × (target − q) − KD × q̇`. |
| **KP** | "Spring strength": the further the rod is from the target, the harder the motor pulls toward it. |
| **KD** | "Shock absorber": the faster the rod moves, the more the motor resists the motion. |
| **torque limit** | The most torque the motor can produce. Bigger motors cost more. |
| **steady-state error** | How far from the target the rod ends up once it stops moving. |
| **model-based control** | A controller that uses built-in knowledge of the physics, such as "the payload weighs 1 kg". |

---

## Sitting 1 (≈1.5 h): how one joint is held

### Step 1: Watch it (≈15 min)

From the repo root, run:

```bash
uv sync
uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py --view
```

(`uv sync` is only needed the first time.)

**What you should see:** a 3D window with a grey floor and a red ball on a thin rod. The ball swings up quickly, overshoots slightly, and settles **a little below horizontal**. After 30 simulated seconds, the window closes by itself.

**Try this while it runs:**
- Drag with the left mouse button to rotate the camera, and scroll to zoom.
- **Double-click the red ball** to select it, then hold **Ctrl** and **right-drag** to pull it. Let go and watch the motor bring it back. Pull hard, and pull gently.

**Write down** in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]: what did the motion look like? Did anything surprise you?

### Step 2: Read the plot (≈15 min)

After each run, the program prints two lines and saves a picture **next to the script**, `modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.png`. Open it. (Each run overwrites it, so to keep one, copy it under a new name.)

For a quicker run without the window, leave out `--view`. It simulates only 3 seconds:

```bash
uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py
```

With the default settings, it prints:

```
target = 90.0 deg, final = 84.4 deg, steady-state error = 5.59 deg
max torque used = 20.0 N*m
```

![[modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.png]]

**How to read it:**
- **Top panel, angle over time.** The dashed line is the target (90°). The blue line is where the rod actually is.
- **Bottom panel, motor torque over time.** Positive = pushing the rod up; negative = pushing it down (braking).
- **"final"** is the angle at the very last instant. It only means something if the rod has stopped moving, so always check the plot before trusting it.

**Answer in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]:**
1. In the first fraction of a second the torque is flat at 20. Why flat, and not higher?
2. Why does the torque briefly go negative?
3. At the end the rod isn't moving, yet the motor still applies about 5 N·m. What is that torque doing?

### Step 3: Read the code, and place it in the robot (≈30 min)

Open `pendulum_pd.py`. It has four parts. You only need to understand them roughly:

| Part | What it is |
|---|---|
| `XML_TEMPLATE = """…"""` | **The robot's body**: the hinge, the rod, the ball, and the motor. |
| Constants (`TARGET`, `KP`, `KD`, `TORQUE_LIMIT`, `GRAVITY_COMP`, `PAYLOAD_MASS`) | **The knobs you'll change** in Sitting 2. |
| `def controller(q, qdot)` | **The robot's brain**: the PD rule. Read these lines carefully. |
| `def step()` inside `main()` | **The robot loop**: *sense* (`q`, `qdot`) → *decide* (`controller`) → *act* (`data.ctrl`) → *physics moves forward 0.002 s* (`mj_step`). It runs 500 times per simulated second. |

Now read **§1 "The stack"** and **§2 "Why control isn't prediction"** in the [[modules/01-industrial-arm/hands-on-pd-control/README|README]] (about 15 min). They show where this loop sits in a full robot.

**Answer in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]:**
1. In your own words, what does `controller()` do?
2. In the stack diagram, which layer is `controller()`? Which layers does this pendulum **not** have at all? (Teardown question 3: how an industrial arm works.)

---

## Sitting 2 (≈1.5 h): experiments, and back to the product

### Step 4: Experiments (≈1 h)

For each experiment, follow the same routine:

1. **Predict first.** Before running, write in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]] what you expect to happen. This is the same habit as [[forecasts]], on a small scale: a wrong prediction teaches you the most.
2. Change **one** constant at the top of `pendulum_pd.py` (unless the table says otherwise) and save the file.
3. Run it (without `--view` is faster; add `--view` if you want to watch).
4. Look at the plot, not just the printed numbers.
5. Write down what happened and **why** you think it happened.
6. **Put the constants back** to their original values before the next experiment.

Each experiment names the **thinking lens** it uses (the same lenses as in insight sessions).

| # | Change | Look at | Lens | Hint (not the answer) |
|---|---|---|---|---|
| 1 | `KD = 0.0` (was `5.0`) | The angle curve's shape. Ignore "final". | first principles | What takes energy out of a swinging system? |
| 2 | `KP = 500.0` (was `50.0`) | Steady-state error, and the torque panel | inversion: "how could a stronger setting make things worse?" | Did the error shrink? How much of the time does the motor sit at its limit? Would a real motor, and the part it's holding, like that? |
| 3 | `TORQUE_LIMIT = 2.0` (was `20.0`) | Does the rod get anywhere near 90°? | Fermi estimation | Estimate the torque gravity creates when the rod is horizontal: force × lever arm, with a 1 kg ball on a 0.5 m rod. Do the estimate **before** you run. |
| 4 | Defaults, then `GRAVITY_COMP = True` | The ~5.6° error, then the same run with the setting on | first principles | When the rod is still, the motor's torque must exactly balance gravity's. Write that as an equation using the PD rule, and solve for the error. Then read what `GRAVITY_COMP` adds in `controller()`. |
| 5 | Keep `GRAVITY_COMP = True`, then set `PAYLOAD_MASS` to `2.0`, then `0.5`, then `5.0` | The steady-state error for each payload | first principles | The controller still *believes* the payload is 1 kg (`M` in the code). What happens when the world no longer matches what the robot was programmed for? |

### Step 5: Back to the product (≈20 min)

This step turns the experiments into the module's teardown. Answer in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]:

1. **Limits (teardown question 5).** From experiment 5: what does a classic arm need to know in advance to hold a part precisely? What would a factory have to keep fixed to make that true?
2. **Tool vs. tool-user ([[01-what-is-a-robot]]).** What would this controller need to handle an *unknown* payload? Which layer of the stack would that add?
3. **Economics, as a first guess (teardown question 2).** Experiments 2 and 3 are about motor size. How do you think motor strength relates to an arm's price? Claude will check this against real data in the teardown.

Then add a dated entry to [[startup-ideas]]:

4. **Bottleneck guess.** Which layer of the stack (perception, policy, control, or hardware) do you think limits robots doing useful work today? One sentence, plus your reason. We'll revisit it in Module 4.

### Step 6: Report back

1. Make sure [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]] is filled in. Write in English, in your own words. Rough notes are fine, and wrong guesses are useful, so leave them in.
2. Tell Claude in chat: *"Part A done"*, plus the one thing that surprised you most.
3. **What happens next:**
   - Claude reviews your answers and explains anything you missed, including the full answers.
   - Claude corrects your English as usual.
   - Your Step 5 answers become the first draft of Module 1's *Limits* section.
   - You move on to **Part B: multi-joint arm kinematics**.

**Optional stretch** (no time limit): replace `controller()` with a tiny neural net, and train it to swing the rod from hanging (0°) to straight up (180°). Compare the effort with the hand-written controller. Learned vs. engineered control is the central question of Module 4.

---

## If you're stuck

| Problem | Try |
|---|---|
| `uv: command not found` | uv isn't installed or the terminal needs a restart. Tell Claude. |
| `ModuleNotFoundError: mujoco` | Run `uv sync` in the repo root, and use `uv run python …`, not plain `python`. |
| The window doesn't open | Run without `--view`. The plot alone is enough for every experiment. |
| My change had no effect | Did you save the file? Did you change the line at the top, not one in the comments? |
| I can't find the plot | It's next to the script, not in the repo root. The terminal prints the full path. |
| I don't understand a question | Write down what you do understand, and ask Claude. That counts as a result. |

## Done when

- [ ] You watched the viewer and pulled the ball at least once
- [ ] You answered the plot and code questions (Steps 2–3)
- [ ] You ran experiments 1–5, each with a prediction and an explanation
- [ ] You answered the product questions (Step 5) and added a bottleneck guess to [[startup-ideas]]
- [ ] You reported back to Claude
