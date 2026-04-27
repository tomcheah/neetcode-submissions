import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s) != len(t):
        #     return False

        # letters_count = dict.fromkeys(string.ascii_lowercase, 0)

        # for letter in s:
        #     letters_count[letter] += 1
        
        # for letter in t:
        #     letters_count[letter] -= 1

        # for letter in letters_count:
        #     if letters_count[letter] != 0:
        #         return False

        # return True