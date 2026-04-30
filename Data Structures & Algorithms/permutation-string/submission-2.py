from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Count all characters in s1 

        If count doesn't match in the current window in s2, then it's not a valid start

        We're keeping all strings valid ending at a certain char

        Only consider valid starting chars before expanding
        '''
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1
        print(f'{s1_count=}')

        l, r = 0, 0
        s2_len = len(s2)
        window = defaultdict(int)
        while r < s2_len:
            print(f'{l=}, {r=}, {window=}')
            # add new character
            char = s2[r]
            window[char] += 1

            # shrink window when character count exceeds what's allowed
            while window[char] > s1_count[char]:
                window[s2[l]] -= 1
                l += 1

            # check for permutation
            has_permutation = True
            for char, count in s1_count.items():
                if count != window[char]:
                    has_permutation = False

            if has_permutation:
                return True

            # increment right pointer
            r += 1

        # do validity check in the end? 

        return False
