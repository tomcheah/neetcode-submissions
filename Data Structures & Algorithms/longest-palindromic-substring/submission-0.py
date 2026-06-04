class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_start = 0
        best_len = 1

        for length in range(1, n+1):
            for l in range(0, n-length+1):
                r = l + length - 1
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True

                    if dp[l][r] and length > best_len:
                        best_start = l
                        best_len = length

        return s[best_start:best_start + best_len]