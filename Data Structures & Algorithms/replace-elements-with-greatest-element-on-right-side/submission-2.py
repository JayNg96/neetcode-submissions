class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newList = []
        for i in range(1,len(arr)):
            newList.append(max(arr[i:]))

            
        newList.append(-1)

        return newList