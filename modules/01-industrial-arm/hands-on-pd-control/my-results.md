# My results: Module 1, Part A

Your file. Claude won't edit it, only reads it when reviewing. Write in English, in your own words. Rough notes are fine. Follow [[modules/01-industrial-arm/hands-on-pd-control/GUIDE|GUIDE]].

# Sitting 1

## Step 1: Watching
- What the motion looked like:
- What surprised me:

## Step 2: The plot
1. Why is the torque flat at 20 at the start?
2. Why does the torque go negative?
3. What is the ~5 N·m at the end doing?

## Step 3: The code and the stack
1. `controller()` in my own words:
2. Which stack layer is `controller()`? Which layers does the pendulum not have?

# Sitting 2

## Step 4: Experiments

### 1. `KD = 0.0` (first principles)
- Prediction:
- What happened:
- Why I think so:

### 2. `KP = 500.0` (inversion)
- Prediction:
- What happened:
- Why I think so:

### 3. `TORQUE_LIMIT = 2.0` (Fermi estimation)
- My estimate of the torque needed at 90°, before running:
- Prediction:
- What happened:
- Why I think so:

### 4. Steady-state error, then `GRAVITY_COMP = True` (first principles)
- My equation for the ~5.6° error:
- Prediction with gravity compensation:
- What happened:
- Why I think so:

### 5. `GRAVITY_COMP = True` with `PAYLOAD_MASS` = 2.0 / 0.5 / 5.0 (first principles)
- Prediction:
- What happened (error for each payload):
- Why I think so:

## Step 5: Back to the product
1. **Limits:** what a classic arm must know in advance, and what a factory must keep fixed:
2. **Tool vs. tool-user:** what the controller would need for an unknown payload, and which stack layer that adds:
3. **Economics (first guess):** how motor strength relates to an arm's price:
4. Bottleneck guess added to [[startup-ideas]]? (yes/no)

## Most surprising thing

## Questions for Claude
