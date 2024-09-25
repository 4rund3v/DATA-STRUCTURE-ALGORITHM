"""
Problem: Path With Minimum Effort

You are given a 2D array 'heights' where heights[row][col] represents the height of cell (row, col).
Find a path from the top-left cell to the bottom-right cell that minimizes the maximum absolute
difference in heights between consecutive cells of the path.

Return the minimum effort required for such a path.

Time Complexity: O(m * n * log(m * n)), where m and n are the dimensions of the grid.
Space Complexity: O(m * n) for the result matrix and priority queue.

Constraints:
- 1 <= m, n <= 100
- 1 <= heights[i][j] <= 10^6
"""

from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        # Interesting representation of directions
        dirs = [
                    [-1, 0],
            [0, -1],        [0, 1],
                    [1, 0]
        ]
        
        def isSafe(x: int, y: int) -> bool:
            return 0 <= x < m and 0 <= y < n
        
        result = [[float('inf')] * n for _ in range(m)]
        pq = [(0, 0, 0)]  # (diff, x, y)
        result[0][0] = 0
        
        while pq:
            diff, x, y = heapq.heappop(pq)
            
            # Early return when reaching the destination
            if x == m - 1 and y == n - 1:
                return diff
            
            for dx, dy in dirs:
                x_, y_ = x + dx, y + dy
                if isSafe(x_, y_):
                    newDiff = max(diff, abs(heights[x][y] - heights[x_][y_]))
                    if result[x_][y_] > newDiff:
                        result[x_][y_] = newDiff
                        heapq.heappush(pq, (newDiff, x_, y_))
        
        return result[m-1][n-1]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    heights1 = [[1,2,2],[3,8,2],[5,3,5]]
    print("Example 1 output:", solution.minimumEffortPath(heights1))
    
    # Example 2
    heights2 = [[1,2,3],[3,8,4],[5,3,5]]
    print("Example 2 output:", solution.minimumEffortPath(heights2))
    
    # Example 3
    heights3 = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    print("Example 3 output:", solution.minimumEffortPath(heights3))