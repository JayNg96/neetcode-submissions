class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        counter = 1
        while n:
            n -= counter
            if n < 0:
                return counter - 1
            elif n == 0:
                return counter
  
            counter += 1