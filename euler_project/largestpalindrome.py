def ispalindrome(n):
    reverse = ''
    N = str(n)
    length = len(N)
    for i in range(length-1,-1,-1):
        reverse += N[i]
    if reverse == N:
        return True
    else:
        return False
output = 0
for i in range(100,1000):
    for z in range(100,1000):
        if ispalindrome(i*z) and i*z>output:
            output = i*z

print(output)
