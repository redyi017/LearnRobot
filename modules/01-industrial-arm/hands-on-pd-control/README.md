# Module 1 hands-on: the robot stack, and why control ≠ prediction

Part of [[modules/01-industrial-arm/README|Module 1: Industrial arm]].

> **To do this lesson, follow [[modules/01-industrial-arm/hands-on-pd-control/GUIDE|GUIDE]].** This README is background reading: the bigger picture behind the exercise.

**Time:** ~5 h · **Goal:** a mental map of a robot system, and first contact with the physics you can't skip.

## 1. The stack (≈30 min)

Every robot runs the same loop, many times per second:

```
 sensors ──► PERCEPTION ──► STATE ESTIMATION ──► PLANNING / POLICY ──► CONTROL ──► ACTUATORS
 (camera,     "what's          "where am I,         "what should I       "what torque     (motors,
  encoders,    there?"          where is it,         do next?"            right now?"      grippers)
  IMU, force)                   how fast?"
     ▲                                                                                          │
     └──────────────────────────────── the physical world ◄────────────────────────────────────┘
```

Each layer runs at a different speed:

| Layer | Typical rate | Classic approach | Learning-based approach |
|------|------|------|------|
| Perception | 10–30 Hz | geometric CV | CNNs / ViTs, foundation vision models |
| Planning / policy | 1–50 Hz | search, optimization | RL, imitation learning, VLAs |
| Control | 100–1000+ Hz | PID, MPC, impedance control | rarely learned; usually stays classical |

**The key idea for an ML person:** recent "AI robotics" mostly *replaces the middle* (perception plus planning/policy) with learned models. The bottom (control, actuators, physics) is still classical engineering, and it is where demos break. A policy can output a perfect target, and the arm still oscillates, saturates, or crushes the object.

## 2. Why control isn't prediction (≈30 min)

In supervised learning, a bad prediction is just a bad number. In robotics:
- **Your outputs change your future inputs.** The system is closed-loop, errors compound, and the data distribution shifts as you act (this comes back as *covariate shift* in imitation learning, Module 4).
- **Physics fights back.** Gravity, inertia, friction, and actuators with torque limits.
- **Time matters.** A correct action 100 ms late can be a wrong action.

The simplest controller is **PD control**: τ = Kp·(target − q) − Kd·q̇. Kp is a spring pulling toward the target, and Kd is a damper resisting motion. Most of what you need to know about control at first is in that one line.

## 3. Build: control a pendulum in MuJoCo (≈3 h)

MuJoCo is the physics simulator most robot-learning research uses (free, by Google DeepMind).

From the repo root:
```bash
uv sync                                                    # first time only
uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py         # headless: prints results, saves pendulum_pd.png
uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py --view  # 3D viewer (Ctrl + right-drag to push the pole)
```

Read the whole script first (~100 lines). Note how the robot is defined in XML (MJCF); you'll write these for arms later.

Exercises (edit the constants at the top, re-run, look at the plot):
1. **`KD = 0`.** What happens, and why? *(Hint: what removes energy from the system?)*
2. **`KP = 500`.** Does it get better? Look at the torque plot. What would a real motor do?
3. **`TORQUE_LIMIT = 2.0`.** Can it still reach 90°? Work out the torque gravity needs at 90° (m·g·l).
4. **Default settings leave a ~5.6° steady-state error.** Where does it come from? Derive it, then set `GRAVITY_COMP = True` and see what changes.
5. **Stretch:** replace the PD controller with a tiny neural net and train it any way you like (random search, CMA-ES, a few lines of PPO) to swing the pendulum from hanging down (q=0) to *upright* (q=180°). Compare how much effort that takes with how easy the hand-written controller was. That trade-off between learned and engineered control is a theme of the whole course.

## 4. Watch / read (≈1 h, pick some)
- MuJoCo documentation, "Overview" and "Modeling" chapters: mujoco.readthedocs.io
- Russ Tedrake, *Underactuated Robotics* (MIT, free online), chapter 1. Dense, but the best course on this material, and it suits a math background.
- Any 10-minute "PID controller explained" video, for intuition

## 5. Startup reflection (≈20 min) → write in [[startup-ideas]]
- In the stack diagram, which layer do you think is the *bottleneck* for robots doing useful work today: perception, policy, control, or hardware? Write down a guess now; we'll revisit it in Module 4.
