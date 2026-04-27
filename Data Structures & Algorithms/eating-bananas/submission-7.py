class Solution:
    def canFinish(self, piles: List[int], eating_speed: int, h: int) -> bool:
        # each hour, eat eating_speed bananas, don't move onto next pile until bananas in existing pile are gone
        print(f"This is {eating_speed = }")
        hours_to_finish = 0
        for pile in piles:
            # this is buggy
            hours_to_finish += math.ceil(float(pile) / eating_speed)

        return hours_to_finish <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        l, r = 1, upper_bound
        # do binary search with the eating_speeds 
        min_eating_speed = upper_bound
        while l <= r:
            m = (l+r) // 2
            curr_eating_speed = m
            if self.canFinish(piles, curr_eating_speed, h):
                min_eating_speed = min(min_eating_speed, curr_eating_speed)
                # if I can finish it with this eating speed, we have to check if there's a lower eating speed
                r = m - 1
            else:
                # if I can't finish it with this eating speed, we have to increase eating speed 
                l = m + 1

        return min_eating_speed