from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a heap 

        Iterate through the nums and get frequency
        '''
        num_to_count = defaultdict(int) # num -> count
        for num in nums:
            num_to_count[num] += 1

        heap = [(-count, num) for num, count in num_to_count.items()]
        heapq.heapify(heap)

        top_k = []
        for i in range(k):
            _, num = heapq.heappop(heap)
            top_k.append(num)

        return top_k
