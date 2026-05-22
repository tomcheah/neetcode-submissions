import heapq

class MedianFinder:

    def __init__(self):
        # contains larger elements + the "extra" element
        self.larger_half = []
        heapq.heapify(self.larger_half)

        # contains smaller elements
        self.smaller_half = []
        heapq.heapify_max(self.smaller_half)
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.larger_half, num)

        # make sure smaller half always gets lower values
        item = heapq.heappop(self.larger_half)
        heapq.heappush_max(self.smaller_half, item)

        # rebalance in case smaller half is too large
        if len(self.smaller_half) > len(self.larger_half):
            item = heapq.heappop_max(self.smaller_half)
            heapq.heappush(self.larger_half, item)

    def findMedian(self) -> float:
        if not self.smaller_half:
            return self.larger_half[0]

        if not self.larger_half:
            return self.smaller_half[0]

        if len(self.larger_half) > len(self.smaller_half):
            return self.larger_half[0]

        return (self.larger_half[0] + self.smaller_half[0]) / 2
        