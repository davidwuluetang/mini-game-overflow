# Author(s): David Tang

'''
This function receive a grid(2d array) and check whether
the absolute value of each cell equal or exceeded the number
of "neighbors". If true, that cell is consider "overflow".
For example, cell in corners have 2 neighbor cells, other
cells on edge have 3 neighbor cells, and cell inside have
4 neighbor cells. Function return all overflow cell 
tuple(coordinate), or "None" if no overflow cell.
'''
def get_overflow_list(grid):
    tuples_list = []
    last_row_index = len(grid) - 1
    last_col_index = len(grid[0]) - 1

    # Check corners
    corners = [(0, 0),
            (0, last_col_index),
            (last_row_index, 0),
            (last_row_index, last_col_index)
            ]

    for corner in corners:
        row, col = corner
        if abs(grid[row][col]) >= 2:
            tuples_list.append(corner)

    # Check top and bottom edge
    for col in range(1, last_col_index):
        if abs(grid[0][col]) >= 3:
            tuples_list.append([0, col])
        if abs(grid[last_row_index][col]) >= 3:
            tuples_list.append([last_row_index, col])

    # Check left and right edge
    for row in range(1, last_row_index):
        if abs(grid[row][0]) >= 3:
            tuples_list.append([row, 0])
        if abs(grid[row][last_col_index]) >= 3:
            tuples_list.append([row, last_col_index])

    # Check inside cells
    for row in range(1, last_row_index):
        for col in range(1, last_col_index):
            if abs(grid[row][col]) >= 4:
                tuples_list.append([row, col])

    if len(tuples_list) > 0:
        return tuples_list
    
    return None


'''
This function a grid(2d array) and a queue as arguments. The function will
Check if the grid is "overflowed" or not. A grid is consider when it contain
overflow cell and the cell sign of all cell are not the same. Then the function
will perform a "iteration" to get a new grid. All overflow cell item become zero
and the adjacent cell of overflowed cell will gain 1 item according to overflow
cell sign (If overflow cell is positive, adjacent cell plus 1, vice versa).
After the new grid is produced, a copy it will added to the queue. Then continue
to perform "iteration" until the grid no long consider be "overflowed". Function
return the number of "iteration" had performed.
'''
def overflow(grid, a_queue):
    overflow_cell = get_overflow_list(grid)
    
    if overflow_cell != None and all_cell_same_sign(grid) == False:
        max_row, max_col = len(grid), len(grid[1])
        # All overflow cells are same sign, only need to check once.
        row, col = overflow_cell[0]
        cell_sign = check_sign(grid[row][col])

        neighbor_cell = [] # hold coordinate of all overflow's neighbor cell
        
        # For each overflowed cell, set item to 0.
        # Then find their adjacent cell coordinate,
        # add them to neighbor_cell list.
        for coordinate in overflow_cell:
            row, col = coordinate
            grid[row][col] = 0
            # Check boundary before add to neighbor_cell list
            if row - 1 >= 0:
                neighbor_cell.append([row-1, col]) # Top
            if row + 1 < max_row:
                neighbor_cell.append([row+1, col]) # Bottom
            if col - 1 >= 0:
                neighbor_cell.append([row, col-1]) # Left
            if col + 1 < max_col:
                neighbor_cell.append([row, col+1]) # Right

        # For each neighbor cell add 1 item according to cell_sign.
        for coordinate in neighbor_cell:
            row, col = coordinate
            if cell_sign == 1:
                grid[row][col] = abs(grid[row][col]) + 1
            else:
                grid[row][col] = 0 - abs(grid[row][col]) - 1

        # Capture a copy of current grid and add it to 'a_queue'
        capture_grid = []
        for i in range(len(grid)):
            capture_grid.append(grid[i].copy())
        a_queue.enqueue(capture_grid)

        return overflow(grid, a_queue) + 1
    else:
        return 0



''' overflow() helper function

This function receive a non zero number as
argument and check the sign. If is positive,
function return 1, else return 0.
'''
def check_sign(num):
    if num > 0:
        return 1
    return -1



''' overflow() helper function

This function receive 2d array list(grid) as
argument and check all the non zero number
are same sign. If all are same sign, function
return True, else return False.
'''
def all_cell_same_sign(grid):
    max_row = len(grid)
    max_col = len(grid[1])
    positive = 0
    negative = 0
    all_same = True

    # Loop through the grid, count positive and negative
    # numbers. If at least 1 positive and 1 negative found,
    # break the loop.
    for row in range(max_row):
        for col in range(max_col):
            if grid[row][col] > 0:
                positive += 1
                if positive and negative:
                    all_same = False
                    break
            elif grid[row][col] < 0:
                negative += 1
                if positive and negative:
                    all_same = False
                    break
        if all_same == False: break

    return all_same