from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1

        required = len(t_count)
        formed = 0
        l = 0
        window = defaultdict(int)
        substring = ''
        for r, char in enumerate(s):
            # add new letter
            window[char] += 1

            if char in t_count and window[char] == t_count[char]:
                formed += 1

            # we have a valid substring -> how to update it 
            while formed == required:
                if not substring:
                    substring = s[l:r+1]
                else:
                    if len(substring) > (r - l + 1):
                        substring = s[l:r+1]

                # try shrinking the window 
                left_char = s[l]
                window[left_char] -= 1
                l += 1

                if left_char in t_count and window[left_char] < t_count[left_char]:
                    formed -= 1


        return substring
        