# Lunar Lander Reinforcement Learning Agent (PPO)

A reinforcement learning agent trained to solve the *LunarLander-v3* environment using *Proximal Policy Optimization (PPO)* from Stable-Baselines3.

---

## Overview

Lunar Lander is a classic continuous-control benchmark from Gymnasium's Box2D suite. The goal is to safely guide a lander to touch down between two flags on the moon's surface by firing directional thrusters, balancing fuel efficiency against a soft, centered landing.

This project trains a PPO agent to solve the environment and evaluates its performance against Gymnasium's defined "solved" threshold.

| | |
|---|---|
| *Environment* | LunarLander-v3 (Gymnasium, Box2D) |
| *Algorithm* | PPO (Proximal Policy Optimization) |
| *Library* | Stable-Baselines3 |
| *Training steps* | 1,000,000 timesteps |
| *Solved threshold* | Mean reward ≥ 200 |
| *Platform* | Google Colab (CPU) |

---

## Problem Setup

*State space (8 continuous values):*
- Lander x, y position
- Lander x, y linear velocity
- Lander angle
- Lander angular velocity
- Left leg ground contact (boolean)
- Right leg ground contact (boolean)

*Action space (4 discrete actions):*
- Do nothing
- Fire left orientation engine
- Fire main engine
- Fire right orientation engine

*Reward shaping:*
- Positive reward for moving toward and landing on the pad
- Positive reward for each leg in contact with the ground
- Negative reward for firing the main engine (fuel cost) and side engines
- Large penalty (-100) for crashing; large bonus (+100) for a safe landing

*Solved criterion:* An average reward of 200 or higher over 100 consecutive episodes.

---

## Results

| Metric | Value |
|---|---|
| Mean evaluation reward | ~235.31 +/- 66.03 |
| Training time (Colab CPU) | ~15–30 minutes |
| Timesteps to convergence | ~600,000–1,000,000 |

---

## Key Design Choices

- *PPO* was chosen for its stability on both discrete and continuous-observation environments, and its strong track record on LunarLander as a benchmark.
- *8 parallel environments* were used during training to increase sample throughput, given the environment's heavier physics simulation compared to simpler control tasks.
- *Extended training horizon* (1M timesteps vs. CartPole's 100k) was necessary due to sparse, delayed reward signals — the agent only receives strong feedback on landing outcome at the end of each episode, making credit assignment harder.
- *Hyperparameters tuned for LunarLander* (higher gamma, gae_lambda, and entropy coefficient) to encourage longer-horizon planning and sufficient exploration, since default PPO settings tend to underperform on this environment.

---

## Challenges Encountered

- *Sparse rewards*: unlike CartPole's dense per-timestep signal, Lunar Lander only reveals success/failure at episode end, requiring significantly more training to converge.
- *Environment setup friction*: LunarLander depends on Box2D physics (box2d-py), which requires swig and can be inconsistent to install in hosted notebook environments.
- *Longer training time*: heavier per-step computation and a harder exploration problem make this a CPU-bound, patience-testing training run compared to simpler control tasks.

---

## Tech Stack

- Gymnasium (Box2D)
- Stable-Baselines3
- PyTorch (backend for SB3)

---

## Future Improvements

- Compare PPO against DQN and A2C on the same environment
- Add TensorBoard logging to visualize the training/reward curve
- Hyperparameter tuning via Optuna for faster convergence
- Extend to the continuous-action variant (LunarLanderContinuous-v3) using SAC or TD3
