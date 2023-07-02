with open("input.txt", "r") as f:
    lines = f.read().split("\n")
length = 1
height = 1
output = str()
for i in lines:
    for l in i:
        if l == 'U' and height > 0:
            height -= 1
        elif l == 'R' and length < 2:
            length += 1
        elif l == 'D' and height < 2:
            height += 1
        elif l == 'L' and length > 0:
            length -= 1

    if (length, height) == (0, 0):
        output += "1"
    elif (length, height) == (1, 0):
        output += "2"
    elif (length, height) == (2, 0):
        output += "3"
    elif (length, height) == (0, 1):
        output += "4"
    elif (length, height) == (1, 1):
        output += "5"
    elif (length, height) == (2, 1):
        output += "6"
    elif (length, height) == (0, 2):
        output += "7"
    elif (length, height) == (1, 2):
        output += "8"
    elif (length, height) == (2, 2):
        output += "9"

print(output)