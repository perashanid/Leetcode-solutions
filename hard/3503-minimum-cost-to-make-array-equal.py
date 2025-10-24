"""
Problem: Minimum Cost to Make Array Equal
Number: 3503
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-make-array-equal/
Date: 2025-10-24
"""

def min_cost_to_make_array_equal(nums):
    """
    Calculates the minimum cost to make all elements of the array equal.

    The approach is to find the median of the array and try to make all
    elements equal to the median.  We calculate the cost by finding the
    difference between the target (median) and each number and multiplying
    the absolute difference with the index difference. We use the fact that 
    the total sum of increments = total sum of decrements.

    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(1)
    """
    n = len(nums)
    total_sum = sum(nums)
    
    # Sort the array to find potential median-like targets
    sorted_nums = sorted(nums)
    
    # The target value that all numbers will converge to, given constraint
    target = total_sum // n
    
    # If target is not an integer, then target+1 is also an important candidate
    candidates = [target]
    if (total_sum % n != 0):
        candidates.append(target + 1)
    
    min_cost = float('inf')
    for target in candidates:
        
        cost = 0
        balance = 0
        
        for i in range(n):
            
            # Calculate how much to increment or decrement each element
            diff = nums[i] - target
            
            # Keep track of the overall balance to ensure no error.
            balance += diff
            
            cost += abs(balance)
        
        min_cost = min(min_cost, cost)
    
    return min_cost

# Example Usage:
if __name__ == '__main__':
    nums1 = [1, 2, 3]
    print(f"Minimum cost for {nums1}: {min_cost_to_make_array_equal(nums1)}")  # Output: 2

    nums2 = [1, 0, 5]
    print(f"Minimum cost for {nums2}: {min_cost_to_make_array_equal(nums2)}")  # Output: 6
    
    nums3 = [2,2,2,2,2]
    print(f"Minimum cost for {nums3}: {min_cost_to_make_array_equal(nums3)}")  # Output: 0

    nums4 = [10, 5, 20, 15]
    print(f"Minimum cost for {nums4}: {min_cost_to_make_array_equal(nums4)}")  # Output: 20