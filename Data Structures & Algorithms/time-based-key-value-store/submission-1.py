from collections import defaultdict
from sortedcontainers import SortedList

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(SortedList) # key -> SortedList[(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ''

        values = self.time_map[key]
        l, r = 0, len(values) - 1

        best_candidate = (timestamp, '')

        while l <= r:
            mid = (l+r) // 2
            mid_timestamp, mid_value = values[mid]

            # valid timestamp
            if mid_timestamp <= timestamp:
                # update rule is bad
                if not best_candidate[1]:
                    best_candidate = (mid_timestamp, mid_value)
                elif mid_timestamp > best_candidate[0]:
                    best_candidate = (mid_timestamp, mid_value)
            
                # take the more recent half and see if we can do better
                l = mid + 1
            else:
                r = mid - 1

        return best_candidate[1]


