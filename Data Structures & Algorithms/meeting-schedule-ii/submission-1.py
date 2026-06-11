"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        Minimum number of rooms = max number of simultaneous meetings happening at a given moment
        '''
        if not intervals:
            return 0
        
        intervals.sort(key=lambda interval: interval.start)
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

