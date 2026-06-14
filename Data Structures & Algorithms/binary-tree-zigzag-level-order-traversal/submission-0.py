# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS but with alternating left <-> right 
        '''
        res = []
        queue = deque()
        queue.append(root)

        if not root:
            return []
        
        reverse_direction = False


        while queue:
            curr_level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if reverse_direction:
                res.append(curr_level[::-1])
            else:
                res.append(curr_level)

            reverse_direction = not reverse_direction

        return res