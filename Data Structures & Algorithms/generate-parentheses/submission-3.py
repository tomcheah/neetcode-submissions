class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        def helper(num_open: int, num_closed: int, path: str) -> None:
            if num_open == num_closed and num_open == n and num_closed == n:
                combinations.append(path)
                return

            if num_open > n or num_closed > n:
                return

            if num_closed > num_open:
                return
            
            # add (
            helper(num_open+1, num_closed, path + '(')

            # add )
            helper(num_open, num_closed+1, path + ')')

        helper(0, 0, '')
        return combinations
