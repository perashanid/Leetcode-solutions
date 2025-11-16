"""
Problem: Minimum Cost to Connect All Points
Number: 9
Difficulty: Medium
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
Date: 2025-11-16
"""

# Time Complexity: O(n^2 log n), where n is the number of points. This is dominated by the sorting of edges.
# Space Complexity: O(n^2), where n is the number of points, due to storing all possible edges.

def minCostConnectPoints(points):
    """
    Calculates the minimum cost to connect all points using Prim's algorithm.

    Args:
        points: A list of lists, where each inner list represents a point [x, y].

    Returns:
        The minimum cost to connect all points.
    """

    n = len(points)

    # Calculate all possible edges and their costs (Manhattan distances)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edges.append((cost, i, j))

    # Sort edges by cost in ascending order
    edges.sort()

    # Prim's algorithm
    mst_cost = 0
    num_edges = 0
    parent = list(range(n))  # Initialize parent array for DSU

    def find(i):
        """Find the root of the set i belongs to (path compression)."""
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        """Union the sets containing i and j."""
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True  # Return True if a union occurred
        return False  # Return False if no union occurred (already in the same set)

    for cost, u, v in edges:
        if union(u, v):
            mst_cost += cost
            num_edges += 1
            if num_edges == n - 1:
                break  # MST is complete

    return mst_cost


if __name__ == '__main__':
    # Example Usage
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(f"Minimum cost for points {points1}: {minCostConnectPoints(points1)}")  # Output: 20

    points2 = [[3, 12], [-2, 5], [-4, 1]]
    print(f"Minimum cost for points {points2}: {minCostConnectPoints(points2)}")  # Output: 18

    points3 = [[0, 0], [1, 1], [1, 0], [0, 1]]
    print(f"Minimum cost for points {points3}: {minCostConnectPoints(points3)}") # Output: 4