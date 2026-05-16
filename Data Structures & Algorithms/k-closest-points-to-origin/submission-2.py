from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        Maintain max heap of size k
        - We use max heap because it allows us to evict the furthest away points quickly

        heap contains: (distance, (x, y))
        - ordered by distance

        Pop heap k times to get k closest points to origin
        '''

        heap = []
        heapq.heapify_max(heap)

        for point in points: 
            x, y = point
            distance = self.get_distance(x, y)
            heap_item = (distance, (x, y))
            heapq.heappush_max(heap, heap_item)

            if len(heap) > k:
                heapq.heappop_max(heap)

        res = []
        while heap:
            heap_item = heapq.heappop_max(heap)
            point = heap_item[1]
            res.append(point)

        return res


    def get_distance(self, x1: int, y1: int, x2: int = 0, y2: int = 0) -> int:
        return sqrt((x1-x2)**2 + (y1-y2)**2)

    