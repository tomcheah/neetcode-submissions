# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def get_height(root: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not root:
                return 0
            
            left_height = get_height(root.left)
            right_height = get_height(root.right)
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        get_height(root)
        return diameter