class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Key is that the array is sorted already

        The index is one indexed -> Add one to the end indicies 

        Use 2 pointers

        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                break
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        # solution is one indexed
        return [l+1, r+1]
