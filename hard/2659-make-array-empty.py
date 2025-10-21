"""
Problem: Make Array Empty
Number: 2659
Difficulty: Hard
Link: https://leetcode.com/
Date: 2025-10-21
"""

# Time Complexity: O(n log n) - due to sorting and heap operations
# Space Complexity: O(n) - for storing indices and the heap
import heapq

def make_array_empty(nums):
    """
    Calculates the number of operations to empty the array according to the given rules.

    Args:
        nums: A list of distinct integers.

    Returns:
        The number of operations required to empty the array.
    """

    n = len(nums)
    indices = {num: i for i, num in enumerate(nums)}  # Store the index of each number
    heap = [(num, i) for i, num in enumerate(nums)]   # Create a min-heap of (number, index)
    heapq.heapify(heap)

    operations = 0
    removed = [False] * n  # Keep track of removed indices

    for _ in range(n):
        operations += 1  # Increment for removing the smallest number

        smallest_num, smallest_index = heapq.heappop(heap)
        while removed[smallest_index]: # If the number is already removed, find the next smallest
            smallest_num, smallest_index = heapq.heappop(heap)

        removed[smallest_index] = True  # Mark the index as removed

        # Check neighbors and remove the larger one if their absolute difference is 1
        left_index = smallest_index - 1
        right_index = smallest_index + 1

        left_valid = left_index >= 0 and not removed[left_index]
        right_valid = right_index < n and not removed[right_index]

        operations += 1 # Increment operations for each comparison step

        if left_valid and right_valid:
            if abs(nums[left_index] - nums[right_index]) == 1:
                if nums[left_index] > nums[right_index]:
                    removed[left_index] = True
                elif nums[right_index] > nums[left_index]:
                    removed[right_index] = True
                else:  # If equal, remove the smaller index
                    if left_index < right_index:
                        removed[left_index] = True
                    else:
                        removed[right_index] = True
        elif left_valid and not right_valid:
           pass
        elif not left_valid and right_valid:
            pass


    return operations


# Example usage:
if __name__ == '__main__':
    nums1 = [3, 4, -1]
    print(f"Input: {nums1}, Output: {make_array_empty(nums1)}")  # Expected Output: 5

    nums2 = [1, 2, 4, 3]
    print(f"Input: {nums2}, Output: {make_array_empty(nums2)}")  # Expected Output: 8

    nums3 = [1, 3, 2, 5, 4]
    print(f"Input: {nums3}, Output: {make_array_empty(nums3)}") # Expected Output: 11

    nums4 = [5,4,3,2,1]
    print(f"Input: {nums4}, Output: {make_array_empty(nums4)}") # Expected Output: 9

    nums5 = [1]
    print(f"Input: {nums5}, Output: {make_array_empty(nums5)}") # Expected Output: 1

    nums6 = [2,1]
    print(f"Input: {nums6}, Output: {make_array_empty(nums6)}") # Expected Output: 3