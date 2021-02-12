import turtle
bob = turtle.Turtle()
bob.speed(0)
for i in range(632):
    bob.forward(200)
    bob.right(1)
    bob.forward(100)
    bob.setpos(0,0)
    bob.left(1.57)
turtle.exitonclick()
