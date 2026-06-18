# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy_head = head
        fast = dummy_head
        slow = fast
        prev = None
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev and dummy_head:
            if dummy_head.val != prev.val:
                return False
            dummy_head, prev = dummy_head.next, prev.next

        return True
        
