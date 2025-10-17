"""
Problem: Sliding Window Maximum
Number: 239
Difficulty: Hard
Link: https://leetcode.com/problems/sliding-window-maximum/
Date: 2025-10-17
"""

# Time Complexity: O(n), where n is the length of the input array `nums`.
#   - Each element is added and removed from the deque at most once.
# Space Complexity: O(k), where k is the size of the sliding window.
#   - The deque stores at most `k` elements.
from collections import deque

def maxSlidingWindow(nums, k):
    """
    Finds the maximum element in each sliding window of size k in the given array nums.

    Args:
        nums (list[int]): The input array of integers.
        k (int): The size of the sliding window.

    Returns:
        list[int]: A list containing the maximum element in each sliding window.
    """

    # Create a deque to store indices of elements in the current window.
    # The deque will store indices in decreasing order of element values.
    dq = deque()
    result = []

    # Iterate through the array.
    for i in range(len(nums)):
        # Remove elements from the back of the deque that are smaller than the current element.
        # This ensures that the deque always contains indices of elements in decreasing order.
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add the current element's index to the back of the deque.
        dq.append(i)

        # Remove elements from the front of the deque that are outside the current window.
        if dq[0] <= i - k:
            dq.popleft()

        # If the window is full (i.e., we have seen k elements), add the maximum element
        # (which is at the front of the deque) to the result.
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result