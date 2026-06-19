# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def _dfs(root):
            if not root:
                return

            _dfs(root.left)
            _dfs(root.right)
            res.append(root.val)

        _dfs(root)

        return res