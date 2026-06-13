import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True
        

    def remove(self, val: int) -> bool:
        '''
        Use val to index to index into values in O(1) time

        Swap the value with the rightmost value, then pop from array
        '''
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        rightmost_value = self.values[-1]
        rightmost_index = self.val_to_index[rightmost_value]
        self.values[index] = self.values[rightmost_index]
        self.val_to_index[rightmost_value] = index
        del self.val_to_index[val]
        self.values.pop()

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()