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

    def render(self, use_emoji=False):
        """Pretty print the board.

        Empty squares show their numeric position so users know which
        value to enter for a move.

        Parameters
        ----------
        use_emoji : bool, optional
            If ``True`` render X and O as emoji for a more colourful board.
        """

        if use_emoji:
            symbols = {self.PLAYER_X: "❌", self.PLAYER_O: "⭕"}
        else:
            symbols = {self.PLAYER_X: 'X', self.PLAYER_O: 'O'}

        digit_emoji = [
            "0️⃣",
            "1️⃣",
            "2️⃣",
            "3️⃣",
            "4️⃣",
            "5️⃣",
            "6️⃣",
            "7️⃣",
            "8️⃣",
        ]

        display = []
        for i, value in enumerate(self.board):
            if value == self.EMPTY:
                display.append(digit_emoji[i] if use_emoji else str(i))
            else:
                display.append(symbols[value])

        for row in range(3):
            start = row * 3
            cells = display[start:start + 3]
            print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
            if row < 2:
                print("---+---+---")
