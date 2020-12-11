import copy

with open("day11/input.txt") as file:
    grid = [list(x) for x in [line for line in file.read().split('\n')]]

def get_visable_seats(grid, row, col):
    #top
    visible_seats = []
    for row_ in range(row-1, -1, -1):
        if grid[row_][col] != '.':
            visible_seats.append(grid[row_][col])
            break
    #topright
    row_temp, col_temp = row, col
    while row_temp > 0 and col_temp < len(grid[0])-1:
        row_temp -= 1
        col_temp += 1
        if grid[row_temp][col_temp] != '.':
            visible_seats.append(grid[row_temp][col_temp])
            break
    #right
    for col_ in range(col+1, len(grid[0])):
        if grid[row][col_] != '.':
            visible_seats.append(grid[row][col_])
            break
    #botright
    row_temp, col_temp = row, col
    while row_temp < len(grid)-1 and col_temp < len(grid[0])-1:
        row_temp += 1
        col_temp += 1
        if grid[row_temp][col_temp] != '.':
            visible_seats.append(grid[row_temp][col_temp])
            break
    #bot
    for row_ in range(row+1, len(grid)):
        if grid[row_][col] != '.':
            visible_seats.append(grid[row_][col])
            break
    #botleft
    row_temp, col_temp = row, col
    while row_temp < len(grid)-1 and col_temp > 0:
        row_temp += 1
        col_temp -= 1
        if grid[row_temp][col_temp] != '.':
            visible_seats.append(grid[row_temp][col_temp])
            break
    #left
    for col_ in range(col-1, -1, -1):
        if grid[row][col_] != '.':
            visible_seats.append(grid[row][col_])
            break
    #topleft
    row_temp, col_temp = row, col
    while row_temp > 0 and col_temp > 0:
        row_temp -= 1
        col_temp -= 1
        if grid[row_temp][col_temp] != '.':
            visible_seats.append(grid[row_temp][col_temp])
            break
    return visible_seats

def do_round(grid):
    o_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '.':
                neighbour_count = get_visable_seats(o_grid, row, col).count('#')
                if grid[row][col] == 'L' and neighbour_count == 0:
                    grid[row][col] = '#'
                elif grid[row][col] == '#' and neighbour_count >= 5:
                    grid[row][col] = 'L'
    return grid

prev_grid = [[]]
while grid != prev_grid:
    prev_grid = copy.deepcopy(grid)
    grid = do_round(grid)

count = sum(row.count('#') for row in grid)

print("Part 2: " + str(count))


