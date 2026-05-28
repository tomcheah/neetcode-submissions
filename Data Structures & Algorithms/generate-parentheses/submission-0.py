class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open: int, closed: int, string: str) -> None:
            # base case
            if open == n and closed == n:
                res.append(string)
                return

            if open < n:
                dfs(open+1, closed, string + '(')

            if closed < open:
                dfs(open, closed+1, string + ')')


        dfs(0, 0, '')
        return res