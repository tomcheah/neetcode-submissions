from collections import deque

class HitCounter:

    def __init__(self):
        self.window_size = 300
        self.window = deque()

    def _evict_expired_records(self, timestamp: int) -> None:
        lower_bound = timestamp - self.window_size

        while self.window and self.window[0] <= lower_bound:
            self.window.popleft()

    def hit(self, timestamp: int) -> None:
        self._evict_expired_records(timestamp) 
        self.window.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._evict_expired_records(timestamp)
        return len(self.window)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
