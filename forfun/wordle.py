import re

letters = 'abcdefghijklmnopqrstuvwxyz'
file = open('words.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].lower()
# print(lines)
m = []
for i in letters:
    word = 'sa'+ i +'d'
    if (word in lines):
        print(word, 'found one!')
        m.append(word)
    else:
        print('...')


print(m)
