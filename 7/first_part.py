import re

def is_abba(word):
    flag = False
    letters = [word[0], word[1]]
    for i in range(2, len(word)):
        try:
            if word[i] == letters[1] and letters[1] != letters[0]:
                if word[i+1] == letters[0]:
                    return True
            letters[0] = letters[1]
            letters[1] = word[i]
        except IndexError:
            return False
    return False

with open("input.txt", 'r') as f:
    my_array = f.read().split("\n")
counter = 0
for i in my_array:
    word = re.split('[\[\]]', i)
    flag = False
    for j in range(len(word)):
        if j%2 == 0 and not flag:
            if is_abba(word[j]):
                flag = True
        elif j%2 == 1:
            if is_abba(word[j]):
                flag = False
                break
    if flag:
        counter += 1
print(counter)
