class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def _dfs(r, c):
            if r < 0 or c < 0:
                return 0
            
            if r == rows or c == cols:
                return 0

            if ( r, c ) in visited:
                return 0

            if grid[r][c] == "0":
                return 0

            visited.add( (r, c) )
                
            _dfs(r+1, c)
            _dfs(r-1, c)
            _dfs(r, c+1)
            _dfs(r, c-1)

            return 1
            
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and ( r, c ) not in visited:
                    count += _dfs(r=r, c=c)

        return count


