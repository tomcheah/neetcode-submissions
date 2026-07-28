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

        curr_meeting_rooms = 0
        max_meeting_rooms = 0
        for t in sorted(changes.keys()):
            curr_meeting_rooms += changes[t]
            max_meeting_rooms = max(curr_meeting_rooms, max_meeting_rooms)

        return max_meeting_rooms