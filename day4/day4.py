with open('day4/input.txt') as file:
    passports =  [[x for x in sub.split()] for sub in file.read().split('\n\n')]

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} # cid not needed

def part_1():
    valid_count = 0

    for passport in passports:
        passport_fields = set()

        for data in passport:
            field, value = data.split(':')
            passport_fields.add(field)
        
        if fields.issubset(passport_fields):
            valid_count += 1
    return valid_count

def check_format(field, value):
    if field == "byr":
        return value.isnumeric() and int(value) >= 1920 and int(value) <= 2002
    elif field == "iyr":
        return value.isnumeric() and int(value) >= 2010 and int(value) <= 2020
    elif field == "eyr":
        return value.isnumeric() and int(value) >= 2020 and int(value) <= 2030
    elif field == "hgt":
        unit = "".join(list(value)[-2:])
        measure = "".join(list(value)[:-2])
        if unit == "cm":
            return int(measure) >= 150 and int(measure) <= 193
        elif unit == "in": 
            return int(measure) >= 59 and int(measure) <= 76
    elif field == "hcl":
        if list(value)[0] == '#':
            colour = "".join(list(value)[1:])
            if len(colour) == 6:
                try:
                    int(colour, 16)
                    return True
                except ValueError:
                    return False
    elif field == "ecl":
        return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    elif field == "pid":
        return value.isnumeric() and len(value) == 9
    return False


def part_2():
    valid_count = 0

    for passport in passports:
        passport_fields = set()
        for data in passport:
            field, value = data.split(':')
            if field != "cid":
                if not check_format(field, value):
                    break
                passport_fields.add(field)

        if fields.issubset(passport_fields):
            valid_count += 1
        
    return valid_count

print ("Part 1: " + str(part_1()))
print ("Part 2: " + str(part_2()))
