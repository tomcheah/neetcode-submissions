from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Count all characters in s1 

        Shrink the window when a character count exceeds what's allowed
        '''
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1

        l = 0
        window = defaultdict(int)
        for r, char in enumerate(s2):
            # add new character
            window[char] += 1

            # shrink window when character count exceeds what's allowed
            while window[char] > s1_count[char]:
                window[s2[l]] -= 1
                l += 1

            # from here, we make sure no character exceeds required frequency
            # if total characters match exacatly, we have a permutation 
            if (r - l + 1) == len(s1):
                return True

        return False
