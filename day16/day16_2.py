with open("day16/input.txt") as file:
    parts = [line.split('\n') for line in [part for part in file.read().split('\n\n')]]

with open("day16/valid_tickets.txt") as file:
    valid_ticks = [tick for tick in file.read().split('\n')]


fields = parts[0]
my_ticket = parts[1][1]
nearby_tickets = parts[2][1:]

all_tickets = [my_ticket] + nearby_tickets

print(fields)
print(my_ticket)
print(nearby_tickets)
print(all_tickets)
print(valid_ticks)
print()


ranges = []
for field in fields:
    field = field.split()
    range_1, range_2 = field[-3], field[-1]
    range_1_l, range_1_u = range_1.split('-')
    range_2_l, range_2_u = range_2.split('-')

    ranges.append((
        (int(range_1_l), int(range_1_u)),
        (int(range_2_l), int(range_2_u))
        ))

def get_field_index(i_tickets):
    list_indexes = []
    for value in i_tickets:
        i_ticket_set = set()
        for i, (range_1, range_2) in enumerate(ranges):
            if range_1[0] <= value <= range_1[1] or range_2[0] <= value <= range_2[1]:
                i_ticket_set.add(i)
        list_indexes.append(i_ticket_set)
    return list_indexes

field_options = []
for i in range(len(valid_ticks[0].split(','))):
    i_tickets = []
    for ticket in valid_ticks:
        i_tickets.append(int(ticket.split(',')[i]))
    field_index = get_field_index(i_tickets)
    # print(i_tickets)
    # print(field_index)
    # print(set.intersection(*field_index))
    field_options.append(set.intersection(*field_index))
    #print()

#print (field_options)

field_options_mapped = dict()
for i, options in enumerate(field_options):
    field_options_mapped[i] = options

#print (field_options_mapped)

def sort_by_values_len(dict):
    dict_len= {key: len(value) for key, value in dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=False)
    sorted_dict = [{item[0]: dict[item [0]]} for item in sorted_key_list]
    return sorted_dict

field_options_mapped = sort_by_values_len(field_options_mapped)

print (field_options_mapped)

for i, (key, value) in enumerate(field_options_mapped):
    print (i, key)

