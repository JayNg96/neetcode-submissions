class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
           self.resize()
        get_last_idx = self.getSize()
        self.arr[get_last_idx] = n

    def popback(self) -> int:
        get_last_idx = self.getSize() - 1
        tmp = self.arr[get_last_idx]
        self.arr[get_last_idx] = None
        return tmp

    def resize(self) -> None:
        new_arr_capacity = [None] * self.capacity
        self.capacity = self.capacity * 2
        self.arr = self.arr + new_arr_capacity 

    def getSize(self) -> int:
        count = 0
        for i in self.arr:
            if i is not None:
                count += 1
        return count
    
    def getCapacity(self) -> int:
        return self.capacity