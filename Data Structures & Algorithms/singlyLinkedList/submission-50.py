class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head
        self.length += 1
        if self.length == 1:
            self.tail = new_head

    def insertTail(self, val: int) -> None:  
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        
        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
        if index == self.length - 1:
            self.tail = curr
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        val_list = []
        while curr:
            val_list.append(curr.val)
            curr = curr.next

        return val_list