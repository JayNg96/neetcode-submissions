from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
            
        node_que = deque()
        node_list = []

        if not node_que:
            node_que.append(root)

        
        level = 0
        while node_que:
            node_list.append([])
            for _ in range(len(node_que)):
                node = node_que.popleft()  
                node_list[level].append(node.val)
                if node.left:
                    node_que.append(node.left)
                if node.right:
                    node_que.append(node.right)
            level += 1

        return node_list
    