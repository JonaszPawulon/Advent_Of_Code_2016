import numpy as np
path = "input.txt"
with open(path, "r") as f:
    data = f.read()

screen = np.zeros((50, 6))

def print_array(arr):
    counter = 0
    for i in range(len(arr[0, :])):
        temp_arr = arr[:, i]
        for j in temp_arr:
            if j != 0:
                print("#", end="")
                counter += 1
            else:
                print(" ", end="")
        print()
    print()
    print(counter)

def shift_array(arr, j):
    arr = list(arr)
    temp_arr = arr[-j:]
    temp_arr += arr[0:-j]
    return temp_arr

def operation(arr, command):
    if command[0:4] == "rect":
        command = command[5:]
        x, y = command.split('x')
        x = int(x)
        y = int(y)
        arr[0:x, 0:y] = 1
    elif command[0:10] == "rotate row":
        command = command[11:]
        i = command.split("=")[1]
        i = int(i.split(" ")[0])
        j = int(command.split(" ")[-1])
        temp_arr = arr[:, i]
        temp_arr = shift_array(temp_arr, j)
        arr[:, i] = temp_arr

    elif command[0:13] == "rotate column":
        command = command[14:]
        i = command.split("=")[1]
        i = int(i.split(" ")[0])
        j = int(command.split(" ")[-1])

        temp_arr = arr[i, :]
        temp_arr = shift_array(temp_arr, j)
        arr[i, :] = temp_arr



for i in data.split("\n"):
    operation(screen, i)
print_array(screen)