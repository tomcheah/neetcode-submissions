class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort nums

        Backtracking with skipping duplicate choices in the same layer
        '''
        nums.sort()
        subsets = []
        
        def helper(i: int, path: List[int]) -> None:
            if i == len(nums):
                subsets.append(path[:])
                return
            
            # take i
            path.append(nums[i])
            helper(i+1, path)
            path.pop()

            # skip i and all subsequent duplicates
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[next_i-1]:
                next_i += 1

            helper(next_i, path)

        
        helper(0, [])
        return subsets