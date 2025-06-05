from tictactoe import TicTacToe
from agent import QAgent, RandomAgent


def train(episodes=5000, save_path='q_table.pkl'):
    env = TicTacToe()
    agent = QAgent(env.PLAYER_X)
    opponent = RandomAgent()
    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            if env.current_player == agent.symbol:
                action = agent.choose_action(env)
                next_state, reward, done, winner = env.step(action)
                agent.update(state, action, reward, next_state, done)
            else:
                action = opponent.choose_action(env)
                next_state, reward, done, winner = env.step(action)
                agent.update(state, action, -reward, next_state, done)
            state = next_state
    agent.save(save_path)
    print(f"Trained agent saved to {save_path}")


if __name__ == "__main__":
    train()
