# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = fast
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_half = None
        while slow:
            temp = slow.next
            slow.next = reversed_half
            reversed_half = slow
            slow = temp

        head_pointer = head
        tail_pointer = reversed_half
        while tail_pointer and head_pointer:
            if head_pointer.val != tail_pointer.val:
                return False
            head_pointer, tail_pointer = head_pointer.next, tail_pointer.next

        return True
        
