from collections import deque

class Solution:
    empty = 0
    fruit = 1
    rotten = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Multi source BFS
        '''
        num_rows = len(grid)
        num_cols = len(grid[0])

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < num_rows and 0 <= c < num_cols

        def can_explore(r: int, c: int) -> bool:
            return in_bounds(r, c) and (r, c) not in visited and grid[r][c] == self.fruit

        queue = deque()
        num_fruit = 0
        minutes = 0
        visited = set()

        # add all sources to our queue
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == self.rotten:
                    queue.append((r,c))
                elif grid[r][c] == self.fruit:
                    num_fruit += 1

        print(f'Start: {num_fruit = }, {queue = }, {minutes = }')

        # run multi source bfs
        while queue and num_fruit > 0:

            print(f'Queue loop start: {queue = }, {num_fruit = }, {minutes = }')
            for _ in range(len(queue)):
                node = queue.popleft()
                r, c = node
                visited.add(node)

                if can_explore(r+1, c):
                    queue.append((r+1, c))
                    num_fruit -= 1
                    visited.add((r+1, c))
                
                if can_explore(r-1, c):
                    queue.append((r-1, c))
                    num_fruit -= 1
                    visited.add((r-1, c))

                if can_explore(r, c+1):
                    queue.append((r, c+1))
                    num_fruit -= 1
                    visited.add((r, c+1))


                if can_explore(r, c-1):
                    queue.append((r, c-1))
                    num_fruit -= 1
                    visited.add((r, c-1))

            minutes += 1

        print(f'End: {queue = }, {num_fruit = }, {minutes = }')

        return minutes if num_fruit == 0 else -1
