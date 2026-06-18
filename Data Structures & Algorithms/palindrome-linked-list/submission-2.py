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
        reversed_half = None
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        while slow:
            temp = slow.next
            slow.next = reversed_half
            reversed_half = slow
            slow = temp

        while reversed_half and dummy_head:
            if dummy_head.val != reversed_half.val:
                return False
            dummy_head, reversed_half = dummy_head.next, reversed_half.next

        return True
        
