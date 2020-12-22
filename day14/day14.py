
import itertools

with open("day14/input.txt") as file:
    lines = file.read().split('\n')

mask_indexes = [lines.index(line) for line in lines if "".join(list(line)[:4]) == "mask"]
groups = []
for i in range(1,len(mask_indexes)):
    groups.append(lines[mask_indexes[i-1]:mask_indexes[i]])
groups.append(lines[mask_indexes[-1]:])


def get_binary_values(lines):
    binary_values = []

    for line in lines:
        line = line.split()
        value = int(line[-1])
        address = int("".join(list(line[0])[4:-1]))
        value = '{:036b}'.format(value)
        binary_values.append((address, value))

    return binary_values


def apply_mask(mask, value):
    value = list(value)
    for i, bit in enumerate(mask):
        if bit != 'X':
            value[i] = bit

    return "".join(value)


memory = dict()

for group in groups:
    mask = group[0].split()[-1]
    for address, b_value in get_binary_values(group[1:]):
        result = apply_mask(mask, b_value)

        memory[address] = int(result, 2)

# print (memory)
print(sum(memory.values()))


def get_b_address_addresses(mask, address):
    address = list(address)
    for i, bit in enumerate(mask):
        if bit == '1' or bit == 'X':
            address[i] = bit
    
    return "".join(address)


def get_b_address_value(lines):
    items = []
    for line in lines:
        line = line.split()
        value = int(line[-1])
        address = int("".join(list(line[0])[4:-1]))
        address = '{:036b}'.format(address)
        items.append((address, value))
    return items
    
def floating(addr):
    xs = addr.count("X")
    addrs = []
    for i in itertools.product([0,1], repeat=xs):
        new_addr = addr[:]
        for char in i:
            new_addr = new_addr.replace("X", str(char), 1)
        addrs.append(new_addr)
    return addrs


memory = dict()
for group in groups:
    mask = group[0].split()[-1]
    for address, value in get_b_address_value(group[1:]):
        add = get_b_address_addresses(mask, address)
        pos_add = floating(add)
        for addr in pos_add:
            memory[addr] = value

# print (memory)
print(sum(memory.values()))