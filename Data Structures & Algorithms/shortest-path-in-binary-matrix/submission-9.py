class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        adj = [ [0,1], [0,-1], [1,0], [-1,0], [1, 1], [1,-1], [-1,1], [-1,-1] ]
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

                    for ar, ac in adj:
                        row_diff = r + ar
                        col_diff = c + ac


                        if row_diff < 0 or col_diff < 0:
                            continue
                         
                        if row_diff == ROWS or col_diff == COLS:
                            continue

                        if (row_diff, col_diff) in visited:
                            continue

                        if grid[row_diff][col_diff] == 1:
                            continue

                        visited.add((row_diff, col_diff))
                        queue.append((row_diff, col_diff))
                length += 1

            return -1

        get_shortest_path = _bfs()
        return get_shortest_path
        
