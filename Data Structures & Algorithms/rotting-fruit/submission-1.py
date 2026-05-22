class Solution:
    empty = 0
    fresh = 1
    rotten = 2

    def in_bounds(self, value: int, bound: int) -> bool:
        return 0 <= value < bound

    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Multi-source BFS
        '''
        queue = deque()

        minutes = 0
        fresh_fruit = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        # get starting positions of rotten fruit and number of fresh fruit
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == self.rotten:
                    queue.append((r,c))
                elif grid[r][c] == self.fresh:
                    fresh_fruit += 1

        while queue and fresh_fruit > 0: 
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if self.in_bounds(r+1, num_rows) and (r+1, c) and grid[r+1][c] == self.fresh:
                    grid[r+1][c] = self.rotten
                    fresh_fruit -= 1
                    queue.append((r+1, c))

                if self.in_bounds(r-1, num_rows) and (r-1, c) and grid[r-1][c] == self.fresh:
                    grid[r-1][c] = self.rotten
                    fresh_fruit -= 1
                    queue.append((r-1, c))
            
                if self.in_bounds(c+1, num_cols) and (r, c+1) and grid[r][c+1] == self.fresh:
                    grid[r][c+1] = self.rotten
                    fresh_fruit -= 1
                    queue.append((r, c+1))

                if self.in_bounds(c-1, num_cols) and (r, c-1) and grid[r][c-1] == self.fresh:
                    grid[r][c-1] = self.rotten
                    fresh_fruit -= 1
                    queue.append((r, c-1))

            minutes += 1


        if fresh_fruit == 0:
            return minutes

        return -1


