x = 1
for i in range(1000):
    x *= 2
print(x)
string = str(x)
output = 0
for i in string:
    output += int(i)

print(f'the sum of 2**1000 digits is {output} and the number is {x}')
