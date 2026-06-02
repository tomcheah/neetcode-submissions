class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Make use of sorted property 

        Rotated sorted array = [larger part, smaller part]

        all values in larger part are greater than all values in smaller part
        '''
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r)//2 

            # mid is in the smaller part -> search there
            if nums[mid] <= nums[r]:
                r = mid
            # mid is in the larger part -> take the smaller part
            else:
                l = mid + 1
            
        return nums[l]