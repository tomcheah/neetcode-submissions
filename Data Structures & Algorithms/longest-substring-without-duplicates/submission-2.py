from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l, r = 0, 0
        length = 0

        while r < len(s):
            # add new character
            char = s[r]
            window[char] += 1

            # invalid window
            while window[char] > 1:
                window[s[l]] -= 1
                l += 1
            
            # update length
            length = max(length, r - l + 1)

            # move the right pointer forward
            r += 1

        return length