"""
Problem: Longest Substring Without Repeating Characters
Number: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(min(m, n)), where n is the length of the string s, and m is the size of the character set (e.g., 26 for English alphabet, 128 for ASCII, 256 for extended ASCII). In the worst case, the space is O(n) if all characters are unique.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """

        # Initialize variables
        start = 0          # Start index of the current substring
        end = 0            # End index of the current substring
        max_length = 0     # Length of the longest substring found so far
        char_index_map = {}  # Dictionary to store the most recent index of each character

        # Iterate through the string
        while end < len(s):
            char = s[end]

            # If the character is already in the map and its index is within the current substring
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start of the substring to the next position after the previous occurrence of the character
                start = char_index_map[char] + 1

            # Update the index of the character in the map
            char_index_map[char] = end

            # Update the maximum length if the current substring is longer
            max_length = max(max_length, end - start + 1)

            # Move the end of the substring to the next character
            end += 1

        # Return the maximum length
        return max_length