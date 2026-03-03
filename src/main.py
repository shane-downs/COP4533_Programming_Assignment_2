from collections import OrderedDict

class FIFOCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.misses = 0

    def get(self, key):
        if key in self.cache:
            return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            pass
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

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
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


test = LRUCache(3)
test.put(1, 5)
test.put(2, 6)
# test.put(1, 5)
test.put(3, 7)
test.put(1, 5)
# test.put(4, 8)
# test.put(5, 9)
# test.put(6, 10)
# test.put(7, 11)
print(test.printCache())
print(test.misses)

