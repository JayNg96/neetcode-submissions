class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArr = []
        for i in range(1,len(arr)):
            newArr.append(max(arr[i:]))     
        newArr.append(-1)
        return newArr