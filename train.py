import argparse
from tictactoe import TicTacToe
from agent import QAgent, RandomAgent


def train(
    episodes=5000,
    save_path="q_table.pkl",
    verbose=True,
    log_interval=500,
    epsilon_decay=None,
    opponent="random",
):
    env = TicTacToe()
    agent = QAgent(env.PLAYER_X, epsilon_decay=epsilon_decay)
    if opponent == "self":
        opponent_agent = QAgent(env.PLAYER_O, epsilon_decay=epsilon_decay)
    else:
        opponent_agent = RandomAgent()

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
                action = opponent_agent.choose_action(env)
                next_state, reward, done, winner = env.step(action)
                if isinstance(opponent_agent, QAgent):
                    opponent_agent.update(state, action, reward, next_state, done)
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

        agent.decay_epsilon()
        if isinstance(opponent_agent, QAgent):
            opponent_agent.decay_epsilon()

    agent.save(save_path)
    print(f"Trained agent saved to {save_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=5000)
    parser.add_argument("--save-path", default="q_table.pkl")
    parser.add_argument("--log-interval", type=int, default=500)
    parser.add_argument("--epsilon-decay", type=float, default=0.999)
    parser.add_argument("--opponent", choices=["random", "self"], default="random")
    parser.add_argument("--no-verbose", dest="verbose", action="store_false")
    args = parser.parse_args()
    train(
        episodes=args.episodes,
        save_path=args.save_path,
        verbose=args.verbose,
        log_interval=args.log_interval,
        epsilon_decay=args.epsilon_decay,
        opponent=args.opponent,
    )


if __name__ == "__main__":
    main()
