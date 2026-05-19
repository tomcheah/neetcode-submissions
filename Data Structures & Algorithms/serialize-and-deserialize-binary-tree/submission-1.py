# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    null_marker = 'N'
    delimiter = '#'

    def encode_preorder(self, preorder_traversal: List[str]) -> str:
        res = ''
        for i, item in enumerate(preorder_traversal):
            if i == len(preorder_traversal) - 1:
                # don't want trailing delimiter
                res += f'{item}'
            else:
                res += f'{item}{self.delimiter}'

        return res

    def decode_preorder(self, encoded_preorder_traversal: str) -> List[str]:
        return encoded_preorder_traversal.split(self.delimiter)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        '''
        Do preorder traversal with null markers
        '''

        preorder = [] 
        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal preorder 

            if not root:
                preorder.append(self.null_marker)
                return

            preorder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.encode_preorder(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder_traversal = self.decode_preorder(data)

        i = 0
        def build_tree(preorder_traversal: List[str]) -> Optional[TreeNode]:
            nonlocal i 

            curr_val = preorder_traversal[i]
            i += 1

            if curr_val == self.null_marker:
                return None

            node = TreeNode(int(curr_val))
            node.left = build_tree(preorder_traversal)
            node.right = build_tree(preorder_traversal)
            return node

        return build_tree(preorder_traversal)
