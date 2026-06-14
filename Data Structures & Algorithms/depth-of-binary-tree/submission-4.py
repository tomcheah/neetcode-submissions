# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], height: int) -> int:
            if not root:
                return height

            left_height = helper(root.left, height)
            right_height = helper(root.right, height)

            return 1 + max(left_height, right_height)

        return helper(root, 0)