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

def cesar(word, number):
    return_word = ""
    for i in word:
        return_word+=chr((ord(i)-ord('a')+number)%(ord('z')-ord('a')+1)+ord('a'))
    return return_word

with open("input.txt", "r") as f:
    input_list = f.read().split("\n")
sum = 0
flag = True
for i in input_list:
    phrase = ""
    data = re.split(r"-", i)
    i_dict = dict()
    h_list = data[-1].split("[")
    num = int(h_list[0])
    s = h_list[1][0:-1]
    for j in data[0:-1]:
        word = cesar(j, num)
        if word == "northpole":
            flag = False
        phrase += word+" "
    if not flag:
        print(phrase, num)
        break
