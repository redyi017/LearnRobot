# Guide: Module 1, Part A: holding a robot joint in place

Part of [[modules/01-industrial-arm/README|Module 1: Industrial arm]]. Background reading: [[modules/01-industrial-arm/hands-on-pd-control/README|README]] (optional; this guide is enough).

**Time:** about 2–2.5 hours, which you can split across days. **You need:** this repo, and a terminal open in the repo folder.

## What you'll do, and why

An industrial arm is a chain of joints, and each joint has a motor. The most basic job of every joint, done hundreds of times a second, is: *"go to this angle and stay there, even though gravity pulls you down."* If that fails, nothing else the robot does can work.

You'll study this job on the simplest robot possible: **one joint**. A rod hangs from a hinge, has a 1 kg ball on the end, and a motor at the top. The motor's task is to lift the rod to horizontal (90°) and hold it there. Nothing physical moves: **MuJoCo**, a physics simulator, calculates how the real thing would move.

You'll change the motor's settings, run the simulation, and explain what you see.

## New words (read once)

| Word | Meaning |
|---|---|
| **angle `q`** | Where the rod points. 0° = hanging straight down, 90° = horizontal. |
| **velocity `q̇` ("q-dot")** | How fast the angle is changing. |
| **torque `τ` ("tau")** | The motor's twisting force, in N·m. More torque = harder push. |
| **controller** | The rule that decides the torque from what the robot senses. Here it's 5 lines of Python. |
| **PD control** | The rule used here: `τ = KP × (target − q) − KD × q̇`. |
| **KP** | "Spring strength": the further the rod is from the target, the harder the motor pulls toward it. |
| **KD** | "Shock absorber": the faster the rod moves, the more the motor resists the motion. |
| **torque limit** | The most torque the motor can produce. Real motors have one. |
| **steady-state error** | How far from the target the rod ends up once it stops moving. |

## Step 1: Watch it (≈15 min)

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

## Step 2: Read the plot (≈15 min)

After each run, the program prints two lines and saves a picture **next to the script**, `modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.png`. Open it. (Each run overwrites it, so to keep one, copy it under a new name.)

For a quicker run without the window, leave out `--view`. It simulates only 3 seconds and takes a moment:

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

**Questions to answer in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]:**
1. In the first fraction of a second the torque is flat at 20. Why flat, and not higher?
2. Why does the torque briefly go negative?
3. At the end the rod isn't moving, yet the motor still applies about 5 N·m. What is that torque doing?

## Step 3: Read the code (≈20 min)

Open `pendulum_pd.py`. It has four parts. You only need to understand them roughly:

| Part | What it is |
|---|---|
| `XML = """…"""` | **The robot's body**: the hinge, the rod, the ball (1 kg), and the motor. |
| Constants (`TARGET`, `KP`, `KD`, `TORQUE_LIMIT`, `GRAVITY_COMP`) | **The knobs you'll change** in Step 4. |
| `def controller(q, qdot)` | **The robot's brain**: the PD rule. Read these 5 lines carefully. |
| `def step()` inside `main()` | **The robot loop**: *sense* (`q`, `qdot`) → *decide* (`controller`) → *act* (`data.ctrl`) → *physics moves forward 0.002 s* (`mj_step`). It runs 500 times per simulated second. |

That sense → decide → act loop is the same loop every robot runs, from this pendulum to a humanoid. Only the "decide" part gets more complicated.

**Write down** one sentence in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]: in your own words, what does `controller()` do?

## Step 4: Experiments (≈1–1.5 h)

For each experiment, follow the same routine:

1. **Predict first.** Before running, write in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]] what you expect to happen. A wrong prediction teaches you the most.
2. Change **one** constant at the top of `pendulum_pd.py` and save the file.
3. Run it (without `--view` is faster; add `--view` if you want to watch).
4. Look at the plot, not just the printed numbers.
5. Write down what happened and **why** you think it happened.
6. **Put the constant back** to its original value before the next experiment.

| # | Change | Look at | Hint (not the answer) |
|---|---|---|---|
| 1 | `KD = 0.0` (was `5.0`) | The angle curve's shape. Ignore "final". | What takes energy out of a swinging system? |
| 2 | `KP = 500.0` (was `50.0`) | Steady-state error, and the torque panel | Did the error shrink? How much of the time does the motor sit at its limit? Would a real motor like that? |
| 3 | `TORQUE_LIMIT = 2.0` (was `20.0`) | Does the rod get anywhere near 90°? | How much torque does gravity create when the rod is horizontal? Torque = force × lever arm, with a 1 kg ball on a 0.5 m rod. |
| 4 | Defaults, then `GRAVITY_COMP = True` | The ~5.6° steady-state error, then the same run with the setting on | When the rod is still, the motor's torque must exactly balance gravity's. Write that as an equation using the PD rule, and solve for the error. Then read what `GRAVITY_COMP` adds in `controller()`. |
| 5 | *(optional stretch)* | — | Replace `controller()` with a tiny neural net, and train it to swing the rod from hanging (0°) to straight up (180°). See README §3. |

## Step 5: Report back

1. Fill in [[modules/01-industrial-arm/hands-on-pd-control/my-results|my-results]]. Rough notes are fine. Wrong guesses are useful, so leave them in.
2. Tell Claude in chat: *"Part A done"*, plus the one thing that surprised you most.
3. Claude then reviews your answers, explains anything you missed (including the full answers), and you move on to **Part B: multi-joint arm kinematics**.

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
- [ ] You answered the three plot questions in Step 2
- [ ] You ran experiments 1–4, each with a prediction and an explanation
- [ ] You reported back to Claude
