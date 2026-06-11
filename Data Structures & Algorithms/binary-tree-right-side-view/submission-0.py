from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        node_que = deque([root])
        node_list = []
        last_node = None
        
        level = 0
        while node_que:
            print('level:', level)      
            for _ in range(len(node_que)):
                node = node_que.popleft()
                last_node = node.val
                print(node.val)
                if node.left:
                    node_que.append(node.left)      
                if node.right:
                    node_que.append(node.right)
            level += 1
            if last_node:
                node_list.append(last_node)     

        print(node_list)

        return node_list
