class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotting_fruit_q = deque()
        fresh_fruit = 0
        timer = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    rotting_fruit_q.append((r, c))
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while rotting_fruit_q and fresh_fruit:
            for _ in range(len(rotting_fruit_q)):
                r, c = rotting_fruit_q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if nr < 0 or nc < 0 or nr == rows or nc == cols:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    rotting_fruit_q.append((nr, nc))
                    fresh_fruit -= 1
            timer += 1
        
        return timer if not fresh_fruit else -1
                    



