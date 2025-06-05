import random
import pickle

class QAgent:
    def __init__(self, symbol, epsilon=0.1, alpha=0.5, gamma=0.9):
        self.q = {}
        self.symbol = symbol
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def choose_action(self, env, explore=True):
        actions = env.available_actions()
        if explore and random.random() < self.epsilon:
            return random.choice(actions)
        qs = [self.get_q(tuple(env.board), a) for a in actions]
        max_q = max(qs)
        best_actions = [a for a, q in zip(actions, qs) if q == max_q]
        return random.choice(best_actions)

    def update(self, state, action, reward, next_state, done):
        old_q = self.get_q(state, action)
        next_max = 0
        if not done:
            next_actions = [self.get_q(next_state, a) for a in range(9)]
            next_max = max(next_actions)
        new_q = old_q + self.alpha * (reward + self.gamma * next_max - old_q)
        self.q[(state, action)] = new_q

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.q, f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.q = pickle.load(f)

class RandomAgent:
    def __init__(self):
        pass

    def choose_action(self, env, explore=True):
        return random.choice(env.available_actions())

    def update(self, *args, **kwargs):
        pass
