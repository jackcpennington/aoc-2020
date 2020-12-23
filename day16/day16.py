with open("day16/input.txt") as file:
    parts = [line.split('\n') for line in [part for part in file.read().split('\n\n')]]

fields = parts[0]
my_ticket = parts[1][1]
nearby_tickets = parts[2][1:]

print(fields)
print(my_ticket)
print(nearby_tickets)

ranges = []
for field in fields:
    field = field.split()
    range_1, range_2 = field[-3], field[-1]
    range_1_l, range_1_u = range_1.split('-')
    range_2_l, range_2_u = range_2.split('-')

    ranges.append((int(range_1_l), int(range_1_u)))
    ranges.append((int(range_2_l), int(range_2_u)))

print(ranges)

def check_valid(value):
    for l, u in ranges:
        if l <= value <= u:
            return True
    return False

invalids = []
invalid_ticks = []
for ticket in nearby_tickets:
    for value in ticket.split(','):
        if not check_valid(int(value)):
            invalid_ticks.append(ticket)
            invalids.append(int(value))

print(invalids)
print(invalid_ticks)

valid_tickets = list(set(nearby_tickets) - set(invalid_ticks))
print (valid_tickets)

with open('day16/valid_tickets.txt', 'w') as f:
    for item in valid_tickets:
        f.write("%s\n" % item)