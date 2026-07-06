from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Tree = connected acyclic graph
        '''

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        discovered = set() # nodes that DFS has discovered 
        def dfs(node: int, parent: Optional[int]) -> bool:
            '''
            Returns whether a cycle exists starting dfs from node or not
            '''
            discovered.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue 

                if neighbor in discovered:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, None):
            return False

        return len(discovered) == n
        