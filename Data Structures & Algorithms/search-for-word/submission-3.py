class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        path = set()

        def in_bounds(r: int, c: int) -> bool:
            return (0 <= r < num_rows) and (0 <= c < num_cols)

        def dfs(r: int, c: int, i: int) -> bool:
            # if i == len(word):
            #     return True

            if not in_bounds(r, c):
                return False

            if (r,c) in path:
                return False

            if board[r][c] != word[i]:
                return False

            if board[r][c] == word[i] and i == len(word) - 1:
                return True

            path.add((r,c))
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r,c))
            return found

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False