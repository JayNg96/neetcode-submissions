# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_value = []

        def _dfs(node: Optional[TreeNode]):
            if not node or len(node_value) == k:
                return
            
            _dfs(node.left)
            node_value.append(node.val)
            _dfs(node.right)
        
        _dfs(root)
        return node_value[k-1]
            
            
