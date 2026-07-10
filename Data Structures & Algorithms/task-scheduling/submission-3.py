class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counter = Counter(tasks)
        task_queue = deque()
        max_heap = [-c for c in tasks_counter.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while task_queue or max_heap:
            time += 1

            if max_heap:
                task_cooldown = -heapq.heappop(max_heap)
                if task_cooldown > 1:
                    task_queue.append((task_cooldown - 1, time + n))
            
            if task_queue and task_queue[0][1] == time:
                task_remaining_time = task_queue.popleft()[0]
                heapq.heappush(max_heap, -task_remaining_time)

        return time