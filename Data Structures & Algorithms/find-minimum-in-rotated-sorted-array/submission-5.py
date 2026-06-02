class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Make use of sorted property

        Find the pivot point
        '''
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r)//2 

            # left half is larger -> take right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]