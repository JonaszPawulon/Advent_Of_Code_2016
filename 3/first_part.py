import re

with open("input.txt", "r") as f:
    data = f.read().split("\n")

output = 0
for i in data:
    l = list(filter(None, re.split(r"\s+", i[0:])))
    l = [eval(k) for k in l]
    l.sort()
    if int(l[0]) + int(l[1]) > int(l[2]):
        output += 1
        print(l)
print(output)