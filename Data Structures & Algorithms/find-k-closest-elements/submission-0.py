import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = [] # (distance, number)
        heapq.heapify(min_heap)

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(min_heap, (distance, num))

        res = []
        for _ in range(k):
            heap_item = heapq.heappop(min_heap)
            res.append(heap_item[1])

        return sorted(res)