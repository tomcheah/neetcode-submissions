# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''

        Preorder tells us what the roots are

        Inorder tells us what nodes comprise the left subtree and right subtree

        In order = [left X right]

        Preorder = [X ... ]

        You grab a number from preorder 

        This splits the in order into a left and right subarray

        node = TreeNode(X) 
        node.left = made from the left subarray
        node.right = made from the right subarray

        just do build tree again?
        
        how do we attach the children?
        '''
        if not preorder or not inorder:
            return None

        val = preorder[0]
        try:
            index = inorder.index(val)
        except ValueError:
            return None

        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        node.right = self.buildTree(preorder[index+1:], inorder[index+1:])

        return node

