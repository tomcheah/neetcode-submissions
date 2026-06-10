class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # add all intervals before the start of newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge all overlapping intervals
        merged_interval_start = newInterval[0]
        merged_interval_end = newInterval[1]
        while i < n and intervals[i][0] <= merged_interval_end:
            merged_interval_start = min(intervals[i][0], merged_interval_start)
            merged_interval_end = max(intervals[i][1], merged_interval_end)
            i += 1

        # append the merged interval
        res.append([merged_interval_start, merged_interval_end])

        # add all intervals that occur after the end of this merged interval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res