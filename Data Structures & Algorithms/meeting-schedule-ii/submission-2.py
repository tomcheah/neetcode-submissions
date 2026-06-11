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
        # keeps track of active meetings
        min_heap = []
        heapq.heapify(min_heap)
        max_rooms = 0

        for interval in intervals:
            # remove all meetings that have ended
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            # add new meeting
            heapq.heappush(min_heap, interval.end)
            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms

