"""
Problem: Painting the Walls
Number: 2742
Difficulty: Hard
Link: https://leetcode.com/problems/painting-the-walls/
Date: 2025-11-16
"""

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def paint_walls(cost, time):
    """
    Calculates the minimum cost to paint all walls using paid and free painters.

    Args:
        cost (list[int]): The cost to hire the paid painter for each wall.
        time (list[int]): The time the free painter takes to paint each wall.

    Returns:
        int: The minimum cost to paint all walls.
    """

    n = len(cost)

    # dp[i][j] represents the minimum cost to paint the first i walls such that at least j walls are painted by paid painters.
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    # Base case: If no walls are considered, and 0 walls are painted by paid painters, the cost is 0.
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(n + 1):
            # Option 1: Don't hire the paid painter for the i-th wall.
            # If we don't hire the paid painter, we still need to paint at least j walls using the paid painters from the previous i-1 walls.
            dp[i][j] = dp[i - 1][j]

            # Option 2: Hire the paid painter for the i-th wall.
            # If we hire the paid painter, we need to account for the walls the free painter can paint while the paid painter works on the i-th wall.
            if j > 0:
                # Calculate the number of walls that need to be painted by paid painters from the previous i-1 walls.
                # We subtract (time[i-1] + 1) because while the paid painter paints wall i, the free painter can paint time[i-1] walls. We add 1 since we hire the paid painter
                # for wall i.  We take max(0, ...) in case the paid painter paints enough walls so free painter covers the rest
                walls_to_paint_before = max(0, j - (time[i - 1] + 1))
                dp[i][j] = min(dp[i][j], cost[i - 1] + dp[i - 1][walls_to_paint_before])

    # The minimum cost to paint all n walls is the minimum cost to paint the first n walls such that at least n walls are painted by paid painters.
    return dp[n][n]