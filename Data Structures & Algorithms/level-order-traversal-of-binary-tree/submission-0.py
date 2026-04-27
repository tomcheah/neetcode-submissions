# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Iterative solution -> BFS

        How to do BFS recursively?
        """
        if not root:
            return []

        bfs_queue = Queue()
        level_order = []


        bfs_queue.put(root)
        while not bfs_queue.empty():
            current_level = []
            for _ in range(bfs_queue.qsize()):
                curr_node = bfs_queue.get()
                current_level.append(curr_node.val)

                if curr_node.left:
                    bfs_queue.put(curr_node.left)
                if curr_node.right:
                    bfs_queue.put(curr_node.right)

            level_order.append(current_level)



        return level_order