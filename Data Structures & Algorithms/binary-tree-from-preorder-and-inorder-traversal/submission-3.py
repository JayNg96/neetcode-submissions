# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder first item is the root
        # we need to split pre-order into left and right based on inorder
        # so that we can recursively go through the list and insert based on left and right of root.
        # how it works is that the left side of the root is going to be empty when we finish inserting.
        # then assign our root's left and right respectively.
        # we want our recursion to return the root each time so that we can travel back up the tree
        
        if not preorder:
            return None

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

        
