from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        Count array
        '''

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        threshold = len(nums) // 3

        res = []
        for num in count:
            if count[num] > threshold:
                res.append(num)

        return res