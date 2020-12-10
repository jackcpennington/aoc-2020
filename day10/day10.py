from collections import Counter
with open("day10/input.txt") as file:
    adapters = [int(line) for line in file.read().split('\n')]

print (adapters)

adapters.sort()

print (adapters)

adapters = [0] + adapters + [adapters[-1] + 3]

print (adapters)

adapter_gaps = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]

print(adapter_gaps)

gap_counts = Counter(adapter_gaps)

print (gap_counts)

result = (gap_counts[1] * gap_counts[3])

print (result)