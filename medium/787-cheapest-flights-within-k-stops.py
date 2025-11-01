"""
Problem: Cheapest Flights Within K Stops
Number: 787
Difficulty: Medium
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Date: 2025-11-01
"""

# Time Complexity: O(K * |E|), where K is the maximum number of stops and |E| is the number of flights.
# Space Complexity: O(N), where N is the number of cities.

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """
    Finds the cheapest price from src to dst with at most k stops.

    Args:
        n: The number of cities.
        flights: A list of flights, where flights[i] = [fromi, toi, pricei].
        src: The source city.
        dst: The destination city.
        k: The maximum number of stops.

    Returns:
        The cheapest price from src to dst with at most k stops. If there is no such route, return -1.
    """

    # Initialize a dictionary to store the graph as an adjacency list.
    graph = {}
    for u, v, w in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    # Initialize a distance array to store the minimum distance from src to each city.
    dist = [float('inf')] * n
    dist[src] = 0

    # Use a queue for BFS traversal. Each element in the queue is a tuple (city, distance, stops).
    queue = [(src, 0, -1)]  # Start with the source city, distance 0, and -1 stops (as we haven't started yet).

    # BFS traversal with at most k stops.
    while queue:
        city, distance, stops = queue.pop(0)

        # If we have reached the maximum number of stops, continue to the next element.
        if stops > k:
            continue

        # If the current city has outgoing edges, iterate over its neighbors.
        if city in graph:
            for neighbor, weight in graph[city]:
                # If the new distance to the neighbor is cheaper than the current distance, update the distance.
                if distance + weight < dist[neighbor]:
                    dist[neighbor] = distance + weight
                    queue.append((neighbor, distance + weight, stops + 1))  # Add the neighbor to the queue with the updated distance and stops.
                # If the number of stops is less than or equal to k but we still found a cheaper cost, keep processing the queue.
                elif stops < k:
                    queue.append((neighbor, distance + weight, stops + 1))


    # If the distance to the destination is still infinity, there is no such route.
    if dist[dst] == float('inf'):
        return -1

    # Otherwise, return the cheapest price from src to dst.
    return dist[dst]


# Example Usage
if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: 700

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 0
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: 500

    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    print(findCheapestPrice(n, flights, src, dst, k))  # Output: 200