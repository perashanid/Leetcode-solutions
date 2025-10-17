"""
Problem: Best Time to Buy and Sell Stock IV
Number: 188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Date: 2025-10-17
"""

# Time Complexity: O(k*n), where n is the length of the prices array
# Space Complexity: O(k*n)
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """
        Calculates the maximum profit achievable with at most k transactions.

        Args:
            k: The maximum number of transactions allowed.
            prices: A list of stock prices for each day.

        Returns:
            The maximum profit achievable.
        """

        n = len(prices)

        # If the number of transactions allowed is greater than n/2, we can buy and sell on every rising day
        # This is equivalent to solving the problem with unlimited transactions
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[i][j] represents the maximum profit achievable with at most i transactions up to day j
        dp = [[0] * n for _ in range(k + 1)]

        # Iterate through each possible number of transactions
        for i in range(1, k + 1):
            # Initialize the maximum profit after buying
            max_profit_after_buy = -prices[0]

            # Iterate through each day
            for j in range(1, n):
                # Case 1: Don't do anything on day j, inherit the profit from the previous day
                dp[i][j] = dp[i][j - 1]

                # Case 2: Sell on day j, buy on a previous day (or not at all)
                # dp[i][j] = max(dp[i][j], prices[j] + dp[i-1][l] - prices[l]) for l in range(j)
                # dp[i][j] = max(dp[i][j], prices[j] + max(dp[i-1][l] - prices[l]) for l in range(j)
                # Keep track of max(dp[i-1][l] - prices[l]) as max_profit_after_buy to avoid recalculating it
                dp[i][j] = max(dp[i][j], prices[j] + max_profit_after_buy)

                # Update the maximum profit after buying up to the current day
                max_profit_after_buy = max(max_profit_after_buy, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]