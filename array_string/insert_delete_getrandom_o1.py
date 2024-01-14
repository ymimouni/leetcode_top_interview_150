import random


class RandomizedSet:
    def __init__(self):
        self.items = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.items)
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices[val]
        self.items[idx] = self.items[-1]
        self.indices[self.items[idx]] = idx
        del self.indices[val]
        self.items.pop()
        return True

    def getRandom(self) -> int:
        return self.items[random.randrange(len(self.items))]
