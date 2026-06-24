class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        first_pixel_color = image[sr][sc]

        def _dfs(image=image, sr=sr, sc=sc, color=color, visited=set(), rows=len(image) - 1, cols=len(image[0]) - 1):
            # print("sr", sr)
            # print("sc", sc)
            # print("image", image)
            # print("row",rows)
            # print("col",cols)
    
            # if ( min(sr, sc) < 0 or
            #      sr > row or sc > col or
            #      ( sr, sc ) in visited or
            #      image[sr][sc] != starting_pixel_color
            # ): return

            if min(sr, sc) < 0:
                return

            if sr > rows or sc > cols:
                return

            if ( sr, sc ) in visited:
                return

            if image[sr][sc] != first_pixel_color:
                return


            image[sr][sc] = color

            visited.add( (sr, sc) )

            _dfs(image, sr + 1, sc=sc, visited=visited)
            _dfs(image, sr - 1, sc=sc, visited=visited)
            _dfs(image, sr, sc + 1, visited=visited)
            _dfs(image, sr, sc - 1, visited=visited)

            visited.remove( (sr, sc) )
            return

        _dfs()
        return image

