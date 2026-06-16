class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lruCache = {}

    def get(self, key: int) -> int:
        if key not in self.lruCache:
            return -1 
        self.bring_to_front(key, self.lruCache[key])
        return self.lruCache[key]

    def put(self, key: int, value: int) -> None:
        self.bring_to_front(key, value)

        while len(self.lruCache) > self.capacity:
            self.lruCache.pop(next(iter(self.lruCache)))
    
    def bring_to_front(self, key, value):
        if key in self.lruCache:
            self.lruCache.pop(key)
        self.lruCache[key] = value