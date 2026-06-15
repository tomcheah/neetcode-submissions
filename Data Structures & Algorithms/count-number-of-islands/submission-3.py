class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> None:
            if (r, c) in visited:
                return

            if not (0 <= r < num_rows) or not (0 <= c < num_cols):
                return

            if grid[r][c] == '0':
                return

            visited.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(num_rows):
            for c in range(num_cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    print(f'We are here {(r,c,)}')
                    dfs(r, c)
                    num_islands += 1

        return num_islands