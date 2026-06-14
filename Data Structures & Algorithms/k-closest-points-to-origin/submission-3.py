import heapq
from math import sqrt

class Solution:
    def get_distance_from_origin(self, x: int, y: int) -> int:
        return sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [] # (distance, point)
        heapq.heapify(min_heap) 

        for point in points:
            x, y = point
            distance = self.get_distance_from_origin(x, y)
            heap_item = (distance, point)
            heapq.heappush(min_heap, heap_item)

        res = []
        for _ in range(k):
            heap_item = heapq.heappop(min_heap)
            res.append(heap_item[1])

        return res