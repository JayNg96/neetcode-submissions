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
        

        print(count)
        new_curr = head
        if count == 0:
            temp = new_curr
            new_curr = new_curr.next
            temp = None
            return new_curr

        for _ in range(count - 1):
            new_curr = new_curr.next

        print(new_curr.val)

        if new_curr.next.next:
            new_curr.next = new_curr.next.next
        else:
            new_curr.next = None
        
        return head
