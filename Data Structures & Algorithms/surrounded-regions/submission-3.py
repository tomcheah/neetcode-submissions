class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Invert the question

        O's on the border won't turn into X's 

        Figure out which O's are connected to these border O's through DFS

        The ones not connected to these O's will become X's

        Use a temporary marker to mark something as visited
        '''
        num_rows = len(board)
        num_cols = len(board[0])
        starting_positions = []

        for c in range(num_cols):
            if board[0][c] == 'O':
                starting_positions.append((0,c))

            if board[num_rows-1][c] == 'O':
                starting_positions.append((num_rows-1, c))

        for r in range(num_rows):
            if board[r][0] == 'O':
                starting_positions.append((r,0))
            
            if board[r][num_cols-1] == 'O':
                starting_positions.append((r, num_cols-1))

        def in_bounds(r: int, c: int) -> bool:
            return (0 <= r < num_rows) and (0 <= c < num_cols)

        def dfs(r, c): 
            if not in_bounds(r, c):
                return

            if board[r][c] == 'X':
                return

            if board[r][c] == 'T':
                return

            board[r][c] = 'T'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for position in starting_positions:
            dfs(position[0], position[1])

        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

        