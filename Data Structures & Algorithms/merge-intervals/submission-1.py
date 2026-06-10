class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_intervals = sorted(intervals)

        for interval in sorted_intervals:
            start, end = interval
            if not res:
                res.append(interval)
                continue

            curr_interval = res.pop()
            curr_interval_start, curr_interval_end = curr_interval

            # overlap condition
            if (curr_interval_start <= start <= curr_interval_end) or (start <= curr_interval_start <= end):
                new_start = min(curr_interval_start, start)
                new_end = max(curr_interval_end, end)
                res.append([new_start, new_end])
            else:
                res.append(curr_interval)
                res.append(interval)

        return res