class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        res = 0
        prev_end = sorted_intervals[0][1] 
        for start, end in sorted_intervals[1:]:
            if start >= prev_end:
                # no overlap
                prev_end = end
            else:
                # overlap + keep interval with earlier ending time
                prev_end = min(prev_end, end)
                res += 1

        

        return res