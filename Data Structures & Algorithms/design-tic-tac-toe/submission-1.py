class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0

    def increment_counts(self, r: int, c: int, player: int) -> None:
        value = 1 if player == 1 else -1

        self.rows[r] += value
        self.cols[c] += value

        # diagonal
        if r == c:
            self.diagonal += value

        # antidiagonal
        if (r + c == self.n - 1):
            self.antidiagonal += value

    def check_board(self, r: int, c: int) -> bool:
        return abs(self.rows[r]) == self.n or abs(self.cols[c]) == self.n or abs(self.diagonal) == self.n or abs(self.antidiagonal) == self.n


    def move(self, row: int, col: int, player: int) -> int:
        # make the move + increment counts
        self.increment_counts(row, col, player)

        # check the board
        if self.check_board(row, col):
            return player

        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
