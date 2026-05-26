from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Valid tree = connected acyclic graph
        '''
        # build graph
        graph = defaultdict(list) # node -> neighbors 
        visited = set()

        for edge in edges:
            node_1, node_2 = edge
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)

        def dfs(node: int, parent: Optional[int]) -> bool:
            # returns whether a cycle exists or not
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                # skip the edge back to parent
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False
            return True

        # a tree must be connected, so we start dfs from one node only
        if not dfs(0, None):
            return False

        return len(visited) == n