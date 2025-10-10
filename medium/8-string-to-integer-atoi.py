"""
Problem: String to Integer (atoi)
Number: 8
Difficulty: Medium
Link: https://leetcode.com/problems/string-to-integer-atoi/
Date: 2025-10-10
"""

# Time Complexity: O(n), where n is the length of the input string.
# Space Complexity: O(1), as we use a constant amount of extra space.

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer.

        Args:
            s: The input string.

        Returns:
            The converted integer.
        """

        sign = 1  # Initialize the sign as positive
        result = 0  # Initialize the result
        index = 0  # Initialize the index to traverse the string
        n = len(s)  # Get the length of the string

        # 1. Skip leading whitespace
        while index < n and s[index] == ' ':
            index += 1

        # 2. Check for sign
        if index < n and (s[index] == '+' or s[index] == '-'):
            sign = -1 if s[index] == '-' else 1
            index += 1

        # 3. Read in digits until non-digit character or end of string
        while index < n and s[index].isdigit():
            digit = int(s[index])

            # 4. Convert digits to integer
            # Check for overflow before multiplying by 10
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            if result < (-2**31) // 10 or (result == (-2**31) // 10 and digit < -8):
                return 2**31 - 1 if sign == 1 else -2**31

            result = result * 10 + digit
            index += 1

        # 5. Apply sign and clamp to 32-bit range
        result *= sign
        
        # 6. Clamp the result to the 32-bit signed integer range
        min_int = -2**31
        max_int = 2**31 - 1
        if result < min_int:
            return min_int
        if result > max_int:
            return max_int

        return result