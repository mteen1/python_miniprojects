def jam_zarayeb(x,n):
    sum = 0
    for i in range(1,n+1):
        if i%x==0:
            sum += i
    return sum

print(jam_zarayeb(5,10)+jam_zarayeb(3,10))
