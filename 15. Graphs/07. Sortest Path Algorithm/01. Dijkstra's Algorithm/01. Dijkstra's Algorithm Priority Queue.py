"""
Problem Statement:
    Given a weighted, undirected graph, find the shortest path from a starting node to all other nodes 
    in the graph using Dijkstra's algorithm with a priority queue (min-heap) implementation.

Explanation:
    Dijkstra's algorithm finds the shortest path from a starting node to all other nodes in a weighted graph. 
    It uses a priority queue (implemented as a min-heap) to efficiently select the next node to process, 
    always choosing the node with the smallest known distance from the start.

Key steps:
    1. Initialize distances to all nodes as infinity, except the start node (distance 0).
    2. Use a min-heap priority queue to store (distance, node) pairs.
    3. While the priority queue is not empty:
    a. Extract the node with the smallest distance.
    b. For each neighbor of this node:
        - Calculate the distance through the current node.
        - If this distance is less than the known distance to the neighbor, update it.
        - Add the neighbor to the priority queue with its new distance.

Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges.
            - Each vertex is added to and removed from the queue once: O(V log V)
            - Each edge is examined once: O(E log V)

Space Complexity: O(V + E)
            - O(V) for the distances dictionary and the priority queue in the worst case
            - O(E) for storing the graph structure

The use of a min-heap priority queue ensures that we always process the most promising (shortest distance) 
nodes first, which is crucial for the algorithm's correctness and efficiency.
"""

import heapq
from typing import List, Dict, Tuple

class Graph:
    def __init__(self):
        self.graph: Dict[int, List[Tuple[int, int]]] = {}
    
    def add_edge(self, u: int, v: int, weight: int):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

def dijkstra(graph: Graph, start: int) -> Dict[int, int]:
    # Initialize distances
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    
    print(f" printing distances -> {distances}") 
    # Priority queue (min-heap) to store (distance, node) pairs
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph.graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update and add to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 6)
    g.add_edge(4, 5, 3)
    
    start_node = 0
    distances = dijkstra(g, start_node)
    
    print(f"Shortest distances from node {start_node}:")
    for node, distance in sorted(distances.items()):
        print(f"To node {node}: {distance}")