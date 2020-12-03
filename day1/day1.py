from math import prod

with open('day1/input.txt') as file:
    entries = [int(line.rstrip('\n')) for line in file]

entries_set = set(entries)

def part_1(value):
    for entry in entries_set:
        complement = value - entry

        if (complement in entries_set):
            return entry, complement
    return -1

def part_2():
    for entry in entries_set:
        target = 2020 - entry
        
        values = part_1(target)
        if values == -1:
            pass
        else:
            return prod(values) * entry
    return -1


print(part_1(2020))
print(part_2())




