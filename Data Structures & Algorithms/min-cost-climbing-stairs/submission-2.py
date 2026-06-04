class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {} # Cost of going from index i to the top
        total_steps = len(cost) # not 0 indexed

        def helper(i: int) -> int:
            # returns cost to reach this step
            if i == total_steps:
                return 0 

            if i > total_steps:
                return 0
            
            if i in cache:
                return cache[i]

            one_step = cost[i] + helper(i+1)
            two_step = cost[i] + helper(i+2)
            cache[i] = min(one_step, two_step)

            return cache[i]

        return min(helper(0), helper(1))
            