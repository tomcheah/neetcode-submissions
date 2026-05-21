class Solution:
    water = -1
    treasure = 0
    land = (2**31) - 1

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Multi-source BFS
        '''

        queue = deque() # (r, c, distance)
        num_rows = len(grid)
        num_cols = len(grid[0])

        def in_bounds(value, bound) -> bool:
            return 0 <= value < bound

        treasures = []

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == self.treasure:
                    treasures.append((r, c, 0))

        for treasure in treasures:
            queue.append(treasure)

        while queue:
            r, c, curr_distance = queue.popleft()

            if in_bounds(r+1, num_rows) and grid[r+1][c] == self.land:
                grid[r+1][c] = curr_distance + 1
                queue.append((r+1, c, curr_distance +1))
            
            if in_bounds(r-1, num_rows) and grid[r-1][c] == self.land:
                grid[r-1][c] = curr_distance + 1
                queue.append((r-1, c, curr_distance+1))

            if in_bounds(c+1, num_cols) and grid[r][c+1] == self.land:
                grid[r][c+1] = curr_distance + 1
                queue.append((r, c+1, curr_distance +1))
        
            if in_bounds(c-1, num_cols) and grid[r][c-1] == self.land:
                grid[r][c-1] = curr_distance + 1
                queue.append((r, c-1, curr_distance +1))

