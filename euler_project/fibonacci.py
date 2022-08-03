def Fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2))
sum = 0
for i in range(1,33):
    if Fibonacci(i)%2==0:
        sum += Fibonacci(i)
print(sum)
