"""
Problem: Minimum Cost to Make All Characters Equal
Number: 4008
Difficulty: Medium
Link: null
Date: 2025-10-25
"""

def min_flips(s: str) -> int:
    """
    Calculates the minimum cost required to make all characters in a binary string equal.

    The cost of one operation is 1, where an operation flips all characters from index i to the end of the string.

    Args:
        s: The input binary string.

    Returns:
        The minimum cost to make all characters equal.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1)
    """

    n = len(s)
    flips = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            flips += 1
    return flips

# Example Usage
# s1 = "0011"
# print(min_flips(s1))  # Output: 1

# s2 = "0101"
# print(min_flips(s2))  # Output: 2

# s3 = "1111"
# print(min_flips(s3))  # Output: 0

# s4 = "101"
# print(min_flips(s4))  # Output: 2

# s5 = "0"
# print(min_flips(s5)) #Output 0