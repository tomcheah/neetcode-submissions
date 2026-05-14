class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # we are guaranteed the existence of a cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break

        cycle_entrance = 0
        while cycle_entrance != slow:
            cycle_entrance = nums[cycle_entrance]
            slow = nums[slow]

        return cycle_entrance