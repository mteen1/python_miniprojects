file = open("numbers.txt",mode = 'r')
data = file.readlines()
sum = 0
for line in data:
    print(line)
    sum += int(line)

print(sum)
