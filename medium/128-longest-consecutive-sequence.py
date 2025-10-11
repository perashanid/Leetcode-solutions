"""
Problem: Longest Consecutive Sequence
Number: 128
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Date: 2025-10-11
"""

def longestConsecutive(nums):
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    For example:
    longestConsecutive([100,4,200,1,3,2]) == 4
    longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_set = set(nums)  # Convert the list to a set for O(1) lookup
    longest_streak = 0

    for num in num_set:
        # Check if the current number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Iterate to find consecutive elements
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak if necessary
            longest_streak = max(longest_streak, current_streak)

    return longest_streak