class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use a hashset to keep track of characters seen in a given window

        Use length to keep track of length of character so far

        Build a sliding window with 2 pointers
        - Increment the right pointer until we see a character we have seen before
        - Increment left pointer pointer until we no longer see the character we have seen before
        '''
        # edge cases
        if not s:
            return 0
        if len(s) == 1:
            return 1

        window = set()
        max_length = 1
        l, r = 0, 1

        # how to initialize the curr count? 

        window.add(s[l])
        while r < len(s):
            curr_char = s[r]
            if curr_char in window:
                # increment left until we no longer see char
                while curr_char in window:
                    left_char = s[l]
                    window.discard(left_char)
                    l += 1
            else:
                window.add(curr_char)
                r += 1
                max_length = max(max_length, len(window))

        return max_length