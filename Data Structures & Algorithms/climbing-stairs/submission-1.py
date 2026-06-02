from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = defaultdict(int)
        def helper(i: int) -> int:
            if i > n:
                return 0
            
            if i == n:
                return 1

            if i in cache:
                return cache[i]

            cache[i] = helper(i+1) + helper(i+2)

            return cache[i]

        return helper(0)

        