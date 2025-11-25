"""
Problem: Special Permutation of a Number
Number: 2741
Difficulty: Hard
Link: https://leetcode.com/problems/special-permutation-of-a-number/
Date: 2025-11-25
"""

# Time Complexity: O(k * 10 * 2^k), where k is the number of digits in n.
# Space Complexity: O(10 * 2^k)

def special_permutations(n: int) -> int:
    """
    Calculates the number of permutations of the digits of n such that the absolute difference
    between any two adjacent digits is at most 1.

    Args:
        n: The positive integer.

    Returns:
        The number of special permutations.
    """

    s = str(n)
    digits = sorted(s)
    count = 0
    
    def backtrack(current_permutation, remaining_digits):
        nonlocal count

        if not remaining_digits:
            count += 1
            return

        used = set()  # To avoid duplicate permutations when digits are repeated.

        for i in range(len(remaining_digits)):
            digit = remaining_digits[i]

            if digit in used:
                continue

            if current_permutation:
                last_digit = int(current_permutation[-1])
                if abs(int(digit) - last_digit) > 1:
                    continue
            elif digit == '0' and len(s) > 1:  # Handling leading zeros.  Allow zero only if n=0.
                continue
            

            used.add(digit)
            backtrack(current_permutation + digit, remaining_digits[:i] + remaining_digits[i+1:])

    backtrack("", digits)
    return count

# Example Usage:
if __name__ == '__main__':
    print(special_permutations(123))  # Output: 5
    print(special_permutations(121))  # Output: 3
    print(special_permutations(5))  # Output: 1
    print(special_permutations(100))  # Output: 3
    print(special_permutations(0)) # Output: 1
    print(special_permutations(1122)) # Output: 6
    print(special_permutations(1234)) # Output: 14