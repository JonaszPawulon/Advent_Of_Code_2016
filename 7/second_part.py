import re

def find_aba(word):
    l = list()
    letters = [word[0], word[1]]
    for i in range(2, len(word)):
        if word[i] == letters[0] and letters[1] != letters[0]:
            l += [letters[0]+letters[1]+word[i]]
        letters[0] = letters[1]
        letters[1] = word[i]
    return l

def reverse(word):
    return word[1]+word[0]+word[1]

with open("input.txt", 'r') as f:
    my_array = f.read().split("\n")
counter = 0
for i in my_array:
    word = re.split('[\[\]]', i)
    flag = False
    outside = list()
    inside = list()
    for j in range(len(word)):
        if j % 2 == 0 and not flag:
            outside += find_aba(word[j])
        elif j % 2 == 1:
            inside += find_aba(word[j])
    for i in inside:
        r = reverse(i)
        if r in outside:
            counter += 1
            break
print(counter)
