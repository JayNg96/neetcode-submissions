class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def _dfs(r, c):
            if r < 0 or c < 0:
                return 0
            
            if r == rows or c == cols:
                return 0 

            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            return 1 + _dfs(r + 1, c) \
                     + _dfs(r - 1, c) \
                     + _dfs(r, c + 1) \
                     + _dfs(r, c - 1)
        
        mx_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    mx_area = max(mx_area, _dfs(r, c))

        return mx_area

