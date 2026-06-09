from typing import Optional
#Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def _find_inorder_successor(root: Optional[TreeNode]) -> Optional[TreeNode]:
            ''' takes in the root's right after we found the key and after we checked if it has 2 childrens
                keep track of current node and save it to prev after we know we need to continue travel i.e currentNode.left not None
                travel down left of the root until currentNode.left is None
                set prev.left = currentNode.right if currentNode.right else None
                return currentNode 
            '''
            curr_node = root
            prev_node = None
            while curr_node:
                if curr_node.left:
                    prev_node = curr_node
                    curr_node = curr_node.left
                else:
                    if prev_node:
                        prev_node.left = curr_node.right if curr_node.right else None
                    return curr_node
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                curr_temp = root
                root = _find_inorder_successor(root.right)
                root.left = curr_temp.left
                if curr_temp.right != root:
                    root.right = curr_temp.right
            elif root.left:
                root = root.left
            else:
                root = root.right
        return root