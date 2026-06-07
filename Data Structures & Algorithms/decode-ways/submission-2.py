class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def helper(i: int) -> int:
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            take_one = helper(i+1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                take_two = helper(i+2)
                dp[i] = take_one + take_two
            else:
                dp[i] = take_one
                
            return dp[i]


        return helper(0)