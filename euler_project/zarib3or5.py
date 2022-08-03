def zarib3or5(n):
    if n%3==0 or n%5==0:
        return True
sum = 0
for i in range(1,1000):
    if zarib3or5(i):
        sum += i
print(sum)
