"""
Problem: Minimum Days to Make m Bouquets
Number: 2850
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Date: 2025-11-16
"""

def minDays(bloomDay, m, k):
    """
    You are given an integer array bloomDay, an integer m and an integer k.

    You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

    The garden consists of n flowers, and the i-th flower will bloom on the bloomDay[i] and be available.

    You are allowed to pick flowers that are already bloomed on the same day.

    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

    Time Complexity: O(n log(max(bloomDay))), where n is the length of bloomDay.
    Space Complexity: O(1)
    """

    n = len(bloomDay)
    if m * k > n:
        return -1

    def possible(days):
        """
        Check if it is possible to make m bouquets in 'days' days.
        """
        bouquets = 0
        flowers = 0
        for bloom in bloomDay:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    left, right = 1, max(bloomDay)
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

# Example usage
if __name__ == '__main__':
    bloomDay1 = [1, 10, 3, 10, 2]
    m1 = 3
    k1 = 1
    print(minDays(bloomDay1, m1, k1))  # Output: 3

    bloomDay2 = [1, 10, 3, 10, 2]
    m2 = 3
    k2 = 2
    print(minDays(bloomDay2, m2, k2))  # Output: -1

    bloomDay3 = [7, 7, 7, 7, 12, 7, 7]
    m3 = 2
    k3 = 3
    print(minDays(bloomDay3, m3, k3))  # Output: 12