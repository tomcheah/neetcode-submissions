class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        position = 0
        for i in range(len(gas)):
            net = gas[i] - cost[i]
            total += net

            if total < 0:
                total = 0
                position = i + 1

        return position
        