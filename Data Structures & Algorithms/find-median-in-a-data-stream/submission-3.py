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
        '''
        Add the new number somewhere, then make sure invariants are upheld

        Maintain ordering invariant and size invariant

        Ordering invariant:
        max(smaller_half) <= min(larger_half)

        size invariant:
        len(larger_half) == len(smaller_half) or len(larger_half) == len(smaller_half) + 1
        '''
        heapq.heappush(self.larger_half, num)

        # let larger half evict its smallest value b/c the value may be too small to belong there
        item = heapq.heappop(self.larger_half)
        heapq.heappush_max(self.smaller_half, item)

        # rebalance in case smaller half is too large
        if len(self.smaller_half) > len(self.larger_half):
            item = heapq.heappop_max(self.smaller_half)
            heapq.heappush(self.larger_half, item)

    def findMedian(self) -> float:
        if len(self.larger_half) > len(self.smaller_half):
            return self.larger_half[0]

        return (self.larger_half[0] + self.smaller_half[0]) / 2
        