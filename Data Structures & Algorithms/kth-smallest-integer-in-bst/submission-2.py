# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root: Optional[TreeNode]):
            nonlocal in_order_traversal 

            if not root:
                return

            dfs(root.left)
            in_order_traversal.append(root.val)
            dfs(root.right)

        in_order_traversal = []
        dfs(root)
        return in_order_traversal[k-1]
