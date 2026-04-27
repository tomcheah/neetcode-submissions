# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Critical idea: 
            - Path can only split once (take left and right)
        """
        self.max_path_sum = float('-inf')

        def dfs(root) -> int:
            if not root:
                return 0

            left_path = dfs(root.left)
            right_path = dfs(root.right)

            # if left or right paths return negative numbers, turn them to 0 
            left_max = max(left_path, 0)
            right_max = max(right_path, 0)

            # curr max if we did split left and right
            path_splits_at_root = root.val + left_max + right_max

            # global max value handles the tracking of max values splitting at different locations 
            self.max_path_sum = max(self.max_path_sum, path_splits_at_root)

            # return this value b/c we can only split once and the path has to be continuous
            path_does_not_split_at_root = root.val + max(left_max, right_max)
            return path_does_not_split_at_root

        
        dfs(root)
        return self.max_path_sum