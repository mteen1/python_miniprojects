counter = 0
def collatz(n):
    if n==1:
        return 1
    if n%2==0:
        return n/2
    else:
        return 3*n+1
chain = 0
num = 0

for i in range(1,10**6):
    counter = 0
    n=i
    while n!=1:
        counter += 1
        n = collatz(n)
    if counter > chain:
        num=i
        chain = counter
        print("for now",i,"makes the longest chain!")

print("found it:",num,"with",chain,"chains")
