with open("input.txt", "r") as f:
    l_input = f.read().replace('\n', '')

my_output = str()
for i in range(8):
    my_array = {i : 0 for i in range(8*8*4)}
    for j in range(0, len(l_input), 8):
        my_array[ord(l_input[i + j])] += 1
    my_output += chr(max(my_array, key=lambda x: my_array[x]))
print(my_output)
