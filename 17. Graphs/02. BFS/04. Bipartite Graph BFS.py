"""
785. Is Graph Bipartite?

- linear graph is bipartite
- graph with cycle - it has to have a even length cycle to be bipartite

Solved
Medium
Topics
Companies
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.

"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import defaultdict, deque

        ROW_LEN = len(graph)
        COL_LEN = len(graph[0])
        visited = [-1 for _ in range(ROW_LEN)]
        adj_list = defaultdict(set)
        for row_index, row in enumerate(graph):
            for col_index, col in enumerate(row):
                if row_index == graph[row_index][col_index]:
                    continue
                adj_list[row_index].add(graph[row_index][col_index])
                adj_list[graph[row_index][col_index]].add(row_index)
        queue = deque([])
        def bfs():
            #{0 : {1, 2, 3}}            
             #  can be 0 or 1
            while queue:
                node = queue.pop()
                existing_group = visited[node]
                neighbors = adj_list[node]
                for neighbor in neighbors:
                    if visited[neighbor] == existing_group:
                        return False
                    if visited[neighbor] == -1:
                        visited[neighbor] = (existing_group+1) % 2
                        queue.append(neighbor)
            return True
        for node in adj_list:
            if visited[node] == -1:
                visited[node] = 0
                queue.appendleft(node)
                if not bfs():
                    return False
        return True