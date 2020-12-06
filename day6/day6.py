with open('day6/input.txt') as file:
    part_1 = sum(map(len, [set("".join([x for x in sub.split()])) for sub in file.read().split('\n\n')]))

print ("Part 1: " + str(part_1))