# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Inorder traversal to get sorted array of values
        - This works because tree is BST

        Return array[k-1] to get kth's smallest value
        """
        if not root: 
            return []
        
        self.values = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.values.append(root.val)
            dfs(root.right)


        dfs(root)

        # k - 1 b/c 0 indexing
        return self.values[k-1]



        