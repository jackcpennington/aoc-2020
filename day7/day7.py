with open("day7/input.txt") as file:
    rules = file.read().split("\n")

def part_1():
    bags = dict()
    for rule in rules:
        bag, sub_bags = rule.split("contain")

        bag = bag.split()
        bag = bag[0] + bag[1]

        sub_bags = set([bag.split()[1] + bag.split()[2] for bag in sub_bags.split(",")])

        bags[bag] = sub_bags

    #print(bags)

    def contain_shinygold(sub_bags):
        if "shinygold" in sub_bags:
            return True
        if "otherbags." in sub_bags:
            return False

        in_a_bag = False
        for sub_bag in sub_bags:
            if contain_shinygold(bags[sub_bag]):
                in_a_bag = True
        return in_a_bag

    return sum([contain_shinygold(bags[bag]) for bag in bags.keys()])
    
def part_2():
    bags = dict()
    for rule in rules:
        bag, sub_bags = rule.split("contain")

        bag = bag.split()
        bag = bag[0] + bag[1]

        sub_bags = set([(bag.split()[0], bag.split()[1] + bag.split()[2]) for bag in sub_bags.split(",")])

        bags[bag] = sub_bags

    def count_sub_bags(n, bag):
        if bags[bag] == {('no', 'otherbags.')}:
            return 1
        
        count = 1
        for sub_n, sub_bag in bags[bag]:
            count += int(sub_n) * count_sub_bags(sub_n, sub_bag)

        return count
    return count_sub_bags(1, "shinygold") - 1

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))

