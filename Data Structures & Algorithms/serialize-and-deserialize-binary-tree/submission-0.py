# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    null_placeholder = "n"
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorder_traversal = []

        def dfs(root):
            if not root:
                self.preorder_traversal.append(self.null_placeholder)
                return

            self.preorder_traversal.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(self.preorder_traversal)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == self.null_placeholder:
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

