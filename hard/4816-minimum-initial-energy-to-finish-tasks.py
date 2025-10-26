"""
Problem: Minimum Initial Energy to Finish Tasks
Number: 4816
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
Date: 2025-10-26
"""

# Time Complexity: O(n log n), due to sorting the tasks array.
# Space Complexity: O(1), as we are sorting in place and using a constant amount of extra space.

def minimum_initial_energy(tasks):
    """
    Calculates the minimum initial energy required to finish all tasks.

    Args:
        tasks (list of list): A list of tasks, where each task is a list of [actual_energy, minimum_energy].

    Returns:
        int: The minimum initial energy required to finish all tasks.
    """

    # Sort the tasks based on the difference between minimum and actual energy in descending order.
    # This ensures that tasks with a larger difference are performed first, minimizing the initial energy.
    tasks.sort(key=lambda task: task[1] - task[0], reverse=True)

    initial_energy = 0
    current_energy = 0

    # Iterate through the sorted tasks.
    for actual_energy, minimum_energy in tasks:
        # If the current energy is less than the minimum energy required for the task,
        # update the initial energy to ensure we can perform the task.
        if current_energy < minimum_energy:
            initial_energy += (minimum_energy - current_energy)
            current_energy = minimum_energy

        # Deduct the actual energy spent on the task from the current energy.
        current_energy -= actual_energy

    return initial_energy

# Example Usage and Test Cases:
if __name__ == '__main__':
    # Example 1
    tasks1 = [[1, 2], [2, 4], [4, 8]]
    print(f"Minimum initial energy for tasks {tasks1}: {minimum_initial_energy(tasks1)}")  # Output: 8

    # Example 2
    tasks2 = [[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]
    print(f"Minimum initial energy for tasks {tasks2}: {minimum_initial_energy(tasks2)}")  # Output: 32

    # Example 3
    tasks3 = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
    print(f"Minimum initial energy for tasks {tasks3}: {minimum_initial_energy(tasks3)}")  # Output: 27

    # Test case 4
    tasks4 = [[7, 10], [3, 5], [6, 8]]
    print(f"Minimum initial energy for tasks {tasks4}: {minimum_initial_energy(tasks4)}") # Output: 13

    # Test case 5: Empty list
    tasks5 = []
    print(f"Minimum initial energy for tasks {tasks5}: {minimum_initial_energy(tasks5)}") # Output: 0