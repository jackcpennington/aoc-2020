with open("day8/input.txt") as file:
    instructions = [tuple(instruction.split()) for instruction in file.read().split('\n')]

ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}

def eval(index, acc, instruction, value):
    op = list(value)[0]
    value = int("".join(list(value)[1:]))

    if instruction == "nop":
        return index + 1, acc
    if instruction == "acc":
        return index + 1, ops[op](acc, value)
    if instruction == "jmp":
        return ops[op](index, value), acc
    return index, acc

def part_1():
    visited_indexes = set()
    index, acc = 0, 0
    while index not in visited_indexes:
        visited_indexes.add(index)
        index, acc = eval(index, acc, instructions[index][0], instructions[index][1])

    return acc

def part_2():
    def change_instruction(instruction):
        if instruction[0] == "jmp":
            return ("nop", instruction[1])
        elif instruction[0] == "nop":
            return ("jmp", instruction[1])
        else:
            return instruction

    for i in range(len(instructions)):
        instructions[i] = change_instruction(instructions[i]) 
        visited_indexes = set()
        index, acc = 0, 0
        while index not in visited_indexes:
            visited_indexes.add(index)
            index, acc = eval(index, acc, instructions[index][0], instructions[index][1])

            if index == len(instructions):
                return acc
        instructions[i] = change_instruction(instructions[i]) #change back after


print ("Part 1: " + str(part_1()))
print ("Part 2: " + str(part_2()))