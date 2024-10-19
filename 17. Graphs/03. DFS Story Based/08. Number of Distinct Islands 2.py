"""
08. Number of Distinct Islands 2.py


HANDLE :
1. ROTATION + REFLECTION
You can apply rotation matrix = [[+cos(t), -sin(t)], [+sin(t), +cos(t)]] or draw a simple picture like the following to figure out the 4 rotated coordinates:

    rotate_0 = [+r, +c]; rotate_90 = [-c, +r]; rotate_180 = [-r, -c]; rotate_270 = [+c, -r]

2. In fact, this problem requires another 4 reflected coordinates along r-axis, c-axis, r=c line, r=-c line:
    reflecte_r = [-r, +c]; reflect_c = [+r, -c]; reflect_rc = [+c, +r]; reflect_minus_rc = [-c, -r]
Together, all 8 combinations of (+-r, +-c) and (+-c, +-r) will be used as possible transformations.
Python does not support "set of sets" because the inner set needs to be immutable to be hashable. Instead, we can use the immutable frozenset as the inner set to form "set of frozensets".


WIKI LINK :: https://en.wikipedia.org/wiki/Rotation_matrix
In linear algebra, a rotation matrix is a transformation matrix that is used to perform a rotation in Euclidean space. For example, using the convention below, the matrix

    R = [ cos ⁡ θ − sin ⁡ θ sin ⁡ θ cos ⁡ θ ] {\displaystyle R={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}}

rotates points in the xy plane counterclockwise through an angle θ about the origin of a two-dimensional Cartesian coordinate system. To perform the rotation on a plane point with standard coordinates v = (x, y), it should be written as a column vector, and multiplied by the matrix R:

    R v = [ cos ⁡ θ − sin ⁡ θ sin ⁡ θ cos ⁡ θ ] [ x y ] = [ x cos ⁡ θ − y sin ⁡ θ x sin ⁡ θ + y cos ⁡ θ ] . {\displaystyle R\mathbf {v} ={\begin{bmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{bmatrix}}{\begin{bmatrix}x\\y\end{bmatrix}}={\begin{bmatrix}x\cos \theta -y\sin \theta \\x\sin \theta +y\cos \theta \end{bmatrix}}.}

If x and y are the endpoint coordinates of a vector, where x is cosine and y is sine, then the above equations become the trigonometric summation angle formulae. Indeed, a rotation matrix can be seen as the trigonometric summation angle formulae in matrix form. One way to understand this is to say we have a vector at an angle 30° from the x axis, and we wish to rotate that angle by a further 45°. We simply need to compute the vector endpoint coordinates at 75°. 

"""
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_len = len(grid)
        col_len = len(grid[0])
        DIRECTIONS = [ [0,1], [1,0], [0,-1], [-1,0] ]
        visited = [[0 for _ in range(col_len)] for _ in range(row_len)]

        def dfs(row, col, path: List[Tuple[int, int]]) -> None:
            for x, y in DIRECTIONS:
                nrow = row + x
                ncol = col + y
                if nrow < 0 or ncol < 0 or nrow>=row_len or ncol>=col_len:
                    continue
                if grid[nrow][ncol] == 0 or visited[nrow][ncol] == 1:
                    continue
                visited[nrow][ncol] = 1
                path.append((nrow, ncol))
                dfs(nrow, ncol, path)
            return
        def normalize(path_list: List[Tuple[int, int]]) -> FrozenSet[List[Tuple[int, int]]]: 
            rows, cols = zip(*path_list)
            r_min, c_min = min(rows), min(cols)
            return frozenset([(r-r_min, c-c_min) for r,c in path_list])

        distinct_islands = set()
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and not visited[row][col]:
                    path = []
                    transformations = []
                    path.append((row, col))
                    visited[row][col] = 1
                    dfs(row, col, path)
                    # 4 Rotations    
                    # rotate_0 = [+r, +c];
                    r0 = normalize([(+r,+c) for  r,c in path])
                    transformations.append(r0)
                    # rotate_90 = [-c, +r];
                    r1 = normalize([(-c,+r) for  r,c in path])
                    transformations.append(r1)
                    # rotate_180 = [-r, -c];
                    r2 = normalize([(-r,-c) for  r,c in path])
                    transformations.append(r2)
                    # rotate_270 = [+c, -r]
                    r3 = normalize([(+c, -r) for  r,c in path])
                    transformations.append(r3)
                    # 4 Reflections
                    # 4 reflected coordinates along r-axis, c-axis, r=c line, r=-c line:
                    # reflecte_r = [-r, +c]; reflect_c = [+r, -c]; reflect_rc = [+c, +r]; reflect_minus_rc = [-c, -r]
                    r4 = normalize([(-r, +c) for  r,c in path])
                    transformations.append(r4)
                    r5 = normalize([(+r, -c) for  r,c in path])
                    transformations.append(r5)
                    r6 = normalize([(+c, +r) for  r,c in path])
                    transformations.append(r6)
                    r7 = normalize([(-c, -r) for  r,c in path])
                    transformations.append(r7)
                    distinct_islands.add(frozenset(transformations))
        return len(distinct_islands)

