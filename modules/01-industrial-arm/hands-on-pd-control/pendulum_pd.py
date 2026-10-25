"""
Module 1 hands-on: control a simulated pendulum with a PD controller in MuJoCo.

Run:
    uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py          # headless: prints, saves a plot
    uv run python modules/01-industrial-arm/hands-on-pd-control/pendulum_pd.py --view   # interactive 3D viewer

Start with GUIDE.md in this folder: it walks you through what to run and what to look for.
"""
import sys
from pathlib import Path
import numpy as np
import mujoco

# --- The robot, described in MJCF (MuJoCo's XML format) -------------------
# One hinge joint, a 0.5 m rod with a 1 kg mass on the end, and a motor.
XML = """
<mujoco>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light pos="0 0 3"/>
    <geom type="plane" size="2 2 0.1" rgba=".9 .9 .9 1"/>
    <body name="pole" pos="0 0 1.2">
      <joint name="hinge" type="hinge" axis="0 1 0" damping="0.05"/>
      <geom type="capsule" fromto="0 0 0 0 0 -0.5" size="0.02" mass="0.0"/>
      <geom type="sphere" pos="0 0 -0.5" size="0.06" mass="1.0" rgba=".8 .2 .2 1"/>
    </body>
  </worldbody>
  <actuator>
    <motor name="torque" joint="hinge" gear="1"/>
  </actuator>
</mujoco>
"""

# --- Controller parameters (play with these) ------------------------------
TARGET = np.deg2rad(90)   # target angle: pole horizontal
KP = 50.0                 # proportional gain  [N*m / rad]
KD = 5.0                  # derivative gain    [N*m / (rad/s)]
TORQUE_LIMIT = 20.0       # real motors saturate! [N*m]
GRAVITY_COMP = False      # exercise 4
SIM_SECONDS = 3.0

M, G, L = 1.0, 9.81, 0.5


def controller(q, qdot):
    """PD control: push toward the target, resist velocity."""
    error = TARGET - q
    tau = KP * error - KD * qdot
    if GRAVITY_COMP:
        tau += M * G * L * np.sin(q)
    return float(np.clip(tau, -TORQUE_LIMIT, TORQUE_LIMIT))


def main():
    model = mujoco.MjModel.from_xml_string(XML)
    data = mujoco.MjData(model)

    log_t, log_q, log_tau = [], [], []

    def step():
        q, qdot = data.qpos[0], data.qvel[0]
        data.ctrl[0] = controller(q, qdot)
        mujoco.mj_step(model, data)
        log_t.append(data.time); log_q.append(q); log_tau.append(data.ctrl[0])

    if "--view" in sys.argv:
        print("Viewer open. It runs 30 simulated seconds, then closes and saves the plot.")
        import time
        from mujoco import viewer as mj_viewer
        with mj_viewer.launch_passive(model, data) as viewer:
            while viewer.is_running() and data.time < 30:
                step()
                viewer.sync()
                time.sleep(model.opt.timestep)
    else:
        while data.time < SIM_SECONDS:
            step()

    q_final = np.rad2deg(log_q[-1])
    print(f"target = {np.rad2deg(TARGET):.1f} deg, final = {q_final:.1f} deg, "
          f"steady-state error = {np.rad2deg(TARGET) - q_final:.2f} deg")
    print(f"max torque used = {max(abs(t) for t in log_tau):.1f} N*m")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(2, 1, sharex=True, figsize=(7, 5))
        ax[0].plot(log_t, np.rad2deg(log_q)); ax[0].axhline(np.rad2deg(TARGET), ls="--", c="gray")
        ax[0].set_ylabel("angle [deg]")
        ax[1].plot(log_t, log_tau); ax[1].set_ylabel("torque [N*m]"); ax[1].set_xlabel("time [s]")
        out = Path(__file__).with_name("pendulum_pd.png")   # saved next to this script
        fig.tight_layout(); fig.savefig(out, dpi=120)
        print(f"saved plot -> {out}")
    except ImportError:
        print("(install matplotlib to get a plot)")


if __name__ == "__main__":
    main()
