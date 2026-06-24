class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])


        def _dfs(r, c, visited):
            if r < 0 or c < 0:
                return
            
            if r == rows or c == cols:
                return

            if (r, c) in visited:
                return

            if grid[r][c] == 0:
                return
            
            visited.add( (r, c) )

            _dfs(r + 1, c, visited)
            _dfs(r - 1, c, visited)
            _dfs(r, c + 1, visited)
            _dfs(r, c - 1, visited)
            
            return len(visited)
        
        mx_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    mx_area = max(mx_area, _dfs(r, c, set()))

        return mx_area

