#!/usr/bin/python3
"""5-island_perimeter module"""


def island_perimeter(grid):
    """A function that returns the perimeter of an island."""
    height = len(grid)
    width = len(grid[0])
    perimeter = 0
    row_max = height - 1
    col_max = width - 1

    for row in range(height):
        for col in range(width):
            if col == 0:
                prev_cell = 1
            else:
                prev_cell = grid[row][col - 1]
            if col == col_max:
                next_cell = 1
            else:
                next_cell = grid[row][col + 1]
            if row == 0:
                up_cell = 1
            else:
                up_cell = grid[row - 1][col]
            if row == row_max:
                down_cell = 1
            else:
                down_cell = grid[row + 1][col]

            cell = grid[row][col]
            if cell == 0:
                pass
            elif cell == 1:
                if (row == 0 or row == row_max) and cell == 1:
                    if col == 0 or col == col_max:
                        perimeter += 2
                    else:
                        perimeter += 1
                elif (col == 0 or col == col_max) and cell == 1:
                    perimeter += 1
                if prev_cell == 0:
                    perimeter += 1
                if next_cell == 0:
                    perimeter += 1
                if up_cell == 0:
                    perimeter += 1
                if down_cell == 0:
                    perimeter += 1

    return (perimeter)
