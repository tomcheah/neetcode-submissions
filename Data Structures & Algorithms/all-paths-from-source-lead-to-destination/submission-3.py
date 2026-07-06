from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        
        visiting = set() # current path
        safe = set() # node that has all paths terminate in destination

        def dfs(node: int) -> bool:
            '''
            Returns whether every possible path starting from node eventually terminates at destination
            '''
            if node in visiting:
                # cycle
                return False

            if node in safe:
                return True

            # node has no outgoing edges -> check if we have reached our destination
            if not graph[node]:
                return node == destination

            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visiting.remove(node)
            safe.add(node)

            return True

        return dfs(source)