"""
Problem: Minimum Cost to Reach Destination in Time
Number: 3907
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
Date: 2025-10-25
"""

import heapq

def minCost(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
    """
    Finds the minimum cost to reach city n - 1 from city 0 within maxTime.

    Args:
        maxTime: The maximum time allowed for the journey.
        edges: A list of edges, where each edge is a list [u, v, time].
        passingFees: A list of passing fees for each city.

    Returns:
        The minimum cost to reach city n - 1, or -1 if it's impossible.

    Time Complexity: O(E * log(N)) where E is the number of edges and N is the number of nodes. The heap operations are O(log(N)) and we may iterate over all edges during Dijkstra
    Space Complexity: O(N + E) where N is the number of nodes and E is the number of edges to store the graph adjacency list and the cost/time arrays.
    """
    n = len(passingFees)

    # Create an adjacency list to represent the graph.
    graph = {i: [] for i in range(n)}
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))

    # Initialize cost and time arrays. cost[i][t] stores the minimum cost to reach city i in time t or less.
    # time[i][c] stores the minimum time to reach city i with a total cost of c or less.
    # Initially fill with infinity since we haven't explored any paths yet.
    
    min_cost = [[float('inf')] * (maxTime + 1) for _ in range(n)]
    min_cost[0][0] = passingFees[0]  # Initial cost to reach city 0 in 0 time is the passing fee of city 0

    # Use a priority queue to explore the graph. The priority queue stores tuples of (cost, city, time).
    pq = [(passingFees[0], 0, 0)]  # (cost, city, time)

    while pq:
        cost, city, time = heapq.heappop(pq)

        # If the current cost is greater than the minimum cost we already have for this city and time, skip it.
        if cost > min_cost[city][time]:
            continue
        
        # If the target city is reached within the time limit return the cost.
        if city == n - 1:
            return cost

        # Explore neighbors of the current city.
        for neighbor, travel_time in graph[city]:
            new_time = time + travel_time
            if new_time <= maxTime:
                new_cost = cost + passingFees[neighbor]

                # If the new cost is lower than the current minimum cost to reach the neighbor in the new time,
                # update the minimum cost and add the neighbor to the priority queue.
                if new_cost < min_cost[neighbor][new_time]:
                    min_cost[neighbor][new_time] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, new_time))

    # If it's impossible to reach city n - 1 within maxTime, return -1.
    return -1


# Example Usage
if __name__ == '__main__':
    maxTime1 = 30
    edges1 = [[0, 1, 10], [1, 2, 10], [0, 2, 10]]
    passingFees1 = [5, 1, 2]
    print(f"Example 1: {minCost(maxTime1, edges1, passingFees1)}")  # Output: 7

    maxTime2 = 29
    edges2 = [[0, 1, 10], [1, 2, 10], [0, 2, 10]]
    passingFees2 = [5, 1, 2]
    print(f"Example 2: {minCost(maxTime2, edges2, passingFees2)}")  # Output: -1

    maxTime3 = 5
    edges3 = [[0, 3, 8], [0, 1, 2], [0, 2, 5], [3, 4, 2], [1, 5, 1], [2, 6, 6], [4, 7, 3], [5, 8, 2], [6, 9, 4],
              [7, 9, 1], [8, 9, 3]]
    passingFees3 = [3, 3, 4, 0, 4, 5, 3, 7, 2, 7]
    print(f"Example 3: {minCost(maxTime3, edges3, passingFees3)}") #Output: -1

    maxTime4 = 6
    edges4 = [[0, 1, 2], [0, 2, 5], [1, 2, 1], [2, 3, 4]]
    passingFees4 = [1, 2, 3, 4]
    print(f"Example 4: {minCost(maxTime4, edges4, passingFees4)}") #Output: 10