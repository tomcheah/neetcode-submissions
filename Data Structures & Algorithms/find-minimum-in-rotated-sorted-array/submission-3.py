class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # portion of array is already in sorted order, only need to check smallest value (left) against the current minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])
            # search right sorted porition if we're in the left sorted portion
            if nums[m] >= nums[l]: 
                l = m + 1
            else:
                r = m - 1
        
        return res

            
