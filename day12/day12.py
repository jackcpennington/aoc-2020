with open("day12/input.txt") as file:
    instructions = [(list(line)[0], int("".join(list(line)[1:])))
                    for line in file.read().split("\n")]
def part_1():
    position = (0,0)
    direction = 'E'
    directions = ['N', 'E', 'S', 'W']

    def move(direction, value):
        if direction == 'N':
            return (position[0], position[1] + value)
        if direction == 'S':
            return (position[0], position[1] - value)
        if direction == 'E':
            return (position[0] + value, position[1])
        else: # direction == 'W':
            return (position[0] - value, position[1])

    def rotate(direction, value):
        magnitude = int(value/90)
        if action == 'L':
            return directions[(directions.index(direction)-magnitude) % 4]
        else: # action == 'R'
            return directions[(directions.index(direction)+magnitude) % 4]
        
    for action, value in instructions:
        if action == 'F':
            position = move(direction, value)
        elif action in {'L', 'R'}:
            direction = rotate(direction, value)
        else:
            position = move(action, value)  
    return abs(position[0]) + abs(position[1])

def part_2():
    position = (0, 0)
    waypoint = (10, 1)

    def move(direction, value):
        if direction == 'N':
            return (waypoint[0], waypoint[1] + value)
        if direction == 'S':
            return (waypoint[0], waypoint[1] - value)
        if direction == 'E':
            return (waypoint[0] + value, waypoint[1]) 
        else: # direction == 'W':
            return (waypoint[0] - value, waypoint[1])

    def rotate(direction, value):
        magnitude = int(value/90)
        i=0
        wp = waypoint
        for i in range(magnitude):
            i+=1
            if direction == 'L':
                wp = (int(-1 * wp[1]),  wp[0])
            else: # direction == 'R
                wp =  (wp[1], int(-1 * wp[0]))
        return wp
    
    for action, value in instructions:
        if action == 'F':
            position = (position[0] + (value * waypoint[0]), position[1] + (value * waypoint[1]))
        elif action in {'L', 'R'}:
            waypoint = rotate(action, value)
        else:
            waypoint = move(action, value)
            
    return abs(position[0]) + abs(position[1])

print ("Part 1: " + str(part_1()))
print ("Part 2: " + str(part_2()))
