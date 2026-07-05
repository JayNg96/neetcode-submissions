# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False

            return valid(node = node.left, low = low, high = node.val) and valid(node = node.right, low = node.val, high = high)
        
        return valid(root, float('-inf'), float('inf'))

            
  