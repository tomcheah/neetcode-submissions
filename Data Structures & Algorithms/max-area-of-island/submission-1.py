class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False] * num_cols for _ in range(num_rows)]

        def dfs(r: int, c: int) -> int:
            # returns size of contiguous island

            if not (0 <= r < num_rows) or not (0 <= c < num_cols):
                return 0

            if visited[r][c]:
                return 0 

            visited[r][c] = True

            if grid[r][c] == 0:
                return 0

            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)


        max_area = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if not visited[r][c] and grid[r][c] == 1:
                    island_size = dfs(r, c)
                    max_area = max(island_size, max_area)

        return max_area
