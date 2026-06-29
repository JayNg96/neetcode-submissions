class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        q = deque()
        q.append((0,0))
        grid[0][0] = 1 # mark as visited
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

        def _get_shortest_path():
            length = 1
            while q:
                for _ in range(len(q)):
                    r , c = q.popleft()
                    if r == rows - 1 and c == cols - 1:
                        return length

                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        
                        if nr < 0 or nc < 0 or nr == rows or nc == cols:
                            continue

                        if grid[nr][nc] != 0:
                            continue

                        grid[nr][nc] = 1 # sink land if 0
                        q.append((nr, nc))
                    
                length += 1

            return -1

                    
        return _get_shortest_path()

