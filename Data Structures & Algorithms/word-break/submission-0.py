class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # starting at index i, can I break the rest of the string into valid words?
        dp = {} # int -> bool
        dp[len(s)] = True
        def helper(i: int) -> bool:
            if i == len(s):
                return True

            if i in dp:
                return dp[i]

            for word in wordDict:
                curr_string = s[i:]
                if curr_string.startswith(word):
                    if helper(i + len(word)):
                        dp[i] = True
                        return True
                        
            dp[i] = False
            return False

        return helper(0)