import re


def select_value_from_data(data, temp_pointer):
    x = ""
    while re.match("[0-9]", data[temp_pointer]):
        x += data[temp_pointer]
        temp_pointer += 1
    temp_pointer += 1
    return int(x), temp_pointer


file = "input.txt"
with open(file, "r") as f:
    data = f.read()

output = ""
pointer = 0
while pointer < len(data):
    if data[pointer] == "(":
        temp_pointer = pointer + 1
        x, temp_pointer = select_value_from_data(data, temp_pointer)
        y, temp_pointer = select_value_from_data(data, temp_pointer)
        output += data[temp_pointer:temp_pointer+x]*y
        pointer = temp_pointer + x
    else:
        output += data[pointer]
        pointer += 1

print(output)
print(len(output))