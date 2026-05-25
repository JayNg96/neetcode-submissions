class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLen = len(arr)
        rightMax = -1
        for i in reversed(range(0,arrLen)):
            newRightMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newRightMax
        return arr