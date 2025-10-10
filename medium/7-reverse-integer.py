"""
Problem: Reverse Integer
Number: 7
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/
Date: 2025-10-10
"""

# Time Complexity: O(log|x|) - proportional to the number of digits in x
# Space Complexity: O(1) - constant space

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a 32-bit signed integer.

        Args:
            x: The integer to reverse.

        Returns:
            The reversed integer, or 0 if the reversed integer overflows.
        """

        # Determine the sign of the input integer
        sign = -1 if x < 0 else 1

        # Convert the integer to its absolute value
        x = abs(x)

        reversed_x = 0
        while x > 0:
            # Get the last digit of x
            digit = x % 10

            # Check for potential overflow before multiplying by 10
            if reversed_x > (2**31 - 1) // 10:
                return 0
            if reversed_x == (2**31 - 1) // 10 and digit > 7:
                return 0

            if reversed_x < (-2)**31 // 10:
                return 0
            if reversed_x == (-2)**31 // 10 and digit < -8:
                return 0

            # Build the reversed integer
            reversed_x = reversed_x * 10 + digit

            # Remove the last digit from x
            x //= 10

        # Apply the sign to the reversed integer
        reversed_x *= sign

        # Check for overflow after applying the sign and return result
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x