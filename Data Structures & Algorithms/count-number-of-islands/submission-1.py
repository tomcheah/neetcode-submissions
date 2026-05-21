class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        
        visited = []
        num_rows = len(grid)
        num_cols = len(grid[0])
        for _ in range(num_rows): 
            visited.append([False] * num_cols)


        def dfs(r: int, c: int, grid: List[List[str]]):
            num_rows = len(grid)
            num_cols = len(grid[0])

            if not (0 <= r < num_rows) or not (0 <= c < num_cols):
                return

            if visited[r][c]:
                return

            visited[r][c] = True

            if grid[r][c] == '0':
                return

            dfs(r-1, c, grid)
            dfs(r+1, c, grid)
            dfs(r, c-1, grid)
            dfs(r, c+1, grid)

        for r in range(num_rows):
            for c in range(num_cols):
                if not visited[r][c] and grid[r][c] == '1':
                    # we have a new island when we start dfs from land
                    islands += 1
                    dfs(r, c, grid)

        return islands