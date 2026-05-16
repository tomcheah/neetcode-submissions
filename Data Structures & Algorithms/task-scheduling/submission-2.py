import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        There is cooldown per task

        Put tasks on cooldown in a queue

        Simulate each time 

        At each time, pop the heap 
        - We want to tackle the task with the highest frequency. Hence we use a max heap
        '''
        t = 0 
        queue = []

        task_counts = defaultdict(int)
        for task in tasks: 
            task_counts[task] += 1

        max_heap = [(count, task) for task, count in task_counts.items()]
        heapq.heapify_max(max_heap)

        while max_heap or queue:
            if queue: 
                if t == queue[0][0]:
                    cooldown, count, task = queue.pop(0)
                    task_item = (count, task)
                    heapq.heappush_max(max_heap, task_item)

            if max_heap:
                count, task = heapq.heappop_max(max_heap)
                cooldown = t + n + 1
                if count - 1 > 0:
                    item = (cooldown, count-1, task)
                    queue.append(item)
    
            t += 1

        return t


