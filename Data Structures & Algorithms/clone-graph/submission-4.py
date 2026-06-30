"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # hashmap -> to store original node : cloned node
        # queue   -> push the first node (after creating it) and then process it via bfs level by level
        # pop queue, and use for loop to process neighbours by levels
        # if node not in hashmap, create it. push the original to queue to process it since we know that it wasn't in hashmap hence it hasn't been processed for neighbors aswell
        # once we created the neighbors node, we can then append it to the root node
        
        old_to_new = {}
        q = deque()
        q.append(node)
        new_node = Node(node.val)
        old_to_new[node] = new_node

        while q:
            old_node = q.popleft()

            for neighbor in old_node.neighbors:

                if neighbor not in old_to_new:
                    new_node = Node(neighbor.val)
                    q.append(neighbor)
                    old_to_new[neighbor] = new_node

                old_to_new[old_node].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]








