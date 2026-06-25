class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [ [0,1], [0,-1], [1,0], [-1,0], [1, 1], [1,-1], [-1,1], [-1,-1] ]
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))

        def _bfs() -> int:
            length = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if r == ROWS - 1 and c == COLS - 1:
                        return length

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc


                        if nr < 0 or nc < 0:
                            continue
                         
                        if nr == ROWS or nc == COLS:
                            continue

                        if (nr, nc) in visited:
                            continue

                        if grid[nr][nc] == 1:
                            continue

                        visited.add((nr, nc))
                        queue.append((nr, nc))
                length += 1

            return -1

        get_shortest_path = _bfs()
        return get_shortest_path
        
