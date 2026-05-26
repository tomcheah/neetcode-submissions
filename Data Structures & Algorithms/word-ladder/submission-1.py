from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        cat -> bat -> bag -> sag
        '''
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque() # (word, distance)
        queue.append((beginWord, 1))
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance

            mutations = self.get_mutations(word)
            for mutation in mutations: 
                if mutation in word_set: 
                    queue.append((mutation, distance+1))
                    # in the shortest path, we only use each word once
                    word_set.remove(mutation)

        return 0

    def get_mutations(self, word: str) -> list:
        mutations = []
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                mutation = word[:i] + letter + word[i+1:]
                if mutation != word:
                    mutations.append(mutation)

        return mutations
