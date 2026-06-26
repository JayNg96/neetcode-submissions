class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        rotten_fruits_q = deque()
        fresh_fruits = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    rotten_fruits_q.append((r, c))    
        
        timer = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while rotten_fruits_q and fresh_fruits:
            for _ in range(len(rotten_fruits_q)):
                r, c = rotten_fruits_q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                        continue
                    
                    if grid[nr][nc] == 0:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten_fruits_q.append((nr, nc))
                        fresh_fruits -= 1
            timer += 1
        
        return timer if not fresh_fruits else -1

        