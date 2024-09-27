"""
Floyd-Warshall Algorithm Implementation

    This algorithm finds the shortest paths between all pairs of vertices in a weighted graph.
    It can handle graphs with negative edge weights, but not negative cycles.

Time Complexity: O(V^3), where V is the number of vertices.
Space Complexity: O(V^2) for the distance matrix.

Parameters:
    - n: Number of vertices in the graph
    - edges: List of edges, where each edge is [u, v, w] (u: source, v: destination, w: weight)

Returns:
     of shortest distances between all pairs of vertices, or None if a negative cycle is detected.

Note: Vertex indexing starts from 0.
"""

from typing import List

class Solution:
    def floyd_warshall(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0  # Distance from a vertex to itself is 0
        
        # Set the initial distances for the given edges
        for u, v, w in edges:
            dist[u][v] = w
        
        # Floyd- Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Check for negative cycles
        for i in range(n):
            if dist[i][i] < 0:
                return None  # Negative cycle detected
        
        # Replace infinity with -1 for unreachable nodes
        return [[-1 if d == float('inf') else d for d in row] for row in dist]
        ## OR 
        # Replace infinity with -1 for unreachable nodes (expanded form)
        # result = []
        # for row in dist:
        #     new_row = []
        #     for d in row:
        #         if d == float('inf'):
        #             new_row.append(-1)
        #         else:
        #             new_row.append(d)
        #     result.append(new_row)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: Graph without negative cycle
    n1 = 4
    edges1 = [[0,1,3], [1,2,-2], [2,3,1], [3,0,4], [0,2,5]]
    print("Example 1 output:")
    result1 = solution.floyd_warshall(n1, edges1)
    for row in result1:
        print(row)
    
    # Example 2: Graph with negative cycle
    n2 = 3
    edges2 = [[0,1,1], [1,2,-1], [2,0,-1]]
    print("\nExample 2 output:")
    result2 = solution.floyd_warshall(n2, edges2)
    print(result2)
    
    # Example 3: Graph with unreachable nodes
    n3 = 4
    edges3 = [[0,1,1], [1,2,2], [2,3,3]]
    print("\nExample 3 output:")
    result3 = solution.floyd_warshall(n3, edges3)
    for row in result3:
        print(row)