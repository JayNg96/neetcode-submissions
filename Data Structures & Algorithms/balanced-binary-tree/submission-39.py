# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def _dfs(node, count=0):
            if not node:
                return count

            left_subtree = _dfs(node.left, count + 1)
            right_subtree = _dfs(node.right, count + 1)
            
            is_balanced = abs(left_subtree - right_subtree) <= 1

            return max(left_subtree, right_subtree) if is_balanced else -1

        left_subtree_height = _dfs(root.left)
        if left_subtree_height == -1:
            return False

        right_subtree_height = _dfs(root.right)
        if right_subtree_height == -1:
            return False
            
        return abs(left_subtree_height - right_subtree_height) <= 1

