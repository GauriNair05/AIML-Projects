# CartPole Reinforcement Learning Agent (PPO)

A reinforcement learning agent trained to solve the classic *CartPole-v1* control problem using *Proximal Policy Optimization (PPO)* from Stable-Baselines3.

---

## Overview

CartPole is a classic control benchmark from OpenAI Gym / Gymnasium. The goal is to balance a pole on a moving cart by applying left/right forces, keeping the pole upright for as long as possible.

This project trains a PPO agent to solve the environment, evaluates its performance, and visualizes the trained policy in action.

| | |
|---|---|
| *Environment* | CartPole-v1 (Gymnasium) |
| *Algorithm* | PPO (Proximal Policy Optimization) |
| *Library* | Stable-Baselines3 |
| *Training steps* | 100,000 timesteps |
| *Max episode reward* | 500 |
| *Platform* | Google Colab (CPU) |

---

## Problem Setup

*State space (4 continuous values):*
- Cart position
- Cart velocity
- Pole angle
- Pole angular velocity

*Action space (2 discrete actions):*
- Push cart left
- Push cart right

*Reward:* +1 for every timestep the pole remains upright. An episode ends when the pole falls past a threshold angle, the cart moves out of bounds, or 500 timesteps are reached.

*Solved criterion:* Average reward ≥ 475 over 100 consecutive episodes (per Gymnasium's definition). A mean reward close to 500 during evaluation indicates a fully trained agent.

---


## Results

| Metric | Value |
|---|---|
| Mean evaluation reward | ~500.00 |
| Standard deviation | ~0.00 |
| Training time (Colab CPU) | ~2–5 minutes |
| Episodes to convergence | ~200–400 |


---

## Key Design Choices

- *PPO* was chosen over DQN for its stability, ease of tuning, and strong out-of-the-box performance on low-dimensional control tasks.
- *Vectorized environments* (n_envs=4) were used to collect experience in parallel, significantly reducing wall-clock training time.
- *Deterministic evaluation* (deterministic=True) is used at test time to assess the agent's learned policy without exploration noise.

---

## Tech Stack

- Python
- [Gymnasium](https://gymnasium.farama.org/)
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- PyTorch (backend for SB3)
- imageio (video rendering)

---

## Future Improvements

- Extend to harder control environments (e.g. LunarLander-v3, BipedalWalker)
- Compare PPO against DQN and A2C on the same environment
- Add TensorBoard logging for training curve visualization
- Hyperparameter tuning via Optuna
