from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def _mergeTwoLists(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            dummy_head = ListNode(0)
            curr = dummy_head
            
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            if left:
                curr.next = left
            else:
                curr.next = right
            
            return dummy_head.next                 
        
        def _merge(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if len(lists) == 1:
                return lists[0]
            else:
                mid = len(lists) // 2
                left = lists[:mid]
                right = lists[mid:]
                
                left_merged = _merge(left)
                right_merged = _merge(right)
                return _mergeTwoLists(left_merged, right_merged)

        if not lists:
            return None
        return _merge(lists)