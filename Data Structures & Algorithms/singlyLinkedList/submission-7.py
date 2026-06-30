class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        curr = self.head
        tmp = curr.next
        new_head = ListNode(val)
        new_head.next = tmp
        curr.next = new_head
        self.length += 1

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr and curr.next.val != -1:
            curr = curr.next
        
        tmp = curr.next
        new_node = ListNode(val)
        new_node.next = tmp
        curr.next = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        
        curr = self.head
        
        for _ in range(index):
            curr = curr.next

        tmp = curr.next.next
        curr.next = tmp
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        if self.length == 0:
            return []

        curr = self.head.next
        val_list = []
        while curr and curr.val != -1:
            val_list.append(curr.val)
            curr = curr.next

        return val_list
