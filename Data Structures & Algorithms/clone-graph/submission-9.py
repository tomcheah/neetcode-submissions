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
        if node is None:
            return None
        
        original_to_clone = {}
        original_to_clone[node] = Node(node.val)

        # bfs 
        queue = deque() 
        queue.append(node)

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                # clone the neighbor if it does not exist
                if neighbor not in original_to_clone:
                    cloned_neighbor = Node(neighbor.val)
                    original_to_clone[neighbor] = cloned_neighbor
                    queue.append(neighbor)
                    
                # copy the edge
                original_to_clone[curr_node].neighbors.append(
                    original_to_clone[neighbor]
                )


        return original_to_clone[node]