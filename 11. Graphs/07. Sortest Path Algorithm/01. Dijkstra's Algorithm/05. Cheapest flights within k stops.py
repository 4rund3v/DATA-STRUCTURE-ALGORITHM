"""
Problem Statement:
    There are n cities connected by some number of flights. You are given an array flights where 
    flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
    If there is no such route, return -1.

Time Complexity: O((N + E) * log(N)), where N is the number of cities and E is the number of flights.
                In the worst case, this could be O(N^2 * log(N)) if the graph is dense (i.e., there are flights between every pair of cities).

Space Complexity: O(N + E)
    - O(N) for the distances and stops arrays
    - O(E) for the graph adjacency list
    - O(N) for the priority queue in the worst case

The total space complexity is therefore O(N + E).
"""

"""
Similarity to Dijkstra's algorithm:

    Use of a priority queue to always explore the cheapest path first
    Maintaining a list of minimum costs to reach each node
    Exploring neighbors and updating costs


Key differences from standard Dijkstra:

    ***Addition of a stops counter
    **Allowing revisiting of nodes if we can reach them with fewer stops
    Early termination when we reach the destination (not necessarily finding all shortest paths)

The main difference is the handling of the 'k' constraint (maximum number of stops). 
In standard Dijkstra's algorithm, once we visit a node, we're guaranteed to have found the shortest path to that node. 
In this problem, we might find a cheaper path later that uses more stops, so we need to continue exploring.

This algorithm is sometimes referred to as a modified Dijkstra's algorithm or a BFS (Breadth-First Search) with a priority queue. It combines elements of both:
    From Dijkstra's: Use of a priority queue to always explore the cheapest path first
    From BFS: The level-wise exploration (here, levels correspond to the number of stop

"""

from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for fromi, toi, pricei in flights:
            graph[fromi].append((toi, pricei))
        
        # Initialize distances and stops
        distances = [float('inf')] * n
        stops = [float('inf')] * n
        distances[src] = 0
        stops[src] = 0
        
        # Priority queue to store vertices to visit
        pq = [(0, 0, src)]  # (price, stops, node)
        
        while pq:
            current_price, current_stops, current_node = heapq.heappop(pq)
            
            # If we've reached the destination, return the price
            if current_node == dst:
                return current_price
            
            # If we've exceeded the number of stops, continue to the next iteration
            if current_stops > k:
                continue
            
            # Check all neighbors of the current node
            for neighbor, price in graph[current_node]:
                new_price = current_price + price
                new_stops = current_stops + 1
                
                # If we've found a cheaper path or a path with fewer stops, update it
                if new_price < distances[neighbor] or new_stops < stops[neighbor]:
                    distances[neighbor] = new_price
                    stops[neighbor] = new_stops
                    heapq.heappush(pq, (new_price, new_stops, neighbor))
        
        # If we can't reach the destination within k stops, return -1
        return -1 if distances[dst] == float('inf') else distances[dst]

# Test the function with the given examples
solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # Output: 700
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # Output: 200
print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # Output: 500



