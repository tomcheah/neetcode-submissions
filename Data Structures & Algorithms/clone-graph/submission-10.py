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
        original_to_clone[node] = Node(val=node.val)

        queue = deque()
        queue.append(node)

        while queue: 
            curr_node = queue.popleft() 
            curr_node_clone = original_to_clone[curr_node]

            for neighbor in curr_node.neighbors:
                if neighbor not in original_to_clone:
                    original_to_clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                curr_node_clone.neighbors.append(original_to_clone[neighbor])

        return original_to_clone[node]

