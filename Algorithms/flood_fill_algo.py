# flood_fill_algo.py

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Problem can be solved via bfs and dfs
        """
        if image[sr][sc] == color:
            return image
        row_len = len(image)
        col_len = len(image[0])
        updated_image = image.copy()
        DIRECTIONS = [ (0,1), (0, -1), (-1,0), (1, 0)]
        
        def dfs(row: int, col: int, starting_color: int, new_color:int):
            updated_image[row][col] = new_color
            for x_, y_ in DIRECTIONS:
                nx = row + x_
                ny = col + y_
                # Boundary and validity check
                if nx < 0 or ny < 0 or nx >= row_len or ny >= col_len or \
                   (updated_image[nx][ny] != starting_color):
                   continue
                dfs(nx, ny, starting_color, new_color)
            return

        starting_color = image[sr][sc]
        dfs(sr, sc, starting_color, color)
        return updated_image