def divisible(n):
    divisible = True
    for i in [2,3,4,5,7,9,11,13,16,20]:
        if n%i==0:
            divisible = True
        else:
            divisible = False
            return divisible
    return divisible

num = 1
while True:
    print(num)
    if divisible(num):
        print("found it!,",num)
        break
    else:
        num += 1
