"""
Problem: Best Time to Buy and Sell Stock IV
Number: 188
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Date: 2025-10-12
"""

# Time Complexity: O(k*n) where n is the length of the prices array
# Space Complexity: O(k*n)

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        """
        Calculates the maximum profit that can be made by buying and selling a stock at most k times.

        Args:
            k (int): The maximum number of transactions allowed.
            prices (list[int]): An array of prices where prices[i] is the price of the stock on the ith day.

        Returns:
            int: The maximum profit that can be achieved.
        """
        n = len(prices)

        # Edge case: If the number of transactions allowed is greater than n/2, we can simply sum the positive differences.
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        # dp[i][j] represents the maximum profit achieved after j transactions up to day i.
        dp = [[0] * n for _ in range(k + 1)]

        # Iterate over the number of transactions.
        for i in range(1, k + 1):
            # Initialize the maximum profit with the profit achieved with previous transactions.
            max_profit = -prices[0]

            # Iterate over the days.
            for j in range(1, n):
                # Either we don't do anything on this day (inherit the previous day's profit)
                # or we sell on this day.
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_profit)

                # Update max_profit, which represents the maximum profit achievable if we buy on day j.
                # max_profit means the max profit we can achieve if we buy at prices[j] *after* making i-1 transactions before.
                # max_profit = dp[i-1][j-1] - prices[j-1], which represents the best profit after i-1 transaction until j-1 day, and buying the stock at prices[j-1] day.
                # We use prices[j-1] instead of prices[j] because we need to "buy" on a previous day to make the transaction valid at day j.

                max_profit = max(max_profit, dp[i - 1][j - 1] - prices[j]) # critical optimization, no TLE here

        # The maximum profit after k transactions on the last day is the result.
        return dp[k][n - 1]