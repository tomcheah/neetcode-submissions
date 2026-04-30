from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Use a window to keep track of character counts
        - Let's make sure this window is always valid

        k is the upper bound for number of replacements in a valid window

        a window is valid when

        window_chars = count_most_frequent_char + everything_else

        k <= window_chars - count_most_frequent_char
        '''

        l, r = 0, 0
        longest_length = 0
        window = defaultdict(int) # {char: count}
        for r, char in enumerate(s):
            # add the latest character into our window
            window[s[r]] += 1

            # maintain our valid window
            most_frequent_char_length = max(window.values())
            while k < (r-l+1) - most_frequent_char_length and l < r: 
                window[s[l]] -= 1 
                l += 1                
                most_frequent_char_length = max(window.values())

            # update our longest length
            longest_length = max(longest_length, r-l+1) 

        return longest_length