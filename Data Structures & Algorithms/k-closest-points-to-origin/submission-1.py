class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print('Before:',points)
        def _quickSort(lists: List[List[int]], left:int, right:int) -> List[List[int]]:
            if left >= right:
                return
            def _partition(lists, left, right):
                pivot_sum = pow(lists[right][0], 2) + pow(lists[right][1], 2)
                for i in range(left, right):
                    i_sum = pow(lists[i][0], 2) + pow(lists[i][1], 2)
                    if i_sum <= pivot_sum:
                        temp = lists[i]
                        lists[i] = lists[left]
                        lists[left] = temp
                        left += 1
                lists[left], lists[right] = lists[right], lists[left]
                return left
            pivot_index = _partition(lists, left, right)
            _quickSort(lists=lists, left=left, right=pivot_index-1)
            _quickSort(lists=lists, left=pivot_index+1, right=right)        
            
        _quickSort(points, 0, len(points)-1)
        return points[:k]