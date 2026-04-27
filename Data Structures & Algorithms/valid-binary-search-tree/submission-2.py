# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS

        Keep track of [min, max] interval when traversing for each subtree

        Update min when going right

        Update max when going left
        """

        def dfs(root, min_val, max_val) -> bool:
            
            if not root:
                return True
            
            if root.val <= min_val or root.val >= max_val:
                return False

            left_max_val = root.val # root.val becomes upper bound of left side
            right_min_val = root.val # root.val becomes lower bound of right side

            left = dfs(root.left, min_val, left_max_val) 
            right = dfs(root.right, right_min_val, max_val)
            return left and right



        return dfs(root, float('-inf'), float('inf'))