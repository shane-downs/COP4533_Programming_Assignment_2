from collections import OrderedDict
from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.misses = 0

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
            self.misses += 1
            self.cache[key] = value
        elif key not in self.cache:
            self.misses += 1
            self.cache[key] = value


    def printCache(self):
        for key, value in self.cache.items():
            print(key, value)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.misses = 0

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key, True)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
            self.misses += 1
            self.cache[key] = value
        elif key not in self.cache:
            self.misses += 1
            self.cache[key] = value

    def printCache(self):
        for key, value in self.cache.items():
            print(key, value)

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.misses = 0

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key, True)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
            self.misses += 1
            self.cache[key] = value
        elif key not in self.cache:
            self.misses += 1
            self.cache[key] = value

    def printCache(self):
        for key, value in self.cache.items():
            print(key, value)

class FIFCache:
    def __init__(self, capacity, inputList):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.inputDict = dict()
        self.misses = 0

        for i in range(len(inputList)):
            if inputList[i] not in self.inputDict:
                self.inputDict[inputList[i]] = deque()
            self.inputDict[inputList[i]].append(i)

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.inputDict[key].popleft()
        elif len(self.cache) >= self.capacity:
            key_to_remove = None
            for key1, value in self.cache.items():
                if len(self.inputDict[key1]) == 0:
                    key_to_remove = key1
                    break
                else:
                    if key_to_remove == None:
                        key_to_remove = key1
                    else:
                        if self.inputDict[key_to_remove][0] < self.inputDict[key1][0]:
                            key_to_remove = key1

            self.cache.pop(key_to_remove)
            self.misses += 1
            self.cache[key] = value
            self.inputDict[key].popleft()
        elif key not in self.cache:
            self.misses += 1
            self.cache[key] = value
            self.inputDict[key].popleft()

    def printCache(self):
        for key, value in self.cache.items():
            print(key, value)

array = ["a", "b", "c", "d", "e", "f", "a", "b", "c", "e", "g"]
test = FIFCache(5, array)
for i in range(len(array)):
    test.put(array[i], i)
print(test.inputDict.items())
print(test.printCache())


