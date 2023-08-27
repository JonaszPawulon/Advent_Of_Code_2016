import re

file = "input.txt"
with open(file, "r") as f:
    data = f.read()


def select_value_from_data(data, temp_pointer):
    x = ""
    while re.match("[0-9]", data[temp_pointer]):
        x += data[temp_pointer]
        temp_pointer += 1
    temp_pointer += 1
    return int(x), temp_pointer


def check_brackets(pointer, data):
    if data[pointer] == "(":
        temp_pointer = pointer + 1
        x, temp_pointer = select_value_from_data(data, temp_pointer)
        y, temp_pointer = select_value_from_data(data, temp_pointer)
        return x, y, temp_pointer


def count_length(data):
    pointer = 0
    _len = 0
    while pointer < len(data):
        if data[pointer] == "(":
            x, y, pointer = check_brackets(pointer, data)
            _len += count_length(data[pointer:pointer+x]) * y
            pointer += x
        else:
            _len += 1
            pointer += 1
    return _len

my_len = count_length(data)
print(my_len)