class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < num_rows and 0 <= c < num_cols

        def dfs(r: int, c: int) -> None:
            if not in_bounds(r,c):
                return 
            
            if (r,c) in visited:
                return 

            visited.add((r,c))

            if grid[r][c] == '0':
                return 

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    num_islands += 1

        return num_islands