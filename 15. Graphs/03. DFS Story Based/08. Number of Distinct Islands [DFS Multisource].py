"""
694. Number of Distinct Islands
Solved


You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:

Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:

Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.



Time Complexity: O(M⋅N).
Space Complexity: O(M⋅N).

Remember how we didn't need to sort islands in Approach 1? When we start a depth-first search on the top-left square of some island, the path taken by our depth-first search will be the same if, and only if, the shape is the same. We can exploit this by using the path as a hash.

Each time we discover the first cell in a new island, we initialize an empty string. Then each time dfs is called for that island, we first determine whether or not the cell being entered is un-visited land, in the same way as before. If it is, then we append the direction we entered it from to the string. For example, this is the path that our algorithm would follow to explore the following island.
This path will be encoded as "RDDRUURRUL".

There's one thing we need to be cautious of. The three islands below would have the same encoding of RDDDR.
The solution to this is that we also need to record where we backtracked. This occurs each time we exit a call to the dfs(...) function. We'll do this by appending a 0 to the string.
In this way, the islands will now have the encodings of RDDDR, RDDD0R, and RDDD00R.
"""


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        Traverse each of the islands, then store the shape of the island
        number of distinct shapes of the islands indicate the total distinct count
        """
        if not grid:
            return 0
        row_len = len(grid)
        col_len = len(grid[0])
        DIRECTIONS = [(0,1, "U"),  (1,0, "R"), (0,-1, "D"), (-1,0,"L"),  ]
        visited = [[0 for _ in range(col_len)] for _ in range(row_len)]
        shapes = set([])
        def dfs(row, col, path_directions):
            for x, y, direc in DIRECTIONS:
                nrow = x+row
                ncol = y+col
                if nrow < 0 or ncol < 0 or nrow >= row_len or ncol >= col_len:
                    continue
                if grid[nrow][ncol] == 0 or visited[nrow][ncol] == 1:
                    continue
                path_directions.append(direc)
                visited[nrow][ncol] = 1
                dfs(nrow, ncol, path_directions)
            path_directions.append("0")
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and not visited[row][col]:
                    path_directions = ["0"]                    
                    dfs(row, col, path_directions)
                    shapes.add("".join(path_directions))
        return len(shapes)