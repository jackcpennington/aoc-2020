with open("day15/input.txt") as file:
    nums = [int(n) for n in file.read().split(',')]

print(nums)

def next_n(nums):
    if nums[-1] not in set(nums[:-1]):
        return 0
    else:
        values = []
        prev_count = 0
        for i in range(len(nums)-1, -1, -1):
             if nums[i] == nums[-1]:
                values.append(i+1)
                prev_count += 1
                if prev_count == 2:
                    break
        return abs(values[0] - values[1])


for i in range(2020-len(nums)):
    #print(i)
    nums.append(next_n(nums))

print(nums[-1])

with open("day15/input.txt") as file:
    nums = [int(n) for n in file.read().split(',')]




last, c = nums[-1], {n: i+1 for i, n in enumerate(nums)}
for i in range(len(nums), 30000000):
    c[last], last = i, i - c.get(last, i)
print(last)