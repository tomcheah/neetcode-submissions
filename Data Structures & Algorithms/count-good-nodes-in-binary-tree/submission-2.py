# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_so_far: int) -> int:
            if not root:
                return 0

            add_good_node = 0
            if root.val >= max_so_far:
                add_good_node = 1

            max_so_far = max(max_so_far, root.val)
            
            left_good_nodes = dfs(root.left, max_so_far)
            right_good_nodes = dfs(root.right, max_so_far)
            return left_good_nodes + right_good_nodes + add_good_node

        return dfs(root, -math.inf)