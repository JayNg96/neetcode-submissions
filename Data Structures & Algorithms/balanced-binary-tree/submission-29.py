# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        def _get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = _get_height(node.left)
            right_height = _get_height(node.right)
            
            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        if _get_height(root) != -1:
            return True
        return False

        left_height, right_height = _get_height(root.left), _get_height(root.right)
        if left_height != -1 and right_height != -1:
            if abs(left_height - right_height) <= 1:
                return True
        return False
