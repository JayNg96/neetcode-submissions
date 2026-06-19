# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        preorder_list = []
        def _dfs(root):
            if not root:
                return

            preorder_list.append(root.val)
            _dfs(root.left)
            _dfs(root.right)


        _dfs(root)
        return preorder_list