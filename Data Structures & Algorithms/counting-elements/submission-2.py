class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        hs = set(arr)
        
        count = 0
        for n in arr:
            if n + 1 in hs:
                count += 1

        return count

        