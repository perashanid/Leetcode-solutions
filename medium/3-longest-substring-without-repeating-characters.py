"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s, and m is the size of the character set.
# In the worst case, the entire string contains unique characters, so the space complexity would be O(n).
# In the best case, the string has limited unique characters, so the space complexity would be O(m).
def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters in a given string.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """

    # Use a sliding window approach to track the current substring.
    # Use a set to efficiently check for repeating characters.

    char_set = set()  # Store characters in the current substring.
    left = 0  # Left pointer of the sliding window.
    max_length = 0  # Length of the longest substring found so far.

    for right in range(len(s)):  # Iterate through the string using the right pointer.
        while s[right] in char_set:  # If the current character is already in the set (repeating).
            char_set.remove(s[left])  # Remove the leftmost character from the set.
            left += 1  # Move the left pointer to the right, shrinking the window.

        char_set.add(s[right])  # Add the current character to the set.
        max_length = max(max_length, right - left + 1)  # Update the maximum length.

    return max_length