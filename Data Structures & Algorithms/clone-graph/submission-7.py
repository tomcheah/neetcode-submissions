"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict, deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        original_to_clone = {}
        original_to_neighbors = defaultdict(set)

        if node is None:
            return None

        # bfs 
        queue = deque() 
        queue.append(node)
        visited = set()
        visited.add(node)

        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()

                # clone the node 
                clone = Node(curr_node.val)
                original_to_clone[curr_node] = clone

                for neighbor in curr_node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

                    original_to_neighbors[curr_node].add(neighbor)
                    visited.add(neighbor)

        # set neighbors for cloned graph
        for original, clone in original_to_clone.items():
            neighbors = original_to_neighbors[original]

            for neighbor in neighbors:
                cloned_neighbor = original_to_clone[neighbor]
                clone.neighbors.append(cloned_neighbor)

        return original_to_clone[node]