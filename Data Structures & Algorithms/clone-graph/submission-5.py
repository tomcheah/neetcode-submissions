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
            return None

        original_to_copy = {}
        queue = deque()
        queue.append(node)
        original_to_copy[node] = Node(node.val)

        # create the copies of nodes
        while queue:
            original = queue.popleft()
            for neighbor in original.neighbors: 
                if neighbor not in original_to_copy:
                    # mark as seen upon discovering
                    original_to_copy[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                    
                # set neighbor    
                original_to_copy[original].neighbors.append(original_to_copy[neighbor])

        return original_to_copy[node]


