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
            
        node_queue = deque([root])
        node_list = []

        level = 0
        while node_queue:
            node_list.append([])
            for _ in range(len(node_queue)):
                node = node_queue.popleft()
                node_list[level].append(node.val)

                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)    
            level += 1

        return node_list
