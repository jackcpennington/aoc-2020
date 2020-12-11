import copy

with open("day11/input.txt") as file:
    grid = [list(x) for x in [line for line in file.read().split('\n')]]

def get_neighbours(grid, row, col):
    neighbours = []
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]):
                neighbours.append(grid[row+r][col+c])
    return neighbours

def do_round(grid):
    o_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '.':
                neighbour_count = get_neighbours(o_grid, row, col).count('#')
                if grid[row][col] == 'L' and neighbour_count == 0:
                    grid[row][col] = '#'
                elif grid[row][col] == '#' and neighbour_count >= 4:
                    grid[row][col] = 'L'
    return grid


prev_grid = [[]]
while grid != prev_grid:
    prev_grid = copy.deepcopy(grid)
    grid = do_round(grid)

count = sum(row.count('#') for row in grid)

print("Part 1: " + str(count))
