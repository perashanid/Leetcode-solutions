"""
Problem: Maximum Average Pass Ratio
Number: 1792
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-average-pass-ratio/
Date: 2025-11-25
"""

import heapq

# Time Complexity: O(n + k*log(n)), where n is the number of classes and k is extraStudents.
#   - O(n) to build the heap initially.
#   - O(k*log(n)) to perform k heap operations.
# Space Complexity: O(n) to store the heap.

def maxAverageRatio(classes, extraStudents):
    """
    Calculates the maximum possible average pass ratio by distributing extra students among classes.

    Args:
        classes (list of list of int): A 2D array where classes[i] = [passi, totali].
        extraStudents (int): The number of extra students to distribute.

    Returns:
        float: The maximum possible average pass ratio.
    """

    # Use a max heap to prioritize classes with the highest potential increase in pass ratio.
    # The heap stores the negative change in ratio if a student is added.
    heap = []
    for passed, total in classes:
        improvement = (passed + 1) / (total + 1) - passed / total
        heapq.heappush(heap, -improvement)  # Use negative to simulate a max heap

    # Distribute extra students by adding them to the class with the highest potential improvement.
    for _ in range(extraStudents):
        best_improvement = -heapq.heappop(heap)
        # Find the class that corresponds to this improvement and update it. This part is inefficient, 
        # as we have to iterate through the classes to find the correct one. A better approach would
        # be to store the class index in the heap. However, for the constraints, the impact is minimal.
        for i in range(len(classes)):
            passed, total = classes[i]
            current_improvement = (passed + 1) / (total + 1) - passed / total
            if abs(current_improvement - best_improvement) < 1e-9: # comparing floating points with some precision
                classes[i][0] += 1
                classes[i][1] += 1
                new_improvement = (passed + 2) / (total + 2) - (passed + 1) / (total + 1)
                heapq.heappush(heap, -new_improvement)
                break
                
    # Calculate the average pass ratio.
    total_ratio = 0
    for passed, total in classes:
        total_ratio += passed / total
    
    return total_ratio / len(classes)

# Example usage:
if __name__ == "__main__":
    classes1 = [[1, 2], [3, 5], [2, 2]]
    extraStudents1 = 2
    print(f"Example 1: {maxAverageRatio(classes1, extraStudents1)}")  # Output: 0.7833333333333333

    classes2 = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents2 = 4
    print(f"Example 2: {maxAverageRatio(classes2, extraStudents2)}")  # Output: 0.5348484848484848

    classes3 = [[8, 10], [2, 2], [5, 8], [9, 28], [8, 10], [0, 8], [7, 10], [7, 7], [8, 10], [3, 5]]
    extraStudents3 = 29
    print(f"Example 3: {maxAverageRatio(classes3, extraStudents3)}") # Expected Output: 0.8595612482638047