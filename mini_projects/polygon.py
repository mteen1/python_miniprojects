import turtle
bob=turtle.Turtle()
def polygon(t,length,n):
    for t in range(n):
        bob.fd(length)
        bob.lt(360/n)
polygon(bob,10,100)
