"""
Problem: Zigzag Conversion
Number: 6
Difficulty: Medium
Link: https://leetcode.com/problems/zigzag-conversion/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(n), where n is the length of the string s (to store the zigzag pattern).

def convert(s: str, numRows: int) -> str:
    """
    Converts a string into a zigzag pattern with a given number of rows.

    Args:
        s: The input string.
        numRows: The number of rows in the zigzag pattern.

    Returns:
        The converted string.
    """

    if numRows == 1:
        return s

    rows = ["" for _ in range(numRows)]  # Initialize a list of strings for each row
    row_index = 0  # Start at the first row
    direction = 1  # 1 for down, -1 for up

    for char in s:
        rows[row_index] += char  # Add the character to the current row

        row_index += direction  # Move to the next row

        if row_index == numRows:  # Reached the bottom row
            row_index = numRows - 2  # Move to the second to last row
            direction = -1  # Change direction to up
        elif row_index < 0:  # Reached the top row
            row_index = 1  # Move to the second row
            direction = 1  # Change direction to down

    return "".join(rows)  # Concatenate all the rows into a single string