# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry_over = 0
        while l1 and l2:
            if l1.val + l2.val + carry_over > 9:
                curr.next = ListNode((l1.val + l2.val + carry_over) % 10)   
            else:
                curr.next = ListNode(l1.val + l2.val + carry_over)
            carry_over = (carry_over + l1.val + l2.val) // 10
            curr, l1, l2 = curr.next, l1.next, l2.next


        left_over = l1 if l1 else l2
        while left_over:
            if left_over.val + carry_over > 9:
                curr.next = ListNode((left_over.val + carry_over) % 10)  
            else:
                curr.next = ListNode(left_over.val + carry_over)
            carry_over = (carry_over + left_over.val) // 10
            curr, left_over = curr.next, left_over.next

        if carry_over:
            curr.next = ListNode(carry_over)

        return dummy.next