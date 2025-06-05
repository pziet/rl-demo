class TicTacToe:
    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = -1

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [self.EMPTY] * 9
        self.current_player = self.PLAYER_X
        return tuple(self.board)

    def available_actions(self):
        return [i for i, v in enumerate(self.board) if v == self.EMPTY]

    def step(self, action):
        if self.board[action] != self.EMPTY:
            raise ValueError("Invalid action")
        self.board[action] = self.current_player
        winner = self.check_winner()
        done = winner is not None or not self.available_actions()
        reward = 0
        if done:
            if winner == self.current_player:
                reward = 1
            elif winner is None:
                reward = 0
            else:
                reward = -1
        self.current_player *= -1
        return tuple(self.board), reward, done, winner

    def check_winner(self):
        b = self.board
        lines = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for line in lines:
            total = b[line[0]] + b[line[1]] + b[line[2]]
            if total == 3:
                return self.PLAYER_X
            elif total == -3:
                return self.PLAYER_O
        return None

    def render(self):
        """Pretty print the board.

        Empty squares show their numeric position so users know which
        value to enter for a move.
        """

        symbols = {self.PLAYER_X: 'X', self.PLAYER_O: 'O'}

        display = []
        for i, value in enumerate(self.board):
            if value == self.EMPTY:
                display.append(str(i))
            else:
                display.append(symbols[value])

        for row in range(3):
            start = row * 3
            cells = display[start:start + 3]
            print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 2:
                print("---+---+---")
