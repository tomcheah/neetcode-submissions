class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        visited = []
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False] * num_cols for _ in range(num_rows)]

        def dfs(r: int, c: int):
            if not (0 <= r < num_rows) or not (0 <= c < num_cols):
                return

            if visited[r][c]:
                return

            visited[r][c] = True

            if grid[r][c] == '0':
                return

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(num_rows):
            for c in range(num_cols):
                if not visited[r][c] and grid[r][c] == '1':
                    # we have a new island when we start dfs from land
                    islands += 1
                    dfs(r, c)

        return islands