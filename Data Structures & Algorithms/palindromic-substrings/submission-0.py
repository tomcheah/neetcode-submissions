class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for length in range(1, n+1):
            for l in range(0, n - length + 1):
                r = l + length - 1

                if s[l] == s[r] and (length <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    count += 1

        return count