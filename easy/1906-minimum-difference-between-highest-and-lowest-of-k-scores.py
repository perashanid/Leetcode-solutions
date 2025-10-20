"""
Problem: Minimum Difference Between Highest and Lowest of K Scores
Number: 1906
Difficulty: Easy
Link: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
Date: 2025-10-20
"""

def minimum_difference(nums, k):
    """
    Finds the minimum difference between the highest and lowest of k scores.

    Args:
        nums (List[int]): A list of integers representing the scores of students.
        k (int): The number of students to pick.

    Returns:
        int: The minimum disparity among all possible sets of k students.
    """

    # Time Complexity: O(n log n) due to sorting. The loop takes O(n) time.
    # Space Complexity: O(1) if sorting is done in-place. O(n) otherwise, depending on the sorting algorithm.

    n = len(nums)

    # If k is greater than the number of students, return -1 (invalid input)
    if k > n or k <= 0:
        return -1  # Or raise an exception, depending on requirements

    # Sort the scores in ascending order
    nums.sort()

    # Initialize the minimum disparity to infinity
    min_disparity = float('inf')

    # Iterate through the sorted scores, calculating the disparity for each possible set of k students
    for i in range(n - k + 1):
        # The disparity is the difference between the highest and lowest scores in the set
        disparity = nums[i + k - 1] - nums[i]

        # Update the minimum disparity if the current disparity is smaller
        min_disparity = min(min_disparity, disparity)

    return min_disparity

# Example Usage:
# nums = [1, 3, 6, 2, 7, 8]
# k = 3
# print(minimum_difference(nums, k))  # Output: 4

# nums = [1, 2, 3, 4, 5]
# k = 5
# print(minimum_difference(nums, k))  # Output: 4

# nums = [9,4,1,7]
# k = 2
# print(minimum_difference(nums, k)) # Output: 2

# nums = [87063,61094,44530,21290,57155,95055,78481,27249,45490,42307,62425,21069,43637,65932,85197,43275,61037,52301,96674,59056,38698]
# k = 11
# print(minimum_difference(nums, k)) # Output: 23057