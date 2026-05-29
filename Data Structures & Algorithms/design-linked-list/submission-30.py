class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.dummy_tail = ListNode(-999) 
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head 
        self.size = 0
    
    # may be a good idea to create a private method that travest through the nodes list and return a specific node
    def _getNode(self, index):
        curr = self.dummy_head.next
        for _ in range(index):  
            curr = curr.next
        return curr
            
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self._getNode(index)
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        # remember to get a temporary variable to save the value of the new node before linking it
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        curr = self._getNode(index)
        new_node = ListNode(val)
        new_node.next = curr
        new_node.prev = curr.prev
        
        
        curr.prev.next = new_node
        curr.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:    
        if index < 0 or index >= self.size:  
            return
        
        curr = self._getNode(index)
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.size -= 1     
    