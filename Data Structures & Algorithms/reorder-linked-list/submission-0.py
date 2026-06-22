# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow.next
        slow.next = None

        reversed_half = None
        while second_half:
            temp = second_half.next
            second_half.next = reversed_half
            reversed_half = second_half
            second_half = temp
        
        curr = head
        while reversed_half:
            temp_curr = curr.next
            temp_rev = reversed_half.next
            curr.next = reversed_half
            reversed_half.next = temp_curr
            curr, reversed_half = temp_curr, temp_rev

            