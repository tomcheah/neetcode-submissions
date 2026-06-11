"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        # sort by start time
        intervals.sort(key=lambda interval: interval.start)
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prev_end:
                return False
        
            prev_end = interval.end

        return True