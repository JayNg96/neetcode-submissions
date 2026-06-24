class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        first_pixel_color = image[sr][sc]
        rows=len(image)
        cols=len(image[0])

        def _dfs(image=image, sr=sr, sc=sc):
            if min(sr, sc) < 0:
                return

            if sr == rows or sc == cols:
                return

            if image[sr][sc] == color:
                return 

            if image[sr][sc] != first_pixel_color:
                return
            
            image[sr][sc] = color

            _dfs(image, sr + 1, sc)
            _dfs(image, sr - 1, sc)
            _dfs(image, sr, sc + 1)
            _dfs(image, sr, sc - 1)

        _dfs()
        return image

