class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Do DFS from ocean -> node
        - Reverse the target and starting points basically 
        '''
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def in_bounds(r: int, c: int) -> bool:
            return (0 <= r < num_rows) and (0 <= c < num_cols)

        def dfs(r: int, c: int, visited: set, previous_height: int) -> None:
            if (r,c) in visited:
                return

            if not in_bounds(r, c):
                return

            if heights[r][c] < previous_height:
                return
            
            visited.add((r,c))
            curr_height = heights[r][c]
            dfs(r+1, c, visited, curr_height)
            dfs(r-1, c, visited, curr_height)
            dfs(r, c+1, visited, curr_height)
            dfs(r, c-1, visited, curr_height)

        for c in range(num_cols):
            # top row
            dfs(0, c, pacific_visited, heights[0][c])

            # bot row
            dfs(num_rows-1, c, atlantic_visited, heights[num_rows-1][c])


        for r in range(num_rows):
            # left col
            dfs(r, 0, pacific_visited, heights[r][0])

            # right col
            dfs(r, num_cols-1, atlantic_visited, heights[r][num_cols-1])
        
        return list(pacific_visited.intersection(atlantic_visited))