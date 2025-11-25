"""
Problem: Count Special Integers in Range
Number: 2876
Difficulty: Hard
Link: https://leetcode.com/problems/count-special-integers/
Date: 2025-11-25
"""

# Time Complexity: O(log(n)^2) due to the recursion and digit extraction.
# Space Complexity: O(log(n)) due to the recursion stack and storing digits.

class Solution:
    def countSpecialIntegers(self, n: int) -> int:
        """
        Counts the number of special integers between 1 and n (inclusive).
        A special integer is defined as an integer which has no repeating digits.

        Args:
            n: The upper bound of the range (inclusive).

        Returns:
            The number of special integers in the range [1, n].
        """

        s = str(n)
        length = len(s)
        
        # Calculate the number of special integers with length less than len(n)
        ans = 0
        for i in range(1, length):
            ans += 9 * self.permutation(9, i - 1)

        # Calculate the number of special integers with length equal to len(n)
        seen = set()
        for i in range(length):
            digit = int(s[i])
            for j in range(0 if i > 0 else 1, digit):
                if j not in seen:
                    ans += self.permutation(10 - (i + 1), length - (i + 1))

            if digit in seen:
                break
            seen.add(digit)
            if i == length - 1:
                ans += 1

        return ans

    def permutation(self, n: int, k: int) -> int:
        """
        Calculates the permutation P(n, k) = n! / (n-k)!
        """
        res = 1
        for i in range(k):
            res *= (n - i)
        return res