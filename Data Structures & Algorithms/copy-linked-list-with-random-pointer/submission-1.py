"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        hash_map = {}

        curr = head
        while curr:
            new_node = Node(curr.val)
            hash_map[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = hash_map[curr]
            if curr.next:
                new_node.next = hash_map[curr.next]
            if curr.random:
                new_node.random = hash_map[curr.random]
            curr = curr.next
        
        return hash_map[head]

            