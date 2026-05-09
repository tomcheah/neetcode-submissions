# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getMaxDepth(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            left_depth = getMaxDepth(root.left, depth+1)
            right_depth = getMaxDepth(root.right, depth+1)
            return max(left_depth, right_depth)

        return getMaxDepth(root, 0)