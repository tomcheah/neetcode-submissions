class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_intervals = sorted(intervals)

        res.append(sorted_intervals[0])
        for start, end in sorted_intervals[1:]: 
            if res[-1][0] <= start <= res[-1][1]:
                prev_start, prev_end = res.pop()
                new_start = min(prev_start, start) 
                new_end = max(prev_end, end)
                res.append([new_start, new_end])
            else:
                res.append([start, end])

        return res