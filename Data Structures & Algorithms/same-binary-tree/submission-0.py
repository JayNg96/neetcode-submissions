# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def _dfs(node, arr):
            if not node:
                arr.append(None)
                return

            arr.append(node.val)
            _dfs(node.left, arr)
            _dfs(node.right, arr)
            return arr

        return _dfs(p, []) == _dfs(q, [])

