import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Maintain a min-heap of size k
        - Evict the smallest one when we exceed size k

        The kth largest is the minimum of our k largest elements
        '''
        min_heap = []
        heapq.heapify(min_heap)

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)

        
