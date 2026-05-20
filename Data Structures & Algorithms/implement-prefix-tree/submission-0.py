from collections import defaultdict

class TrieNode:
    def __init__(self, is_word = False):
        self.children = defaultdict(TrieNode)
        self.is_word = is_word
        self.child_words = set()

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            curr.child_words.add(word)

        curr.is_word = True
        curr.child_words.add(word)

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            curr = curr.children[char]

        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            curr = curr.children[char]

        return len(curr.child_words) > 0 
        