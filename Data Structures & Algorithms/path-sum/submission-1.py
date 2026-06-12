# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _leafPath(root: Optional[TreeNode], arr: List[int]):
            if not root:
                return False

            arr.append(root.val)
            if not root.left and not root.right:
                if sum(arr) == targetSum:
                    print('sum:',sum(arr))
                    return True
            if _leafPath(root.left, arr):
                if sum(arr) == targetSum:
                    return True
            if _leafPath(root.right, arr):
                if sum(arr) == targetSum:
                    return True
            arr.pop()
            return False

            
            
                
        
        return _leafPath(root, [])

        