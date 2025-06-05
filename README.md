# RL Demo: Tic Tac Toe

This repo contains a minimal reinforcement learning demo for Tic Tac Toe.
It uses a simple Q-learning agent.

## Training

Run `train.py` to train the agent against a random opponent:

```bash
python train.py
```

This creates `q_table.pkl` which stores the learned Q-values.

## Playing

Use `play.py` to play games between agents of different abilities. The `--x` and `--o` options select the type of agent playing as X and O:

- `trained` &ndash; load Q-values from `q_table.pkl`
- `untrained` &ndash; fresh Q-learning agent (acts mostly randomly)
- `random` &ndash; completely random moves

Example: play a trained X against an untrained O:

```bash
python play.py --x trained --o untrained
```
