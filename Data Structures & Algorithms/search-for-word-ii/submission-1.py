class TrieNode:
    def __init__(self, end_of_word: bool = False) -> None:
        self.children = {} # letter: TrieNode
        self.end_of_word = end_of_word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.build_trie(words)
        num_rows = len(board)
        num_cols = len(board[0])
        res = []
        visited = set()

        def in_range(r: int, c: int) -> bool:
            return 0 <= r < num_rows and 0 <= c < num_cols 

        def dfs(r: int, c: int, curr: TrieNode, path: str) -> None: 
            if not in_range(r, c):
                return
            
            if (r, c) in visited:
                return

            letter = board[r][c]
            if letter not in curr.children:
                return

            next_node = curr.children[letter]
            next_path = path + letter
            if next_node.end_of_word:
                res.append(next_path)
                next_node.end_of_word = False

            visited.add((r,c))
            dfs(r+1, c, next_node,next_path)
            dfs(r-1, c, next_node, next_path)
            dfs(r, c+1, next_node, next_path)
            dfs(r, c-1, next_node, next_path)
            visited.remove((r,c))

        curr = trie
        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, curr, '')
                
        return res


    def build_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.end_of_word = True

        return root
                
