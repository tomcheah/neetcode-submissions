class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m

            left_half_low, left_half_high = nums[l], nums[m]
            right_half_low, right_half_high = nums[m], nums[r]


            # left half is sorted
            if left_half_low <= left_half_high:
                # check if target is inside the left half and take the left half
                if target >= left_half_low and target <= left_half_high:
                    r = m - 1
                else: 
                    l = m + 1
            # right half is sorted
            else:

                if target >= right_half_low and target <= right_half_high:
                    l = m + 1
                else:
                    r = m - 1


        return -1