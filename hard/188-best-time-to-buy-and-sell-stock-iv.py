"""
Problem: Best Time to Buy and Sell Stock IV
Number: 188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Date: 2025-11-16
"""

# Time Complexity: O(k*n) where n is the length of the prices array.
# Space Complexity: O(k*n)

def maxProfit(k: int, prices: list[int]) -> int:
    """
    Finds the maximum profit that can be achieved with at most k transactions.

    Args:
        k (int): The maximum number of transactions allowed.
        prices (list[int]): A list of stock prices for each day.

    Returns:
        int: The maximum profit that can be achieved.
    """
    n = len(prices)

    # If the length of prices is 0, return 0
    if n == 0:
        return 0

    # If k is large enough, we can simply perform as many transactions as possible
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # dp[i][j] represents the maximum profit with at most i transactions up to day j.
    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0] # Initialize the maximum difference
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff) # Check if we can get more profit by doing transaction i on day j or take the previous best
            max_diff = max(max_diff, dp[i - 1][j - 1] - prices[j]) # Update the maximum difference

    return dp[k][n - 1]

# Example Usage
if __name__ == '__main__':
    # Example 1
    k1 = 2
    prices1 = [2, 4, 1]
    print(f"Example 1: k = {k1}, prices = {prices1}, max profit = {maxProfit(k1, prices1)}")  # Output: 2

    # Example 2
    k2 = 2
    prices2 = [3, 2, 6, 5, 0, 3]
    print(f"Example 2: k = {k2}, prices = {prices2}, max profit = {maxProfit(k2, prices2)}")  # Output: 7

    # Example 3
    k3 = 2
    prices3 = [3,3,5,0,0,3,1,4]
    print(f"Example 3: k = {k3}, prices = {prices3}, max profit = {maxProfit(k3, prices3)}")  # Output: 6

    # Example 4
    k4 = 1
    prices4 = [1,2]
    print(f"Example 4: k = {k4}, prices = {prices4}, max profit = {maxProfit(k4, prices4)}")  # Output: 1