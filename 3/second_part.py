import re

with open("input.txt", "r") as f:
    data = f.read().split("\n")

output = 0
temp_list = []
for i in data:
    l = list(filter(None, re.split(r"\s+", i[0:])))
    l = [eval(k) for k in l]
    temp_list += l
output_list = []
for i in range(int(len(temp_list)/9)):
    for j in range(3):
        output_list+=[[temp_list[9*i+j], temp_list[9*i+3+j], temp_list[9*i+6+j]]]
for i in output_list:
    i.sort()
    if i[0] + i[1] > i[2]:
        output += 1
print(output)