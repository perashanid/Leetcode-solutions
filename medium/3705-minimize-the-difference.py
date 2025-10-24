"""
Problem: Minimize the Difference
Number: 3705
Difficulty: Medium
Link: https://leetcode.com/
Date: 2025-10-24
"""

def minimize_the_difference(nums1, nums2):
    """
    Minimize the absolute difference between the sums of two arrays after performing some number of swaps.

    Time Complexity: O(n * sum_diff) where n is the length of the arrays and sum_diff is the possible range
                     of the difference between the sums of nums1 and nums2.  In the worst case, sum_diff can be
                     n * 100. Thus, it can be approximated to O(n^2).
    Space Complexity: O(n * sum_diff). Similar to time complexity, it can be approximated to O(n^2).
    """
    n = len(nums1)
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    diff = abs(sum1 - sum2)

    # dp[i][j] represents whether it is possible to achieve a difference of 'j' by considering the first 'i' elements
    max_sum_diff = n * 100
    dp = [[False] * (2 * max_sum_diff + 1) for _ in range(n + 1)]

    # Base case: when no element is considered, the difference is 0.
    dp[0][max_sum_diff] = True

    for i in range(1, n + 1):
        for j in range(-max_sum_diff, max_sum_diff + 1):
            # If the current state is achievable
            if dp[i - 1][j + max_sum_diff]:
                # Option 1: Don't swap nums1[i-1] and nums2[i-1].  The difference is maintained.
                dp[i][j + max_sum_diff] = True

                # Option 2: Swap nums1[i-1] and nums2[i-1].
                diff_update = nums2[i - 1] - nums1[i - 1]
                if -max_sum_diff <= j + diff_update <= max_sum_diff:
                    dp[i][j + diff_update + max_sum_diff] = True

    # Find the minimum absolute difference that is achievable.
    min_diff = float('inf')
    for j in range(-max_sum_diff, max_sum_diff + 1):
        if dp[n][j + max_sum_diff]:
            min_diff = min(min_diff, abs(j))

    return min_diff

# Example Usage and Test Cases:
if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    print(f"Minimum difference for nums1={nums1}, nums2={nums2}: {minimize_the_difference(nums1, nums2)}")  # Output: 0

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(f"Minimum difference for nums1={nums1}, nums2={nums2}: {minimize_the_difference(nums1, nums2)}")  # Output: 0

    nums1 = [10, 7, 3, 1]
    nums2 = [2, 4, 8, 9]
    print(f"Minimum difference for nums1={nums1}, nums2={nums2}: {minimize_the_difference(nums1, nums2)}") # Output: 2