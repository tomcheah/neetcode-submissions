# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -math.inf
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if not root:
                return 0

            # what are the child paths that yield positive results?
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # path where the split happens at this node
            max_path_split = root.val + left + right 

            # update global answer
            max_path_sum = max(max_path_sum, max_path_split)

            # one sided path that can be extended by parent
            max_path_to_return_to_parent = max(root.val + left, root.val + right)

            return max_path_to_return_to_parent

        dfs(root)
        return max_path_sum