# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Calculate [isBalanced, height] of each node from bottom up using DFS

        This does one pass through the entire tree -> O(n) time
        """

        def dfs(root: Optional[TreeNode]):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            left_height = left[1]
            right_height = right[1]
            height_difference = abs(left_height - right_height)
            height_of_root = 1 + max(left_height, right_height)
            
            # tree is balanced iff left is balanced, right is balanced, and height difference is less than 1
            if left[0] and right[0] and height_difference <= 1:
                return [True, height_of_root]
            else:
                return [False, height_of_root]
        
        return dfs(root)[0]

        

            