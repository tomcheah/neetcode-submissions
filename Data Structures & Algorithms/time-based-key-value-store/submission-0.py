from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        ts_value_tuples = self.map[key]
        res = ""
        l, r = 0, len(ts_value_tuples) - 1
        while l <= r:
            m = (l+r) // 2
            curr_tuple = ts_value_tuples[m]
            curr_value, curr_timestamp = curr_tuple[1], curr_tuple[0]
            if curr_timestamp <= timestamp:
                # keep track of value so far b/c this is a vaild value
                res = curr_value
                l = m + 1
            else:
                r = m - 1

        return res
        
