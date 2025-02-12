import random

class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.d:
            last_index = len(self.l)
            self.l.append(val)
            self.d[val] = last_index
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.d:
            index = self.d[val]
            shift = self.l[index:]
            for element in shift:
                self.d[element] += -1
            self.l.pop(index)
            self.d.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.l)