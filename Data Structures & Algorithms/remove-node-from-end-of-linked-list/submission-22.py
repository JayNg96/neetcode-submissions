# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        if not head.next:
            return None
        
        curr = head
        
        count = 0
        while curr:
            curr = curr.next
            count += 1
        
        count -= n

        curr = head
        if count == 0:
            temp = curr
            curr = curr.next
            temp = None
            return curr

        for _ in range(count - 1):
            curr = curr.next

        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head
