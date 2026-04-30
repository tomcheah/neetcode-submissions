from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a deque to maintain a monotonically decreasing queue 

        When a new number arrives that is larger than what we've seen before, we don't care about what we've seen before

        newer + bigger = strictly better candidate 

        A good value can still become invalid if it slides out the window

        2 update rules to our deque: 
        - Remove from the back anything smaller than current value
        - Remove from the front anything outside the current window 

        ^ We need to do these operations efficiently, which is why we use a deque 

        Store the index itself in the deque
        '''

        res = []
        l, r = 0, 0
        q = deque()
        nums_len = len(nums)
        while r < nums_len:
            curr_num = nums[r]

            # maintain monotonically decreasing order
            while q and curr_num > nums[q[-1]]:
                q.pop()

            # add r to the queue
            q.append(r) 

            # evict the beginning element once we slid the window forward
            if l > q[0]:
                q.popleft()    
            
            # need to make sure window is at least size k
            if r >= k - 1:
                max_val_in_window = nums[q[0]]
                res.append(max_val_in_window)
                l += 1

            r += 1

        return res