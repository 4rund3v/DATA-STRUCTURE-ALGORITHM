"""
Problem Statement:
    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
    The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 
    4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim 
    infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

    Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Time Complexity: O(N^2 * log(N^2))
        - In the worst case, we might visit all N^2 cells
        - Each heap operation (push or pop) takes log(N^2) time
        - Therefore, the overall time complexity is O(N^2 * log(N^2))

Space Complexity: O(N^2)
        - O(N^2) for the visited set in the worst case
        - O(N^2) for the priority queue in the worst case
        - Therefore, the overall space complexity is O(N^2)

where N is the side length of the grid.
"""

"""
The Problem is described as a modified version of Dijkstra's algorithm, or a combination of Dijkstra's algorithm and a Best-First Search. Here's why:

Similarity to Dijkstra's:

    It uses a priority queue to always explore the "cheapest" path first.
    It maintains a set of visited nodes to avoid revisiting.

Differences from classic Dijkstra's:

    In Dijkstra's, we typically update distances to all nodes and potentially revisit nodes if we find a shorter path.
    This algorithm doesn't maintain a distance array for all nodes and doesn't revisit nodes.
    The "cost" in this problem (max height) doesn't accumulate like in typical Dijkstra's; instead, it takes the maximum value along the path.

Similarity to Best-First Search:

    It explores nodes based on a heuristic (in this case, the maximum height encountered).
    It doesn't revisit nodes, which is more characteristic of best-first search algorithms.

"""

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # Priority queue to store cells to visit: (max_height, row, col)
        # We use max_height as the priority to always explore the path with the lowest maximum height first
        pq = [(grid[0][0], 0, 0)]  # (max_height, row, col)
        # Set to keep track of visited cells
        visited = set()
        visited.add((0, 0))

        # Possible directions to move: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            # Get the cell with the lowest maximum height so far
            max_height, row, col = heapq.heappop(pq)
            
            # If we've reached the bottom-right cell, we're done
            if row == n - 1 and col == n - 1:
                return max_height
            
            # Explore all adjacent cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new cell is within the grid and not visited
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    # Mark the new cell as visited
                    visited.add((new_row, new_col))
                    
                    # Calculate the new maximum height
                    # It's the max of the current max_height and the height of the new cell
                    new_max_height = max(max_height, grid[new_row][new_col])
                    
                    # Add the new cell to the priority queue
                    heapq.heappush(pq, (new_max_height, new_row, new_col))
        
        # We should never reach here given the problem constraints
        return -1

# Test the solution
solution = Solution()
print(solution.swimInWater([[0,2],[1,3]]))  # Output: 3
print(solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))  # Output: 16