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

        max_meeting_rooms = 0
        curr_meeting_rooms = 0

        sorted_times = sorted(changes.keys())
        for t in sorted_times:
            curr_meeting_rooms += changes[t]
            max_meeting_rooms = max(max_meeting_rooms, curr_meeting_rooms)

        return max_meeting_rooms