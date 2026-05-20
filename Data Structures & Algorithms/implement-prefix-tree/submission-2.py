from collections import defaultdict

class TrieNode:
    def __init__(self, is_word = False):
        self.children = defaultdict(TrieNode)
        self.is_word = is_word

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]

        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
                
            curr = curr.children[char]

        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
        