"""
Problem: Best Time to Buy and Sell Stock IV
Number: 188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Date: 2025-11-01
"""

# Time Complexity: O(k*n) where n is the length of prices
# Space Complexity: O(k*n)
def maxProfit(k: int, prices: list[int]) -> int:
    """
    Calculates the maximum profit achievable with at most k transactions.

    Args:
        k: The maximum number of transactions allowed.
        prices: A list of stock prices for each day.

    Returns:
        The maximum profit.
    """

    n = len(prices)

    # Edge case: If no prices or no transactions allowed, return 0
    if not prices or k == 0:
        return 0

    # If k is large enough, we can perform unlimited transactions
    if k >= n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    # dp[i][j] represents the maximum profit with at most i transactions up to day j
    dp = [[0] * n for _ in range(k + 1)]

    # Iterate through the number of transactions
    for i in range(1, k + 1):
        # Initialize the maximum profit after buying
        max_profit_after_buy = -prices[0]

        # Iterate through the days
        for j in range(1, n):
            # Case 1: No transaction on day j (inherit from previous day)
            dp[i][j] = dp[i][j - 1]

            # Case 2: Sell on day j (buy on a previous day)
            # We have to find the maximum profit of (buying on day t and selling on day j)
            # In this case we use a variable to store max_profit_after_buy
            # max_profit_after_buy = max(max_profit_after_buy, dp[i - 1][j - 1] - prices[j])
            # dp[i][j] = max(dp[i][j], prices[j] + max_profit_after_buy)
            max_profit_after_buy = max(max_profit_after_buy, dp[i - 1][j - 1] - prices[j])
            dp[i][j] = max(dp[i][j], prices[j] + max_profit_after_buy)
            
            # Update max_profit_after_buy for the next iteration
            max_profit_after_buy = max(max_profit_after_buy, dp[i-1][j] - prices[j])

    return dp[k][n - 1]


# Example usage:
if __name__ == "__main__":
    k = 2
    prices = [2, 4, 1]
    print(f"Maximum profit for k={k} and prices={prices}: {maxProfit(k, prices)}")  # Output: 2

    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(f"Maximum profit for k={k} and prices={prices}: {maxProfit(k, prices)}")  # Output: 7

    k = 2
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(f"Maximum profit for k={k} and prices={prices}: {maxProfit(k, prices)}")  # Output: 11

    k = 0
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(f"Maximum profit for k={k} and prices={prices}: {maxProfit(k, prices)}")  # Output: 0

    k = 100
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(f"Maximum profit for k={k} and prices={prices}: {maxProfit(k, prices)}")  # Output: 11