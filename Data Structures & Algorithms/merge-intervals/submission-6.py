class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for interval in intervals:
            if not res:
                res.append(interval)
                continue

            start, end = interval
            prev_start, prev_end = res[-1]
            if start <= prev_end: 
                merged_start = min(start, prev_start)
                merged_end = max(end, prev_end)
                res.pop()
                res.append([merged_start, merged_end])
            else:
                res.append(interval)
            

        return res