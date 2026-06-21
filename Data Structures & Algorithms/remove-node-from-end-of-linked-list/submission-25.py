# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        if not head:
            return None
        
        curr = head
        
        count = 0
        while curr:
            curr = curr.next
            count += 1
        
        count -= n

        curr = head
        if count == 0:
            return head.next

        for _ in range(count - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head
