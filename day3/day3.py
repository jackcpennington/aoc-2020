with open('day3/input.txt') as file:
    grid = [list(row.rstrip('\n')) for row in file.readlines()] # grid[row][col]




def is_tree(row, col):
    if grid[row][col] == '#':
        return True
    else:
        return False

def traverse(right, down):
    row, col = 0, 0
    count = 0
    while True:
        row, col = row + down, col + right
        # wrap around
        if col > len(grid[0])-1:
            col = col - len(grid[0])
        
        if row > len(grid)-1:
            break
        
        if is_tree(row, col):
            count += 1
    
    return count

def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1

    for right, down in slopes:
        product *= traverse(right, down)

    return product

print("Part 1: " + str(traverse(3, 1)))
print("Part 2: " + str(part_2()))

