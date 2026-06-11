from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]    
         
        left_preorder = preorder[1 : len(left_inorder) + 1]
        right_preorder = preorder[1 + len(left_inorder):]       

        left_subtree = self.buildTree(left_preorder, left_inorder)
        right_subtree = self.buildTree(right_preorder, right_inorder)
        
        root.left = left_subtree
        root.right = right_subtree
        
        return root