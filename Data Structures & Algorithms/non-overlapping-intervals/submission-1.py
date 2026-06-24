from collections import defaultdict

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        

        removals = 0
        prev_end = None
        for start, end in sorted_intervals:
            # overlap
            if prev_end is not None and start < prev_end:
                removals += 1
                prev_end = min(prev_end, end)
            # no overlap
            else: 
                prev_end = end

        return removals