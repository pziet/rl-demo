import argparse
from tictactoe import TicTacToe
from agent import QAgent, RandomAgent, HumanAgent


def load_agent(name, symbol):
    if name == 'trained':
        agent = QAgent(symbol)
        agent.load('q_table.pkl')
        return agent
    if name == 'untrained':
        return QAgent(symbol)
    if name == 'human':
        return HumanAgent()
    return RandomAgent()


def play_game(x_agent, o_agent, render=True):
    env = TicTacToe()
    env.reset()
    done = False
    while not done:
        if render:
            env.render()
            print()
        if env.current_player == env.PLAYER_X:
            action = x_agent.choose_action(env, explore=False)
        else:
            action = o_agent.choose_action(env, explore=False)
        state, reward, done, winner = env.step(action)
    if render:
        env.render()
    if winner == env.PLAYER_X:
        print("X wins!")
    elif winner == env.PLAYER_O:
        print("O wins!")
    else:
        print("Draw!")


def main():
    parser = argparse.ArgumentParser()
    choices = ['trained', 'untrained', 'random', 'human']
    parser.add_argument('--x', choices=choices, default='trained')
    parser.add_argument('--o', choices=choices, default='random')
    args = parser.parse_args()
    x_agent = load_agent(args.x, TicTacToe.PLAYER_X)
    o_agent = load_agent(args.o, TicTacToe.PLAYER_O)
    play_game(x_agent, o_agent)


if __name__ == '__main__':
    main()
