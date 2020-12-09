with open("day9/input.txt") as file:
    data = [int(line) for line in file.read().split('\n')]

def part_1(preamble_size):
    def get_prev_nums(data, index, n):
        return data[index-n: index]

    def two_sum(sub_data, x):
        sub_data = set(sub_data) 
        for d in sub_data:
            complement = x - d

            if complement in sub_data:
                return True
        
        return False

    for i in range(preamble_size, len(data)):

        if not two_sum(get_prev_nums(data, i, preamble_size), data[i]):
            return data[i]

part1_result = part_1(25)

def part_2():
    for i in range(len(data)):
        for size in range(2, len(data)): # probably cause out of bounds error
            list_sum = sum(data[i:i+size])
            if list_sum > part1_result:
                break
            if list_sum == part1_result:
                return min(data[i:i+size]) + max(data[i:i+size])
    return -1


print ("Part 1: " + str(part1_result))
print ("Part 2: " + str(part_2()))

