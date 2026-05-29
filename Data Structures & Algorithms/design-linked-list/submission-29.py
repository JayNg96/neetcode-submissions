class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0) 
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.left.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        curr = self.left
        for _ in range(index):
            curr = curr.next
        
        new_node = ListNode(val)
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.left.next
        for _ in range(index):
            curr = curr.next

        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1