from typing import Optional
#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def _find_inorder_successor(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while node and node.left:
                node = node.left
            return node
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left or not root.right:
                return root.left if root.left else root.right
            else:
                successor = _find_inorder_successor(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        return root