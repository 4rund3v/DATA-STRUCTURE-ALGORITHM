"""
Problem Statement:
    You are given a network of n nodes, labeled from 1 to n. 
    You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
    Where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.   
    We will send a signal from a given node k. 
    Return the minimum time it takes for all the n nodes to receive the signal. 
    If it is impossible for all the n nodes to receive the signal, return -1.

Time Complexity: O((N + E) * log(N)), where N is the number of nodes and E is the number of edges.
Space Complexity: O(N + E) for the adjacency list and priority queue.

Constraints:
    - 1 <= k <= n <= 100
    - 1 <= times.length <= 6000
    - times[i].length == 3
    - 1 <= ui, vi <= n
    - ui != vi
    - 0 <= wi <= 100
    - All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize distances
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        
        # Priority queue to store vertices to visit
        pq = [(0, k)]
        
        while pq:
            current_time, current_node = heapq.heappop(pq)
            
            # If we've already found a shorter path, skip
            if current_time > distances[current_node]:
                continue
            
            # Check all neighbors of the current node
            for neighbor, time in graph[current_node]:
                new_time = current_time + time
                
                # If we've found a shorter path to the neighbor, update it
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
        
        # Find the maximum time (excluding node 0 and unreachable nodes)
        # max_time = max(d for i, d in enumerate(distances) if i > 0)
        # as the oth element in the list will always be infinity (zero based index , we are taking n+1 in the calculation )
        max_time = max(distances[1:])
        
        # If any node is unreachable, return -1
        return max_time if max_time < float('inf') else -1

# Example usage
if __name__ == "__main__":
    solution = Solution()
    #n: The number of nodes in the network
    #k: The starting node from which the signal is sent

    # Example 1
    times1 = [[2,1,1],[2,3,1],[3,4,1]]
    n1, k1 = 4, 2
    print("Example 1 output:", solution.networkDelayTime(times1, n1, k1))
    
    # Example 2
    times2 = [[1,2,1]]
    n2, k2 = 2, 1
    print("Example 2 output:", solution.networkDelayTime(times2, n2, k2))
    
    # Example 3
    times3 = [[1,2,1]]
    n3, k3 = 2, 2
    print("Example 3 output:", solution.networkDelayTime(times3, n3, k3))