import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Greedy: Process the task with the highest frequency

        State:
            - max heap (count, task)
            - min heap (eligible_time, task)

        '''
        task_counts = defaultdict(int) # task -> task_count
        available = [] # max heap (count, task)
        cooldown = [] # min heap (eligible_time, task)

        task_counts = defaultdict(int)
        for task in tasks:
            task_counts[task] += 1

        for task, count in task_counts.items():
            heap_item = (count, task)
            heapq.heappush_max(available, heap_item)

        t = 0
        while available or cooldown:
            print(f'{t = }, {available = }, {cooldown = }')

            # make tasks eligible if current time has passed the next eligible time
            while cooldown and t >= cooldown[0][0]:
                _, task = heapq.heappop(cooldown)
                count = task_counts[task]
                max_heap_item = (count, task)
                heapq.heappush_max(available, max_heap_item)
            
            # nothing is on cooldown -> do the most frequent task
            if available:
                count, task = heapq.heappop_max(available)
                # print(f'At {t = }, we process {task = } with {count = }')
                task_counts[task] -= 1
                if task_counts[task] > 0:
                    min_heap_item = (t+n+1, task)
                    heapq.heappush(cooldown, min_heap_item)
                
                t += 1

            else:
                # print(f'At {t = }, we idle')
                # idle cycle, nothing is available
                t += 1
        
        return t
