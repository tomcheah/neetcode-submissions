import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Use a max heap

        Pop until max heap length = 1
        '''
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            second_heaviest = heapq.heappop_max(stones)           
            if heaviest > second_heaviest:
                heapq.heappush_max(stones, heaviest-second_heaviest)


        if stones:
            return stones[0]

        return 0