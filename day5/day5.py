import math

with open('day5/input.txt') as file:
    seat_paths = [row.rstrip('\n') for row in file.readlines()]

def get_seat(path, lower, upper):
    next_part = path[0]

    middle = lower + (upper - lower) / 2

    if next_part == 'F' or next_part == 'L':
        upper = math.floor(middle)
        if len(path) == 1:
            return min(lower, upper)
    elif next_part == 'B' or next_part == 'R':
        lower = math.ceil(middle)
        if len(path) == 1:
            return max(lower, upper)

    return get_seat(path[1:], lower, upper)

maxi = 0

plane = [[0 for i in range(8)] for j in range(128)]

seat_ids = set()

for seat_path in seat_paths:
    behind, forward = 0, 127
    left, right = 0, 7

    row_path = seat_path[:7]
    col_path = seat_path[-3:]

    row = get_seat(row_path, behind, forward)
    col = get_seat(col_path, left, right)

    plane[row][col] = 1

    seat_id = row * 8 + col

    if seat_id > maxi:
        maxi = seat_id

    seat_ids.add(seat_id)

print("Part 1: " + str(maxi))

empty_seats = set()
for r in range(len(plane)):
    for c in range(len(plane[0])):
        if plane[r][c] == 0:
            empty_seats.add((r, c))


for r, c in empty_seats:
    seat_id = r * 8 + c

    if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
        print ("Part 2: " + str(seat_id))




    