class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (2 ** 31) - 1
        treasure_que = deque()
        visited = set()
        
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure_que.append((r,c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while treasure_que:
            for _ in range(len(treasure_que)):
                r, c = treasure_que.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if (nr, nc) in visited:
                        continue

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                        continue

                    if grid[nr][nc] == -1 or grid[nr][nc] == 0:
                        continue
                    

                    grid[nr][nc] = grid[r][c] + 1
                        
                    visited.add((nr,nc))
                    treasure_que.append((nr, nc))