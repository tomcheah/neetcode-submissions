"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        changes = defaultdict(int)
        for interval in intervals:
            changes[interval.start] += 1
            changes[interval.end] -= 1

        meeting_rooms = 0
        res = 0
    
        sorted_keys = sorted(changes.keys())

        for x in sorted_keys:
            if meeting_rooms > 0:
                res = max(meeting_rooms, res)
        
            meeting_rooms += changes[x]

        return res