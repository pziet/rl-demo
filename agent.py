import random
import pickle

class QAgent:
    def __init__(self, symbol, epsilon=0.1, alpha=0.5, gamma=0.9, epsilon_decay=None):
        self.q = {}
        self.symbol = symbol
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon_decay = epsilon_decay

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def decay_epsilon(self):
        if self.epsilon_decay:
            self.epsilon *= self.epsilon_decay
            if self.epsilon < 0.01:
                self.epsilon = 0.01

    @staticmethod
    def available_actions_from_state(state):
        return [i for i, v in enumerate(state) if v == 0]

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
            actions = self.available_actions_from_state(next_state)
            if actions:
                next_max = max(self.get_q(next_state, a) for a in actions)
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


class HumanAgent:
    """Simple agent that queries the user for moves."""

    def choose_action(self, env, explore=True):  # explore flag ignored
        valid_actions = env.available_actions()
        while True:
            try:
                move = int(input(f"Choose your move {valid_actions}: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if move in valid_actions:
                return move
            print("Invalid move. Try again.")

    def update(self, *args, **kwargs):
        pass
