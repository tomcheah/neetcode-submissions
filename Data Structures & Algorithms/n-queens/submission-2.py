class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        diag = set() # r - c  # identifies its \ diagonal
        anti_diag = set() # r + c  # identifies its / diagonal

        def helper(row: int) -> None:
            if row == n:
                solution = [''.join(row) for row in board]
                res.append(solution)
                return

            for col in range(n):
                if col in cols or row - col in diag or row + col in anti_diag:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)

                helper(row+1)

                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)
                board[row][col] = '.'

            
        helper(0)
        return res