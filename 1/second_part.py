def add_to_map(num, direction):

    global advent_map
    global current_location
    for i in range(num):
        if direction == 0:
            current_location[0] += 1
        elif direction == 1:
            current_location[1] += 1
        elif direction == 2:
            current_location[0] -= 1
        elif direction == 3:
            current_location[1] -= 1
        if advent_map.__contains__(tuple(current_location)):
            print(abs(current_location[0])+abs(current_location[1]))
            exit(0)
        else:
            advent_map.add(tuple(current_location))


with open("input.txt", "r") as f:
    file_input = f.read().split(", ")
current_location = [0, 0]
advent_map = set()
advent_map.add(tuple(current_location))
current_direction = 0
for i in file_input:
    if i[0] == 'R':
        current_direction = (current_direction+1) % 4
    elif i[0] == 'L':
        current_direction = (current_direction-1) % 4
    add_to_map(int(i[1:]), current_direction)


