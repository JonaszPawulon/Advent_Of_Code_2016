with open("input.txt", "r") as f:
    file_input = f.read().split(", ")
directions = {0: 0, 1: 0, 2: 0, 3: 0}
current_direction = 0
for i in file_input:
    if i[0] == 'R':
        current_direction = (current_direction+1) % 4
    elif i[0] == 'L':
        current_direction = (current_direction-1) % 4
    directions[current_direction] += int(i[1:])

print(abs(directions[0]-directions[2])+abs(directions[1]-directions[3]))