from tictactoe import TicTacToe
from agent import QAgent, RandomAgent


def train(episodes=5000, save_path='q_table.pkl', verbose=True, log_interval=500):
    env = TicTacToe()
    agent = QAgent(env.PLAYER_X)
    opponent = RandomAgent()

    wins = losses = draws = 0

    for episode in range(1, episodes + 1):
        state = env.reset()
        done = False
        winner = None

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

        if winner == agent.symbol:
            wins += 1
        elif winner == env.PLAYER_O:
            losses += 1
        else:
            draws += 1

        if verbose and episode % log_interval == 0:
            total = wins + losses + draws
            win_rate = wins / total if total else 0
            print(
                f"Episode {episode}/{episodes} - "
                f"Wins: {wins}, Losses: {losses}, Draws: {draws}, "
                f"Win rate: {win_rate:.2f}, Q-table size: {len(agent.q)}"
            )

    agent.save(save_path)
    print(f"Trained agent saved to {save_path}")


if __name__ == "__main__":
    train()
