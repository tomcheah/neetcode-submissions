# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def dfs(root) -> int:
            if not root:
                return 0

            left_path = dfs(root.left)
            right_path = dfs(root.right)
            left_max = max(left_path, 0)
            right_max = max(right_path, 0)

            # curr max that includes this node in the path
            curr_max = root.val + left_max + right_max
            self.max_path_sum = max(self.max_path_sum, curr_max)

            return root.val + max(left_max, right_max)

        
        dfs(root)
        return self.max_path_sum