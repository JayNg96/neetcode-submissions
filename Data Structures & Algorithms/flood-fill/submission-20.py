class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        first_pixel_color = image[sr][sc]
        rows=len(image)
        cols=len(image[0])

        def _dfs(sr:int, sc:int) -> None:
            if sr < 0 or sc < 0:
                return

            if sr == rows or sc == cols:
                return

            if image[sr][sc] == color:
                return 

            if image[sr][sc] != first_pixel_color:
                return
            
            image[sr][sc] = color

            _dfs(sr + 1, sc)
            _dfs(sr - 1, sc)
            _dfs(sr, sc + 1)
            _dfs(sr, sc - 1)

        _dfs(sr = sr, sc = sc)
        return image

