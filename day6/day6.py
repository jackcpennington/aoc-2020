with open('day6/input.txt') as file:
    part_1 = sum([len(set("".join([x for x in sub.split()]))) for sub in file.read().split('\n\n')])

with open('day6/input.txt') as file:
    part_2 = sum([len(set.intersection(*map(set, [x for x in sub.split()]))) for sub in file.read().split('\n\n')])

print("Part 1: " + str(part_1))
print("Part 2: " + str(part_2))
