"""
Problem: Minimum Weighted Subgraph With Required Vertices
Number: 3806
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-vertices/
Date: 2025-10-24
"""

import heapq

def minimum_weighted_subgraph(n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
    """
    Finds the minimum weight of a subgraph of the given graph that contains all three required vertices.

    Time Complexity: O(E log V), where E is the number of edges and V is the number of vertices.
    Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
    """

    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]  # reversed adjacency list

    for u, v, w in edges:
        adj[u].append((v, w))
        radj[v].append((u, w))

    def dijkstra(start_node: int, graph: list[list[tuple[int, int]]]) -> list[int]:
        """
        Performs Dijkstra's algorithm to find the shortest distances from a start node to all other nodes.
        """
        dist = [float('inf')] * n
        dist[start_node] = 0
        pq = [(0, start_node)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist

    dist_src1 = dijkstra(src1, adj)
    dist_src2 = dijkstra(src2, adj)
    dist_dest = dijkstra(dest, adj)
    dist_rev_dest = dijkstra(dest, radj)

    min_weight = float('inf')

    for i in range(n):
        if dist_src1[i] == float('inf') or dist_src2[i] == float('inf') or dist_dest[i] == float('inf'):
            continue
        min_weight = min(min_weight, dist_src1[i] + dist_src2[i] + dist_dest[i])

    if min_weight == float('inf'):
        return -1
    else:
        return min_weight


if __name__ == '__main__':
    # Example 1
    n1 = 6
    edges1 = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1_1 = 0
    src2_1 = 1
    dest1 = 5
    print(f"Example 1: {minimum_weighted_subgraph(n1, edges1, src1_1, src2_1, dest1)}")  # Output: 9

    # Example 2
    n2 = 6
    edges2 = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
    src1_2 = 0
    src2_2 = 1
    dest2 = 2
    print(f"Example 2: {minimum_weighted_subgraph(n2, edges2, src1_2, src2_2, dest2)}")  # Output: -1

    # Example 3
    n3 = 4
    edges3 = [[0,1,1], [0,2,5], [2,3,2], [1,3,3]]
    src1_3 = 0
    src2_3 = 1
    dest3 = 3
    print(f"Example 3: {minimum_weighted_subgraph(n3, edges3, src1_3, src2_3, dest3)}") # Output: 4