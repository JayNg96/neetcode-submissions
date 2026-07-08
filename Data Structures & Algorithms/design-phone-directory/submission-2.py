class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.is_used = [False] * maxNumbers

    def get(self) -> int:
        for i in range(len(self.is_used)):
            if not self.is_used[i]:
                self.is_used[i] = True
                return i
            
        return -1
        
    def check(self, number: int) -> bool:
        return not self.is_used[number]
    
    def release(self, number: int) -> None:
        self.is_used[number] = False
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
