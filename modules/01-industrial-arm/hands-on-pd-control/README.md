# Background: the robot stack, and why control ≠ prediction

Part of [[modules/01-industrial-arm/README|Module 1: Industrial arm]], hands-on Part A.

> **To do this lesson, follow [[modules/01-industrial-arm/hands-on-pd-control/GUIDE|GUIDE]].** It tells you when to read this page (Step 3). This page is background only: the steps, exercises and questions all live in the guide.

## 1. The stack

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

## 2. Why control isn't prediction

In supervised learning, a bad prediction is just a bad number. In robotics:
- **Your outputs change your future inputs.** The system is closed-loop, errors compound, and the data distribution shifts as you act (this comes back as *covariate shift* in imitation learning, Module 4).
- **Physics fights back.** Gravity, inertia, friction, and actuators with torque limits.
- **Time matters.** A correct action 100 ms late can be a wrong action.

The simplest controller is **PD control**: τ = Kp·(target − q) − Kd·q̇. Kp is a spring pulling toward the target, and Kd is a damper resisting motion. Most of what you need to know about control at first is in that one line.

## 3. Going further (optional)
- MuJoCo documentation, "Overview" and "Modeling" chapters: mujoco.readthedocs.io
- Russ Tedrake, *Underactuated Robotics* (MIT, free online), chapter 1. Dense, but the best course on this material, and it suits a math background.
- Any 10-minute "PID controller explained" video, for intuition
