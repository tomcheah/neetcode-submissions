class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        sorted_intervals = sorted(intervals)

        for interval in sorted_intervals:
            if not res:
                res.append(interval)
                continue 
            
            prev_start, prev_end = res[-1]
            start, end = interval[0], interval[1]

            # due to sorting, we know prev_start <= start
            if start <= prev_end:
                new_start = min(prev_start, start)
                new_end = max(prev_end, end)
                res.pop()
                res.append([new_start, new_end])
            else:
                res.append(interval)

        return res