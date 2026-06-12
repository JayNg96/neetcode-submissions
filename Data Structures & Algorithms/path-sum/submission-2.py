# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _leafPath(root: Optional[TreeNode], sum_of_path: int):
            if not root:
                return False

            sum_of_path += root.val
            if not root.left and not root.right:
                return sum_of_path == targetSum
            
            return _leafPath(root.left, sum_of_path) or _leafPath(root.right, sum_of_path)
        return _leafPath(root, 0)