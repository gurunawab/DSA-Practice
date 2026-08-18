import random

class RandomizedSet:
    def __init__(self):
        self.a, self.d = [], {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.a)
        self.a.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        i, last = self.d[val], self.a[-1]
        self.a[i], self.d[last] = last, i
        self.a.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.a)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()