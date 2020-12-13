with open("day13/input.txt") as file:
    times = [time for time in [line for line in file.readlines()][1].split(',')]

times = list(zip([i for i in range(len(times))], times))
times = [(int(index), int(time)) for index, time in times if time != 'x']

current_time = 0

print(times)
print (current_time)

while True:
    print(current_time)
    for index, time in times:
        if (current_time + index) % time != 0:
            break
    else:
        print ("Part 2: " + str(current_time))
        break
    compare_time = current_time + times[-1][0]
    while current_time < compare_time:
        current_time += times[0][1]
