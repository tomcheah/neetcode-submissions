# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if not a and not b:
                return True
            elif a and not b:
                return False
            elif not a and b:
                return False
            elif a.val != b.val:
                return False
            
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        # call isSameTree on all nodes of the tree
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False

        if isSameTree(root, subRoot):
            return True


        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)