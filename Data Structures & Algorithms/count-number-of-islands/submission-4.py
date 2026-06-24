class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def _dfs(r, c):
            if r < 0 or c < 0:
                return
            
            if r == rows or c == cols:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
                
            _dfs(r+1, c)
            _dfs(r-1, c)
            _dfs(r, c+1)
            _dfs(r, c-1)
            
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    _dfs(r=r, c=c)
                    count += 1

        return count