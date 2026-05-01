
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
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
