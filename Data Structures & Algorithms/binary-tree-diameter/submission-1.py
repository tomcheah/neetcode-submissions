# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = max(curr_max_diameter, diameter(left) + diameter(right))
        """
        diameter at node = height(node.left) + 1 if node.left + height(node.right) + 1 if node.right

        call this function at every node

        how can we do this in one traversal?

        Keep track of 
        """
        self.res = 0

        def heightOfBinaryTree(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left_height = heightOfBinaryTree(root.left)
            right_height = heightOfBinaryTree(root.right)
            self.res = max(self.res, left_height + right_height)
            return 1 + max(left_height, right_height) # return height 
        
        heightOfBinaryTree(root)
        return self.res
