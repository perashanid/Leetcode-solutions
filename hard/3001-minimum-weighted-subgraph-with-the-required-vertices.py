"""
Problem: Minimum Weighted Subgraph With the Required Vertices
Number: 3001
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-vertices/
Date: 2025-10-21
"""

import heapq

def minimum_weighted_subgraph(n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
    """
    Finds the minimum weight of a subgraph of the given graph such that it is possible to reach dest from both src1 and src2.

    Time Complexity: O(E log V), where E is the number of edges and V is the number of vertices (n).
    Space Complexity: O(V + E), where V is the number of vertices (n) and E is the number of edges.
    """

    def dijkstra(graph: list[list[tuple[int, int]]], start: int) -> list[int]:
        """
        Performs Dijkstra's algorithm to find the shortest distances from a start node to all other nodes.
        """
        distances = [float('inf')] * n
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)

        while pq:
            dist, u = heapq.heappop(pq)

            if dist > distances[u]:
                continue

            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))

        return distances

    # Build the adjacency list for the original graph
    graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        graph[u].append((v, weight))

    # Build the reversed adjacency list for the reversed graph
    reversed_graph = [[] for _ in range(n)]
    for u, v, weight in edges:
        reversed_graph[v].append((u, weight))

    # Calculate shortest distances from src1, src2, and dest to all other nodes
    dist_src1 = dijkstra(graph, src1)
    dist_src2 = dijkstra(graph, src2)
    dist_dest = dijkstra(reversed_graph, dest)  # Use reversed graph for shortest paths to dest

    # Find the minimum weight by iterating through all nodes and summing the distances
    min_weight = float('inf')
    for i in range(n):
        if dist_src1[i] != float('inf') and dist_src2[i] != float('inf') and dist_dest[i] != float('inf'):
            min_weight = min(min_weight, dist_src1[i] + dist_src2[i] + dist_dest[i])

    # If no such subgraph exists, return -1
    return min_weight if min_weight != float('inf') else -1

# Example Usage
if __name__ == '__main__':
    n = 6
    edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1 = 0
    src2 = 1
    dest = 5
    print(minimum_weighted_subgraph(n, edges, src1, src2, dest))  # Output: 16

    n = 3
    edges = [[0, 1, 1], [1, 2, 1]]
    src1 = 0
    src2 = 1
    dest = 2
    print(minimum_weighted_subgraph(n, edges, src1, src2, dest))  # Output: -1