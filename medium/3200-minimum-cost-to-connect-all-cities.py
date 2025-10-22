"""
Problem: Minimum Cost to Connect All Cities
Number: 3200
Difficulty: Medium
Link: https://example.com/minimum-cost-to-connect-cities
Date: 2025-10-22
"""

# Time Complexity: O(E log V), where E is the number of edges (roads + existingRoads) and V is the number of vertices (n)
# Space Complexity: O(V), where V is the number of vertices (n)

def minimum_cost_to_connect_all_cities(n: int, roads: list[list[int]], existingRoads: list[list[int]]) -> int:
    """
    Calculates the minimum cost to connect all cities.

    Args:
        n: The number of cities.
        roads: A list of roads where roads[i] = [city1, city2, cost].
        existingRoads: A list of existing roads where existingRoads[i] = [city1, city2].

    Returns:
        The minimum cost to connect all the cities.
        If it is not possible to connect all cities, return -1.
    """

    # 1. Union-Find data structure for detecting cycles and connecting components.
    parent = list(range(n + 1))  # Initialize parent of each city to itself.
    rank = [0] * (n + 1)  # Initialize rank of each city to 0.

    def find(i: int) -> int:
        """Finds the root of the set that the element i belongs to."""
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])  # Path compression.
        return parent[i]

    def union(i: int, j: int) -> bool:
        """Unions the sets containing elements i and j. Returns True if a union occurred, False otherwise."""
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True
        return False

    # 2. Add existing roads to the Union-Find data structure with cost 0.
    for city1, city2 in existingRoads:
        union(city1, city2)

    # 3. Kruskal's algorithm to find the minimum spanning tree.
    edges = []
    for city1, city2, cost in roads:
        edges.append((cost, city1, city2))
    edges.sort()  # Sort edges by cost.

    total_cost = 0
    num_edges = 0
    for cost, city1, city2 in edges:
        if union(city1, city2):
            total_cost += cost
            num_edges += 1

    # 4. Check if all cities are connected.
    num_components = 0
    for i in range(1, n + 1):
        if parent[i] == i:
            num_components += 1

    root_of_one = find(1)
    for i in range(2, n+1):
        if find(i) != root_of_one:
            return -1

    #5. Return the total cost.
    return total_cost

# Example Usage
if __name__ == '__main__':
    n = 3
    roads = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    existingRoads = [[1, 2]]
    print(minimum_cost_to_connect_all_cities(n, roads, existingRoads))  # Output: 1

    n = 4
    roads = [[1, 2, 3], [3, 4, 4]]
    existingRoads = []
    print(minimum_cost_to_connect_all_cities(n, roads, existingRoads))  # Output: -1

    n = 4
    roads = [[1, 2, 3], [1, 3, 5], [1, 4, 7], [2, 3, 8]]
    existingRoads = [[2, 4]]
    print(minimum_cost_to_connect_all_cities(n, roads, existingRoads)) # Output 8