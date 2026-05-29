#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr: #1 next 2 next 3
            #1 next 2
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev