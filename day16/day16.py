with open("day16/input.txt") as file:
    parts = [line.split('\n') for line in [part for part in file.read().split('\n\n')]]

fields = parts[0]
my_ticket = parts[1][1]
nearby_tickets = parts[2][1:]

# print(fields)
# print(my_ticket)
# print(nearby_tickets)

ranges = []
for field in fields:
    field = field.split()
    range_1, range_2 = field[-3], field[-1]
    range_1_l, range_1_u = range_1.split('-')
    range_2_l, range_2_u = range_2.split('-')

    ranges.append((int(range_1_l), int(range_1_u)))
    ranges.append((int(range_2_l), int(range_2_u)))

def check_valid(value):
    for l, u in ranges:
        if l <= value <= u:
            return True
    return False

invalids = []
for ticket in nearby_tickets:
    for value in ticket.split(','):
        if not check_valid(int(value)):
            invalids.append(int(value))

print(sum(invalids))
