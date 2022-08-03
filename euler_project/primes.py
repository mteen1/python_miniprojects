def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True

def prime(n):
    num = 0
    for i in range(2,10**6):
        if num==n:
            break
        if isprime(i):
            prime = i
            num +=1
    print(prime,'is the {}st prime'.format(n))

prime(6)
