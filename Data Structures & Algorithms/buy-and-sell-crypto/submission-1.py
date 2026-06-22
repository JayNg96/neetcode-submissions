class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = None
        highestProfit = 0


        for p in prices:
            if minPrice is None:
                minPrice = p
            else:
                minPrice = min(p, minPrice)
                highestProfit = max(highestProfit, p - minPrice) 

        
        return highestProfit