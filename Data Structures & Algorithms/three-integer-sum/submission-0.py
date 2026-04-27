class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort() # sort the array 
        for i in range(len(nums)-2):
            # for each i, do 2 pointer algorithm where the target is 
            j = i+1
            k = len(nums)-1
            while j < k:
                # we want nums[i] + nums[j] + nums[k] = 0 
                # -nums[i] = nums[j] + nums[k]
                value = nums[j] + nums[k]
                target = -1 * nums[i]
                print(f"{value=}, {target=}")
                if value == target:
                    triplet = [nums[i], nums[j], nums[k]] 
                    if triplet not in triplets:
                        triplets.append([nums[i],nums[j],nums[k]])
                    # increment pointer
                    j += 1
                    k -= 1
                elif value < target:
                    j += 1
                elif value > target:
                    k -= 1
        # TODO: handle duplicates


        return triplets