from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Bottoms up solution
        '''
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def climbStairsTopDown(self, n: int) -> int:
        '''
        Top down solution
        '''
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

        