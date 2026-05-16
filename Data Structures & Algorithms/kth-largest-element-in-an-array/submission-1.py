import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Min heap of size k 
        - Keep track of k largest elements so far
        - Root of heap = kth largest = smallest of our largest
        '''

        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

