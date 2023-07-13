import hashlib

with open("input.txt", "r") as f:
    my_input = f.read()

word = str()
i = 0
my_index = 0
while len(word) < 8:
    result = hashlib.md5(bytes(my_input + str(i), "utf-8"))
    result = result.hexdigest()
    if result[0:5] == "00000":
        word += result[5]
    i+=1
print(word)