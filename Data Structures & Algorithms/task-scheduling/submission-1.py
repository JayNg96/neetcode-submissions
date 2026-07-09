class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        tasks_q = deque()
        
        max_heap = [-x for x in task_counter.values()]
        heapq.heapify(max_heap)
        # [-3, -1, -1]

        timer = 0
        while max_heap or tasks_q:
            timer += 1
            
            if max_heap:
                task_count = -heapq.heappop(max_heap)
                if task_count >= 2:
                    tasks_q.append((task_count - 1, timer + n))

            if tasks_q and tasks_q[0][1] == timer:
                ready, _ = tasks_q.popleft()
                heapq.heappush(max_heap, -ready)
        
        return timer
                
