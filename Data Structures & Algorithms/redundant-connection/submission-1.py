from collections import defaultdict

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        '''
        Find root parent of x
        '''
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        '''
        Returns whether a merge between a and b occurred
        - Merges them if not already merged
        '''
        parent_a, parent_b = self.find(a), self.find(b)

        if parent_a == parent_b:
            return False

        # attach the smaller component to the larger component
        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += 1
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += 1


        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Union Find way
        '''
        n = len(edges) + 1 # 1-indexed
        union_find = UnionFind(n)

        for edge in edges:
            node_1, node_2 = edge
            if not union_find.union(node_1, node_2):
                return [node_1, node_2]


    def findRedundantConnectionDFS(self, edges: List[List[int]]) -> List[int]:
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



