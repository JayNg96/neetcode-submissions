from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruCache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.lruCache:
            return -1 
        self.lruCache.move_to_end(key)
        return self.lruCache[key]

    def put(self, key: int, value: int) -> None:
        self.lruCache[key] = value
        self.lruCache.move_to_end(key)

        while len(self.lruCache) > self.capacity:
            self.lruCache.popitem(last=False)
    
