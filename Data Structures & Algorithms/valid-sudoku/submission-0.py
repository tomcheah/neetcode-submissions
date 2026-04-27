class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Use sets to keep track of each row, column, square

        Divide board into 9 squares -> Each square can be identified with (a, b) 

        Where a,b  >= 0 and a,b <= 2 

        To figure out which square an entry (x, y) belongs to, do integer division x/3, y/3 

        Map (a, b) -> square set
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r // 3, c // 3)

        for r in range(len(board)):
            curr_row = board[r]
            for c in range(len(curr_row)):
                curr_val = board[r][c]
                if curr_val == ".":
                    continue
                if (curr_val in rows[r] or 
                    curr_val in cols[c] or 
                    curr_val in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(curr_val)
                cols[c].add(curr_val)
                squares[(r//3, c//3)].add(curr_val)


        return True