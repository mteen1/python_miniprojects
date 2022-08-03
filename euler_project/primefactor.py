def PrimeFactor(n):
    p = 2
    while n>= p:
        if n%p==0:
            print(p,'*')
            n = n/p
        p += 1

    print(n)

PrimeFactor(22)
