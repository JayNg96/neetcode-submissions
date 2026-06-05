class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)     # m = number of rows
        n = len(matrix[0])  # n = number of items in the row
        
        def _search(left: int, right:int) -> bool:
            if left > right:
                return False
            
            mid = (left + right) // 2
            col = mid % n
            row = mid // n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                return _search(left=mid+1, right=right)
            else:
                return _search(left=left, right=mid-1)

        return _search(left=0, right=(m * n) - 1)