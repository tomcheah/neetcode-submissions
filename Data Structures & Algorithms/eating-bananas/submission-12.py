class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Binary search within 1 <= k <= max(piles)
        '''
        def can_complete(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours_needed = (pile + k - 1) // k
                hours += hours_needed
            return hours <= h

        l, r = 1, max(piles)
        eating_speed = r

        while l <= r:
            mid = (l+r) // 2

            if can_complete(mid):
                eating_speed = min(eating_speed, mid)

                # see if we can do better by taking the lower half
                r = mid - 1
            else:
                l = mid + 1

        return eating_speed

