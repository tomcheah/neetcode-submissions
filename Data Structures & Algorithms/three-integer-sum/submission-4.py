class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            # we have seen this starting num already
            if i > 0 and num == sorted_nums[i-1]:
                continue 

            l, r = i+1, len(sorted_nums)-1
            while l < r:
                curr_sum = num + sorted_nums[l] + sorted_nums[r]
                if curr_sum == 0:
                    triplets.append([num, sorted_nums[l], sorted_nums[r]])
                    # take care of duplicates
                    l += 1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1

        return triplets