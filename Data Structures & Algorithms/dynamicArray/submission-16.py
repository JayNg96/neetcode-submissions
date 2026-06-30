class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        get_last_idx = self.getSize()
        if get_last_idx == self.capacity:
           self.resize()
        self.arr[get_last_idx] = n
        self.size += 1

    def popback(self) -> int:
        get_last_idx = self.getSize() - 1
        tmp = self.arr[get_last_idx]
        self.arr[get_last_idx] = None
        self.size -= 1
        return tmp

    def resize(self) -> None:
        new_arr_capacity = [None] * self.capacity
        self.capacity = self.capacity * 2
        self.arr = self.arr + new_arr_capacity 

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity