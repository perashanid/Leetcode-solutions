"""
Problem: Maximum Running Time of N Computers
Number: 2141
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-running-time-of-n-computers/
Date: 2025-10-21
"""

# Time Complexity: O(Nlog(Sum of Batteries)), where N is the number of batteries. Binary search dominates the time complexity.
# Space Complexity: O(1), excluding the input array.

def maxRunTime(n: int, batteries: list[int]) -> int:
    """
    Calculates the maximum number of minutes you can run all n computers simultaneously.

    Args:
        n (int): The number of computers.
        batteries (list[int]): A list of integers representing the battery power of each battery.

    Returns:
        int: The maximum number of minutes you can run all n computers simultaneously.
    """

    # Define a function to check if it's possible to run all computers for a given time 't'
    def is_possible(t: int) -> bool:
        total_power = 0
        for battery in batteries:
            total_power += min(battery, t)  # Use battery power up to 't' or the battery's capacity, whichever is smaller

        return total_power >= n * t  # Check if the total power is enough to run all n computers for time 't'

    # Use binary search to find the maximum possible time
    left, right = 1, sum(batteries) // n  # The lower bound is 1, and the upper bound is the average battery power
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = mid
            left = mid + 1  # Try to increase the time
        else:
            right = mid - 1  # Reduce the time

    return ans

# Example Usage:
# n = 2, batteries = [3,3,3]
# result = maxRunTime(n, batteries)
# print(f"Maximum running time: {result}")  # Output: 4

# n = 2, batteries = [1,1,1]
# result = maxRunTime(n, batteries)
# print(f"Maximum running time: {result}")  # Output: 1

# n = 3, batteries = [10,10,3,5]
# result = maxRunTime(n, batteries)
# print(f"Maximum running time: {result}")  # Output: 8

# n = 3, batteries = [5,6,7,8,9]
# result = maxRunTime(n, batteries)
# print(f"Maximum running time: {result}")  # Output: 8