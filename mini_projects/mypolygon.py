import turtle
bob=turtle.Turtle()
def square(t,length):
    for t in range(4):
        bob.fd(length)
        bob.lt(90)

square(bob,500)
