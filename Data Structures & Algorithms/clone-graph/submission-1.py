"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Hashmap? 

        Map original node -> copy node
        - this keeps track of those we have visited 

        One pass to create the node 

        Another pass to set each node's neighbors?

        Visit the node

        Then handle the neighbors 
        '''
        if not node:
            return

        original_to_copy = {}
        queue = []
        queue.append(node)

        # create the copies of nodes
        while queue:
            original = queue.pop(0)
            original_to_copy[original] = Node(original.val)

            for neighbor in original.neighbors: 
                if neighbor and neighbor not in original_to_copy:
                    queue.append(neighbor)

        # set the neighbors of nodes
        for original, copy in original_to_copy.items():
            for neighbor in original.neighbors:
                copy.neighbors.append(original_to_copy[neighbor])

        
        return original_to_copy[node]


