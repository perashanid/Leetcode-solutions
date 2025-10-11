"""
Problem: Number of Islands
Number: 200
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/
Date: 2025-10-11
"""

def numIslands(grid: list[list[str]]) -> int:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid.
    We visit each cell in the grid at most once.
    Space Complexity: O(M * N) in the worst case. This is due to the potential space occupied by the call stack during DFS,
    which can grow up to M * N if the entire grid is filled with land.
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(row, col):
        """
        Performs Depth-First Search to explore an island and mark all connected land cells as visited (water).

        Args:
            row: The row index of the current cell.
            col: The column index of the current cell.
        """

        # Check for boundary conditions and if the cell is water or already visited
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
            return

        # Mark the current cell as visited (water)
        grid[row][col] = '0'

        # Explore adjacent cells recursively
        dfs(row + 1, col)  # Down
        dfs(row - 1, col)  # Up
        dfs(row, col + 1)  # Right
        dfs(row, col - 1)  # Left

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If a cell is land ('1'), start a DFS to explore the island
            if grid[i][j] == '1':
                num_islands += 1  # Increment island count
                dfs(i, j)  # Explore the island and mark visited cells

    return num_islands