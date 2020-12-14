from math import exp


with open("day13/input.txt") as file:
    times = [time for time in [line for line in file.readlines()][1].split(',')]

times = list(zip([i for i in range(len(times))], times))
times = [(int(index), int(time)) for index, time in times if time != 'x']

current_time = 0

# # brute force
# while True:
#     print(current_time)
#     for index, time in times:
#         if (current_time + index) % time != 0:
#             break
#     else:
#         print ("Part 2: " + str(current_time))
#         break
    
#     current_time += times[0][1]

# https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# example 7,13,x,x,59,x,31,19
# [(0, 7), (1, 13), (4, 59), (6, 31), (7, 19)] (index, time)
# x = 0  (mod  7)
# x = 12 (mod 13)
# x = 55 (mod 59)
# x = 25 (mod 31)
# x = 12 (mod 19)       x = a (mod N) where n = time, a = -index mod time
# X is the answer. Find x 

# convert to modulus form
expressions = [(-index % time, time) for index, time in times]

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
result = (chinese_remainder([e for a, e in expressions], [a for a, e in expressions]))

print ("Part 2: " + str(result))

