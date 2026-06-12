# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _leafPath(node: Optional[TreeNode], arr: List[int]):
            if not node:
                return False
            
            arr.append(node.val)

            if not node.left and not node.right:
                if sum(arr) == targetSum:
                    return True

            if _leafPath(node.left, arr) or _leafPath(node.right, arr):
                return True

            arr.pop()
            return False
        
        return _leafPath(root, [])

        