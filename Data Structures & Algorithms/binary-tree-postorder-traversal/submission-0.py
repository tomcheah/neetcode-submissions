# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal postorder

            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            postorder.append(root.val)

        postorder = []
        dfs(root)
        return postorder