class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        dp[(r, c)] = length of the longest increasing path starting at (r, c)
        '''
        dp = {}
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < num_rows and 0 <= c < num_cols

        def dfs(r: int, c: int) -> int:
            longest = 1

            if (r,c) in dp:
                return dp[(r,c)]

            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for neighbor in neighbors:
                next_r, next_c = neighbor
                if in_bounds(next_r, next_c) and matrix[next_r][next_c] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(next_r, next_c))

            dp[(r,c)] = longest
            return longest




        best = 1 
        for r in range(num_rows):
            for c in range(num_cols):
                best = max(best, dfs(r, c))

        return best