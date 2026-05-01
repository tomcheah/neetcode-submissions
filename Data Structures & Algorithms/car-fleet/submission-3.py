
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Time to target is what matters

        time_to_target = (target - position) / speed

        If a car behinds arrives earlier or at the same time, it merges into the fleet ahead

        To simulate merging naturally, I process cars from closest to target -> furthest from target
        - Front car defines whether anything behind can catch it

        Stack is strictly increasing in arrival time from front to back fleets

        Transform -> Sort -> Monotonically Increasing Stack

        '''
        cars = [(pos, s) for pos, s in zip(position, speed)]
        sorted_cars = sorted(cars, key = lambda x: x[0], reverse=True)
        stack = []
        for car in sorted_cars:
            pos, s = car
            time_to_target = (target - pos) / s

            if not stack:
                stack.append(time_to_target)
            elif time_to_target > stack[-1]:
                stack.append(time_to_target)

        return len(stack)
