"""
Problem Statement:
    You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. 
    Find the shortest weight path between the vertex 1 and the vertex n, if there exists a path, and return a list of integers 
    whose first element is the weight of the path, and the rest consist of the nodes on that path. 
    
    If no path exists, then return a list containing a single element -1.

    The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note:   The driver code will first check if the weight of the path returned is equal to the sum of the weights along the nodes 
        on that path. If equal, it will output the weight of the path, else -2. In case the list contains only a single element (-1) 
        it will simply output -1.

Time Complexity: O(m * log(n)), where m is the number of edges and n is the number of vertices.
Space Complexity: O(n + m) for the adjacency list, distances list, previous list, and priority queue.

Constraints:
    - 2 <= n <= 10^6
    - 0 <= m <= 10^6
    - 1 <= a, b <= n
    - 1 <= w <= 10^5
"""

from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Create adjacency list
        graph = [[] for _ in range(n+1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Initialize distances and previous nodes
        distances = [float('inf')] * (n+1)
        distances[1] = 0
        previous = [None] * (n+1)
        
        # Priority queue to store vertices to visit
        pq = [(0, 1)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            # If we've reached the target node
            if current_node == n:
                break
            
            # If we've already found a shorter path, skip
            if current_distance > distances[current_node]:
                continue
            
            # Check all neighbors of the current node
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                # If we've found a shorter path to the neighbor, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        # If no path exists to node n
        if distances[n] == float('inf'):
            return [-1]
        
        # Reconstruct the path
        path = []
        current = n
        while current:
            path.append(current)
            current = previous[current]
        path.reverse()
        
        # Return the weight of the path and the path itself
        return [distances[n]] + path

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # n: The number of vertices (nodes) in the graph.
    # m: The number of edges in the graph.
    # Example 1
    n1, m1 = 5, 6
    edges1 = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
    print("Example 1 output:", solution.shortestPath(n1, m1, edges1))
    
    # Example 2
    n2, m2 = 2, 1
    edges2 = [[1, 2, 2]]
    print("Example 2 output:", solution.shortestPath(n2, m2, edges2))
    
    # Example 3
    n3, m3 = 2, 0
    edges3 = []
    print("Example 3 output:", solution.shortestPath(n3, m3, edges3))