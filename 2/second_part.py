with open("input.txt", "r") as f:
    lines = f.read().split("\n")
width = 2
height = 2
output = str()
for i in lines:
    for l in i:
        if l == 'U' and abs(height-2 - 1) + abs(width-2) <= 2:
            height -= 1
        elif l == 'R' and abs(height-2) + abs(width-2 + 1) <= 2:
            width += 1
        elif l == 'D' and abs(height-2 + 1) + abs(width-2) <= 2:
            height += 1
        elif l == 'L' and abs(height-2) + abs(width-2 - 1) <= 2:
            width -= 1

    if (width, height) == (2, 0):
        output += "1"
    elif (width, height) == (1, 1):
        output += "2"
    elif (width, height) == (2, 1):
        output += "3"
    elif (width, height) == (3, 1):
        output += "4"
    elif (width, height) == (0, 2):
        output += "5"
    elif (width, height) == (1, 2):
        output += "6"
    elif (width, height) == (2, 2):
        output += "7"
    elif (width, height) == (3, 2):
        output += "8"
    elif (width, height) == (4, 2):
        output += "9"
    elif (width, height) == (1, 3):
        output += "A"
    elif (width, height) == (2, 3):
        output += "B"
    elif (width, height) == (3, 3):
        output += "C"
    elif (width, height) == (2, 4):
        output += "D"

print(output)