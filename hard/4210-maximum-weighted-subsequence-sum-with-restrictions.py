"""
Problem: Maximum Weighted Subsequence Sum with Restrictions
Number: 4210
Difficulty: Hard
Link: https://leetcode.com/
Date: 2025-10-25
"""

# Time Complexity: O(n log n), where n is the length of the input arrays. This is due to the binary search.
# Space Complexity: O(n), for the dp array.

def max_weighted_subsequence_sum(values, indices, k):
    """
    Calculates the maximum sum of a subsequence of 'values' such that the absolute difference
    between the indices of any two elements in the subsequence is greater than or equal to 'k'.

    Args:
        values (list[int]): A list of integers representing the values of the elements.
        indices (list[int]): A list of integers representing the indices of the elements.
        k (int): An integer representing the minimum allowed difference between the indices of any two elements in the subsequence.

    Returns:
        int: The maximum possible sum of a valid subsequence.
    """

    n = len(values)
    if n == 0:
        return 0

    # dp[i] stores the maximum sum of a valid subsequence ending at index i.
    dp = [0] * n
    dp[0] = values[0]

    for i in range(1, n):
        # Option 1: Don't include values[i] in the subsequence.
        dp[i] = dp[i - 1]

        # Option 2: Include values[i] in the subsequence.
        # Find the largest j < i such that abs(indices[i] - indices[j]) >= k.
        # Since indices is strictly increasing, abs(indices[i] - indices[j]) = indices[i] - indices[j].

        # Use binary search to find the largest j < i such that indices[i] - indices[j] >= k
        left, right = 0, i - 1
        j = -1  # Initialize j to -1, meaning no such j is found
        while left <= right:
            mid = (left + right) // 2
            if indices[i] - indices[mid] >= k:
                j = mid
                left = mid + 1  # Try to find a larger j
            else:
                right = mid - 1

        # If a valid j is found, add values[i] to the maximum sum ending at j.
        if j != -1:
            dp[i] = max(dp[i], dp[j] + values[i])
        else:  # If no valid j is found, the subsequence only contains values[i]
            dp[i] = max(dp[i], values[i])
            
    return dp[n - 1]


# Example Usage
if __name__ == "__main__":
    values1 = [4, -2, 1, 5, -3]
    indices1 = [0, 2, 3, 6, 8]
    k1 = 3
    print(f"Example 1: {max_weighted_subsequence_sum(values1, indices1, k1)}")  # Output: 9

    values2 = [1, 2, 3, 4, 5]
    indices2 = [0, 1, 2, 3, 4]
    k2 = 2
    print(f"Example 2: {max_weighted_subsequence_sum(values2, indices2, k2)}")  # Output: 9

    values3 = [-1, -2, -3]
    indices3 = [0, 1, 2]
    k3 = 1
    print(f"Example 3: {max_weighted_subsequence_sum(values3, indices3, k3)}")  # Output: -1

    values4 = [1,2,3]
    indices4 = [0,5,10]
    k4 = 6
    print(f"Example 4: {max_weighted_subsequence_sum(values4, indices4, k4)}")  # Output: 4

    values5 = [5, 1, 6, 2, 7]
    indices5 = [0, 1, 2, 3, 4]
    k5 = 1
    print(f"Example 5: {max_weighted_subsequence_sum(values5, indices5, k5)}") # Output: 18