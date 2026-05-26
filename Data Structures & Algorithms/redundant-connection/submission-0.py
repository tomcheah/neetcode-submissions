from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Graph nodes: 1 - n
        - not 0 indexed 

        Find the extra edge

        Build the graph edge by edge
        '''

        graph = defaultdict(list)
        def dfs(node: int, target: int, visited: set) -> bool:
            # returns whether a path exists from node -> target

            if node == target:
                return True

            if node in visited:
                return False

            visited.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor, target, visited):
                    return True

            return False

            
        for edge in edges:
            node_1, node_2 = edge
            visited = set()
            if dfs(node_1, node_2, visited):
                return [node_1, node_2]

            graph[node_1].append(node_2)
            graph[node_2].append(node_1)



