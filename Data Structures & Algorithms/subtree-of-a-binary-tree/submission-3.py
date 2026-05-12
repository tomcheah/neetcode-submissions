# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(tree_1: Optional[TreeNode], tree_2: Optional[TreeNode]) -> bool:
            if not tree_1 and not tree_2:
                return True

            if not tree_1 and tree_2: 
                return False
            
            if tree_1 and not tree_2:
                return False

            if tree_1.val != tree_2.val:
                return False

            left = is_same_tree(tree_1.left, tree_2.left)
            right = is_same_tree(tree_1.right, tree_2.right)
            return left and right

        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if root and not subRoot:
            return False

        if is_same_tree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right