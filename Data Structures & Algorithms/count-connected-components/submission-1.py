from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        # build graph
        graph = defaultdict(list)
        for edge in edges:
            node_1, node_2 = edge
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)


        def dfs(node: int) -> None:
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res

        