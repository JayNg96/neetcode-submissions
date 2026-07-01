class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.dummy_head = ListNode(-1)
        self.dummy_tail = ListNode(-1)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def isEmpty(self) -> bool:
        return self.dummy_head.next == self.dummy_tail

    def append(self, value: int) -> None:
        curr = self.dummy_tail.prev
        new_node = ListNode(value)
        new_node.next = curr.next
        new_node.prev = curr
        curr.next = new_node
        self.dummy_tail.prev = new_node

    def appendleft(self, value: int) -> None:
        curr = self.dummy_head.next
        new_node = ListNode(value)
        new_node.next = curr
        new_node.prev = curr.prev
        curr.prev = new_node
        self.dummy_head.next = new_node

    def pop(self) -> int:
        if self.isEmpty(): return -1
        curr = self.dummy_tail.prev
        curr.prev.next = self.dummy_tail
        self.dummy_tail.prev = curr.prev
        return curr.val
        
    def popleft(self) -> int:
        if self.isEmpty(): return -1
        curr = self.dummy_head.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        return curr.val
