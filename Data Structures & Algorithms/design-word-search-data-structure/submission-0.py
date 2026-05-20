class TrieNode:
    def __init__(self, end_of_word: bool = False):
        self.children = {}
        self.end_of_word = end_of_word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        '''
        Need to handle special character '.' through recursion
        '''
        def dfs(node: TrieNode, i: int, word: str) -> bool:
            if i == len(word):
                return node.end_of_word

            char = word[i]
            if char == '.':
                for child in node.children:
                    if dfs(node.children[child], i+1, word):
                        return True
                return False

            else:
                if char not in node.children:
                    return False
                
                return dfs(node.children[char], i+1, word)


        return dfs(self.root, 0, word)



        
