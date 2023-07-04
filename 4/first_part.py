import re

class letter:
    def __init__(self, name):
        self.name = name
        self.value = 1

    def __eq__(self, other):
        if type(other) != type(other):
            return False
        if self.name != other.name:
            return False
        return True

    def increment(self):
        self.value += 1

    def __str__(self):
        return f"{self.name}: {str(self.value)}"

    def __repr__(self):
        return self.__str__()

def my_sort(l):
    return l.value * -1000 + ord(l.name)

with open("input.txt", "r") as f:
    input_list = f.read().split("\n")
sum = 0
for i in input_list:
    data = re.split(r"-", i)
    i_dict = dict()
    for j in data[0:-1]:
        for k in j:
            num = ord(k)
            if i_dict.__contains__(num):
                i_dict.get(num).increment()
            else:
                i_dict.update({num: letter(k)})
    l = list(i_dict.values())
    l.sort(key=my_sort)
    h_list = data[-1].split("[")
    h_set = set()
    num = l[4].value
    l_2 = [j.name for j in l[0:5]]
    num = int(h_list[0])
    s=h_list[1][0:-1]
    flag = True
    for j in s:
        if j not in l_2:
            flag = False
            break
    if flag:
        sum += num

print(sum)