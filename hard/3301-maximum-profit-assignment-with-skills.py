"""
Problem: Maximum Profit Assignment with Skills
Number: 3301
Difficulty: Hard
Link: https://leetcode.com/problems/most-profitable-task-schedule/
Date: 2025-10-22
"""

# Time Complexity: O(n log n + m log m), where n is the length of difficulty and profit, and m is the length of worker.
# Space Complexity: O(n), where n is the length of difficulty and profit.

def maxProfitAssignment(difficulty, profit, worker):
    """
    Calculates the maximum profit that can be achieved by assigning workers to jobs.

    Args:
        difficulty (list[int]): A list of integers representing the difficulty of each job.
        profit (list[int]): A list of integers representing the profit of each job.
        worker (list[int]): A list of integers representing the ability of each worker.

    Returns:
        int: The maximum profit that can be achieved.
    """

    jobs = sorted(zip(difficulty, profit))  # Sort jobs by difficulty
    worker.sort()  # Sort workers by ability

    max_profit = 0
    job_index = 0
    best_profit_so_far = 0

    for worker_ability in worker:
        # Find the best job that this worker can do
        while job_index < len(jobs) and jobs[job_index][0] <= worker_ability:
            best_profit_so_far = max(best_profit_so_far, jobs[job_index][1])
            job_index += 1
        max_profit += best_profit_so_far

    return max_profit


# Example usage:
if __name__ == "__main__":
    difficulty1 = [2, 4, 6, 8, 10]
    profit1 = [10, 20, 30, 40, 50]
    worker1 = [4, 5, 6, 7]
    print(maxProfitAssignment(difficulty1, profit1, worker1))  # Output: 100

    difficulty2 = [85, 47, 57]
    profit2 = [24, 66, 99]
    worker2 = [40, 25, 25]
    print(maxProfitAssignment(difficulty2, profit2, worker2))  # Output: 0

    difficulty3 = [13, 37, 53, 59, 84]
    profit3 = [11, 46, 88, 91, 96]
    worker3 = [14, 17, 61, 30, 69]
    print(maxProfitAssignment(difficulty3, profit3, worker3))  # Output: 259