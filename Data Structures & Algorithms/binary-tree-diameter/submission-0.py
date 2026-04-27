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

        def depthOfBinaryTree(root: Optional[TreeNode], depth: int) -> int:
            if not root:
                return depth

            return max(depthOfBinaryTree(root.left, depth+1), depthOfBinaryTree(root.right, depth+1))

        if not root: 
            return 0
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        left_depth = depthOfBinaryTree(root.left, 0)
        right_depth = depthOfBinaryTree(root.right, 0)

        return max(left_diameter, right_diameter, left_depth+right_depth)

