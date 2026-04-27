from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Use 3 sets
        - one for each of row, column, square

        Tricky part is to determine which square a tile belongs to

        What I'm given is coordinates (row, col)

        Can I somehow map combination of row, col to [0...8]? 


        '''
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        num_rows = len(board[0])
        num_cols = len(board)

        for row in range(num_rows): 
            for col in range(num_cols): 
                curr_num = board[row][col]
                if curr_num == '.':
                    continue

                # figure out which row this belongs to
                belonging_row = row
                if curr_num in rows[belonging_row]:
                    return False
                rows[belonging_row].add(curr_num)

                # figure out which col this belongs to
                belonging_col = col
                if curr_num in columns[belonging_col]:
                    return False
                columns[belonging_col].add(curr_num)

                # figure out which square this belongs to
                belonging_square = (row//3, col//3)
                if curr_num in squares[belonging_square]:
                    return False
                squares[belonging_square].add(curr_num)

        return True