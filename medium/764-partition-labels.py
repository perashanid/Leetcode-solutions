"""
Problem: Partition Labels
Number: 764
Difficulty: Medium
Link: https://leetcode.com/problems/partition-labels/
Date: 2025-10-12
"""

# Time Complexity: O(n), where n is the length of the string s. We iterate through the string twice.
# Space Complexity: O(1), because the character map can have at most 26 entries (for lowercase English letters).

def partitionLabels(s: str) -> list[int]:
    """
    Partitions a string into as many parts as possible such that each letter appears in at most one part.

    Args:
        s: The input string.

    Returns:
        A list of integers representing the size of these parts.
    """

    # Create a map to store the last occurrence of each character in the string.
    last_occurrence = {}
    for i, char in enumerate(s):
        last_occurrence[char] = i

    # Initialize variables to track the start and end of the current partition.
    start = 0
    end = 0
    result = []

    # Iterate through the string.
    for i, char in enumerate(s):
        # Update the end of the current partition to the last occurrence of the current character.
        end = max(end, last_occurrence[char])

        # If we have reached the end of the current partition, add the size of the partition to the result.
        if i == end:
            result.append(end - start + 1)
            # Reset the start to the next character's index
            start = i + 1

    return result