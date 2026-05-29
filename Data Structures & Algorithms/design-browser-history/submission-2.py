from typing import Optional

class ListNode:
    def __init__(self, url='.', next=None, prev=None):
        self.url = url.lower()
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy_head = ListNode(homepage)
        self.dummy_tail = ListNode('Dummy Tail')
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.history_size = 0
        self.history_backed_times = 0
        
    def _isUrlValid(self, url: str) -> bool:
        return '.' in url and len(url) > 0 and len(url) <= 20
    
    def _getUrl(self, steps: int) -> Optional[ListNode]:
        if self.history_size < steps:
            print('No URL')
            return
            
        curr = self.dummy_head
        for _ in range(steps):
            curr = curr.next
        return curr
    
    def visit(self, url: str) -> None:
        if not self._isUrlValid(url):
            return
        
        curr = self._getUrl(self.history_size - self.history_backed_times)
        
        new_visit = ListNode(url)
        new_visit.next = self.dummy_tail
        new_visit.next.prev = new_visit
        new_visit.prev = curr
        
        curr.next = new_visit
        self.history_size += 1
        if self.history_backed_times:
            self.history_size -= self.history_backed_times   
        self.history_backed_times = 0
        
    def back(self, steps: int) -> str:
        if self.history_size == self.history_backed_times:
            steps = 0
        back_steps = self.history_size - (steps + self.history_backed_times)
        
        curr = self._getUrl(back_steps)
        self.history_backed_times += steps
        return curr.url

    def forward(self, steps: int) -> str:     
        if steps > self.history_backed_times:
            steps = self.history_backed_times
        
        curr = self._getUrl(self.history_size - self.history_backed_times + steps)
        if self.history_backed_times > 0:
            self.history_backed_times -= steps
        return curr.url

