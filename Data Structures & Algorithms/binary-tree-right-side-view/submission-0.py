# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS
        """
        if not root:
            return [] 
        
        queue = Queue() 
        right_side_view = []

        queue.put(root)
        while not queue.empty():
            rightmost_node = None
            for _ in range(queue.qsize()):
                curr_node = queue.get()
                rightmost_node = curr_node

                if curr_node.left:
                    queue.put(curr_node.left)
                if curr_node.right:
                    queue.put(curr_node.right)


            right_side_view.append(rightmost_node.val)


        return right_side_view


        