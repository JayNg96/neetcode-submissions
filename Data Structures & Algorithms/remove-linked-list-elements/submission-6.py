# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            temp = head.next
            head = None
            head = temp

        if not head:
            return head
        
        slow = head
        fast = head.next

        while fast:
            if fast.val == val:
                slow.next = fast.next
                fast = fast.next
            else:
                slow = slow.next
                fast = fast.next
        
        return head