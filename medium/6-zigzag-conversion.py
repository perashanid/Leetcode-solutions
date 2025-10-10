"""
Problem: Zigzag Conversion
Number: 6
Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n), where n is the length of the input string s, due to the storage of rows.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern based on the given number of rows.

        Args:
            s (str): The input string to be converted.
            numRows (int): The number of rows in the zigzag pattern.

        Returns:
            str: The converted string read line by line.
        """

        if numRows == 1:
            return s

        rows = [''] * numRows  # Initialize an empty string for each row.
        current_row = 0  # Start from the first row.
        going_down = False  # Initially, the direction is going up.

        for char in s:
            rows[current_row] += char  # Append the character to the current row.

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down  # Change direction at top and bottom rows.

            current_row += 1 if going_down else -1  # Move to the next row in the correct direction.

        return ''.join(rows)  # Concatenate the rows to form the result string.