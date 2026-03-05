from collections import OrderedDict

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

    def print_cache(self):
        print(self.cache.keys())
