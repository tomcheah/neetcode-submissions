# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS with keeping track of a max seen so far
        """
        self.good_nodes = 0

        def dfs(root, max_so_far): 
            if not root:
                return
            
            if root.val >= max_so_far:
                self.good_nodes += 1
                max_so_far = root.val

            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)

        dfs(root, float('-inf')) # initialize to negative infinity
        return self.good_nodes

        