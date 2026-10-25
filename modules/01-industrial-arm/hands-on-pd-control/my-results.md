# My results: Module 1, Part A

Your file. Claude won't edit it, only reads it when reviewing. Rough notes are fine. Follow [[modules/01-industrial-arm/hands-on-pd-control/GUIDE|GUIDE]].

## Step 1: Watching
- What the motion looked like:
- What surprised me:

## Step 2: The plot
1. Why is the torque flat at 20 at the start?
2. Why does the torque go negative?
3. What is the ~5 N·m at the end doing?

## Step 3: The code
- `controller()` in my own words:

## Step 4: Experiments

### 1. `KD = 0.0`
- Prediction:
- What happened:
- Why I think so:

### 2. `KP = 500.0`
- Prediction:
- What happened:
- Why I think so:

### 3. `TORQUE_LIMIT = 2.0`
- Prediction:
- What happened:
- Why I think so (torque needed at 90° = ?):

### 4. Steady-state error, then `GRAVITY_COMP = True`
- My equation for the ~5.6° error:
- What happened with gravity compensation:
- Why I think so:

### 5. (optional) Neural-net controller
-

## Most surprising thing

## Questions for Claude
