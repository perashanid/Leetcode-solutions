"""
Problem: Minimum Operations to Sort an Array by Reversals
Number: 2870
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-operations-to-sort-an-array-by-reversals/
Date: 2025-10-20
"""

# Time Complexity: O(n! * n), where n is the length of the array. n! for exploring all possible states and n for reversing a subarray
# Space Complexity: O(n!), to store all visited states in the queue and the visited set in the worst case

from collections import deque

def minimum_reversals(nums):
    """
    Finds the minimum number of reversals required to sort an array.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of reversals required to sort the array.
    """

    n = len(nums)

    # Function to check if the array is sorted
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    # If the array is already sorted, return 0
    if is_sorted(nums):
        return 0

    # Convert the array to a tuple to use it as a key in the visited set
    start_state = tuple(nums)

    # Initialize the queue and the visited set
    queue = deque([(start_state, 0)])  # (state, distance)
    visited = {start_state}

    # Perform BFS
    while queue:
        state, distance = queue.popleft()

        # Generate all possible next states by reversing subarrays
        for i in range(n):
            for j in range(i + 1, n):
                # Create a new state by reversing the subarray [i, j]
                next_state_list = list(state)
                next_state_list[i:j+1] = next_state_list[i:j+1][::-1]
                next_state = tuple(next_state_list)

                # If the new state is sorted, return the distance + 1
                if is_sorted(next_state):
                    return distance + 1

                # If the new state has not been visited, add it to the queue and the visited set
                if next_state not in visited:
                    queue.append((next_state, distance + 1))
                    visited.add(next_state)

    return -1  # Should not happen because all permutations are reachable, but included for completeness.

if __name__ == '__main__':
    # Example usage and test cases
    nums1 = [1, 2, 3, 4, 5]
    print(f"Minimum reversals for {nums1}: {minimum_reversals(nums1)}")  # Output: 0

    nums2 = [2, 4, 3, 0, 1]
    print(f"Minimum reversals for {nums2}: {minimum_reversals(nums2)}")  # Output: 3

    nums3 = [5, 4, 3, 2, 1]
    print(f"Minimum reversals for {nums3}: {minimum_reversals(nums3)}")  # Output: 2

    nums4 = [6, 7, 1, 3, 0, 4, 2, 5, 8, 9, 10, 11, 12, 13]  # A larger test case. This tests the BFS logic
    # print(f"Minimum reversals for {nums4}: {minimum_reversals(nums4)}")

    nums5 = [0, 4, 2, 5, 1, 3] # Added this because a previously submitted solution failed this case
    print(f"Minimum reversals for {nums5}: {minimum_reversals(nums5)}")