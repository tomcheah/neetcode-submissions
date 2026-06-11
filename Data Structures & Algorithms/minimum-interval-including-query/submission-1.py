from collections import defaultdict
import heapq

class Solution:
    def get_interval_length(self, interval: List[int]) -> int:
        return interval[1] - interval[0] + 1

    def interval_contains(self, interval: List[int], q: int) -> bool:
        return interval[0] <= q <= interval[1]

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort intervals by start time
        intervals.sort()

        # we want to process queries in increasing order so we don't have to revisit intervals
        sorted_queries = sorted(queries)
        query_to_length = defaultdict(int)

        min_heap = []
        heapq.heapify(min_heap) # contains (length, end)

        i = 0
        for query in sorted_queries:

            # add all intervals whose start time begin before my query
            while i < len(intervals) and intervals[i][0] <= query:
                interval = intervals[i]
                heap_item = (self.get_interval_length(interval), interval[1])
                heapq.heappush(min_heap, heap_item)
                i += 1

            # remove all intervals that end before my query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # the shortest interval that contains my query must be the top of the heap
            if min_heap:
                query_to_length[query] = min_heap[0][0]
            else:
                query_to_length[query] = -1

        # build our result
        res = []
        for query in queries:
            res.append(query_to_length[query])

        return res
