"""
Problem: Island Perimeter
Number: 463
Difficulty: Easy
Link: https://leetcode.com/problems/island-perimeter/
Date: 2025-10-16
"""

def island_perimeter(grid: list[list[int]]) -> int:
    """
    You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.

    Compute the perimeter of the island.

    Approach:
    Iterate through each cell in the grid. If a cell is land (grid[i][j] == 1), check its four neighbors (up, down, left, right).
    If a neighbor is water (grid[i][j] == 0) or is out of bounds, then add 1 to the perimeter.
    This works because each side of a land cell that is adjacent to water or the boundary contributes to the perimeter.

    Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the grid. We iterate through each cell in the grid once.
    Space Complexity: O(1). We only use a constant amount of extra space to store the perimeter.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter