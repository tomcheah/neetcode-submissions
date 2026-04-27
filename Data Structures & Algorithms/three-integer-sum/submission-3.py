class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Can sort the array because we want to return the values

        Sort first

        How do we use 2 pointers for this then?

        Pick a number nums[i]

        then left pointer = i+1
        right pointer = len(nums) - 1

        nums[i] + nums[j] + nums[k] = 0
        nums[j] + nums[k] = -nums[i]
        '''
        sorted_nums = sorted(nums)
        triplets = []
        for i, num in enumerate(sorted_nums):
            l, r = i+1, len(sorted_nums)-1
            while l < r: 
                left = sorted_nums[l]
                right = sorted_nums[r]
                curr_sum = num + left + right
                if curr_sum == 0:
                    triplet = [num, left, right]
                    if triplet not in triplets:
                        triplets.append([num, left, right])
                    l += 1
                    r -= 1
                    # TODO: handle duplicates
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return triplets


