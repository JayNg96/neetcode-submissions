# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def _merge_two_lists(list1, list2):
            dummy_node = ListNode(0)
            curr = dummy_node
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            curr.next = list1 if list1 else list2
            return dummy_node.next

        def _merge(lists):
            if not lists:
                return None

            if len(lists) == 1:
                return lists[0]

            mid = len(lists) // 2
            left = lists[:mid]
            right = lists[mid:]

            merge_left = _merge(left)
            merge_right = _merge(right)

            return _merge_two_lists(merge_left, merge_right)
        
        return _merge(lists=lists)
