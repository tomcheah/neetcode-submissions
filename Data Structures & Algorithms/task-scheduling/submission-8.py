import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Greedy: Process the task with the highest frequency

        State:
            - max heap (count, task) -> What tasks are available to do? 
            - min heap (eligible_time, count, task) -> What tasks are on cooldown?
        '''
        available = [] # max heap (count, task)
        cooldown = [] # min heap (eligible_time, count, task)
        task_counts = defaultdict(int)

        for task in tasks:
            task_counts[task] += 1

        for task, count in task_counts.items():
            heap_item = (count, task)
            heapq.heappush_max(available, heap_item)

        t = 0
        while available or cooldown:
            # make tasks eligible if current time has passed the next eligible time
            while cooldown and t >= cooldown[0][0]:
                _, count, task = heapq.heappop(cooldown)
                max_heap_item = (count, task)
                heapq.heappush_max(available, max_heap_item)
            
            # task is available -> do the most frequent task; else idle
            if available:
                count, task = heapq.heappop_max(available)
                if count - 1 > 0:
                    min_heap_item = (t+n+1, count -1, task)
                    heapq.heappush(cooldown, min_heap_item)

            t += 1
        
        return t
