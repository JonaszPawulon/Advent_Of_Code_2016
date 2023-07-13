import hashlib

with open("input.txt", "r") as f:
    my_input = f.read()

i = 0
my_index = 0
my_list = [0 for i in range(8)]
while my_index < 8:
    result = hashlib.md5(bytes(my_input + str(i), "utf-8"))
    result = result.hexdigest()
    if result[0:5] == "00000":
        try:
            res = int(result[5])
            if my_list[res] == 0:
                my_list[res] = result[6]
                my_index += 1
                print(".")

        except Exception:
            pass
    i+=1

s = str()
for i in my_list:
    s += i
print(s)
