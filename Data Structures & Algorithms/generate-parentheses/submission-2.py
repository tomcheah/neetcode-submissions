class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        
        def helper(num_open: int, num_closed: int, path: List[str]) -> None:
            if num_open == num_closed and num_open == n and num_closed == n:
                combinations.append(''.join(path))
                return

            if num_open > n or num_closed > n:
                return

            if num_closed > num_open:
                return

            
            # add (
            path.append('(')
            helper(num_open+1, num_closed, path)
            path.pop()

            # add )
            path.append(')')
            helper(num_open, num_closed+1, path)
            path.pop()

        helper(0, 0, [])
        return combinations
