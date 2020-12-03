with open('day2/input.txt') as file:
    lines = [line.rstrip('\n') for line in file]

def check_valid(low, high, c, pw):
    count = pw.count(c)
    return count <= high and count >= low

def part_1():
    counter = 0

    for line in lines:
        parts = line.split()

        low, high = parts[0].split("-")
        c = parts[1][0]
        pw = parts[2]

        if check_valid(int(low), int(high), c, pw):
            counter += 1
    
    return counter

def check_valid_2(index_1, index_2, c, pw):

    pos_1 = list(pw)[index_1-1] == c
    pos_2 = list(pw)[index_2-1] == c

    return pos_1 != pos_2 # XOR
    

def part_2():
    counter = 0
    for line in lines:
        parts = line.split()

        index_1, index_2 = parts[0].split("-")
        c = parts[1][0]
        pw = parts[2]

        if check_valid_2(int(index_1), int(index_2), c, pw):
            counter += 1
    return counter

print (part_1())
print (part_2())
