import turtle
import time
import random

s = turtle.getscreen()
t = turtle.Turtle()
t.clear()

t.pencolor("black")
t.fillcolor("black")
t.speed(10)
t.penup()
t.goto(-225,20)
t.left(90)

for step in range(11):
    t.write(step)
    t.right(90)
    t.pendown()
    t.forward(450)
    t.penup()
    t.backward(450)
    t.left(90)
    t.forward(20)

t.goto(-230,250)
t.pendown()

for i in range(3):
    t.forward(40)
    t.rt(90)
    t.forward(460)
    t.rt(90)

t.penup()
t.forward(20)
t.right(90)
t.pendown()
t.forward(460)
t.penup()
t.rt(90)

for i in range(12):
    t.pendown()
    t.begin_fill()
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.end_fill()
    t.rt(180)
    t.penup()
    t.forward(40)
    t.lt(90)

t.rt(270)
t.forward(40)
t.lt(90)

for i in range(11):
    t.pendown()
    t.begin_fill()
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.rt(90)
    t.forward(20)
    t.end_fill()
    t.rt(180)
    t.penup()
    t.forward(40)
    t.lt(90)

t.pen(pencolor="white", fillcolor="white")
t.home()

red = turtle.Turtle()
red.shape("turtle")
orange = turtle.Turtle()
orange.shape("turtle")
yellow = turtle.Turtle()
yellow.shape("turtle")
green = turtle.Turtle()
green.shape("turtle")
blue = turtle.Turtle()
blue.shape("turtle")
magenta = turtle.Turtle()
magenta.shape("turtle")
purple = turtle.Turtle()
purple.shape("turtle")
black = turtle.Turtle()
black.shape("turtle")

red.pen(pencolor="red", fillcolor="red")
orange.pen(pencolor="orange", fillcolor="orange")
yellow.pen(pencolor="yellow", fillcolor="yellow")
green.pen(pencolor="green", fillcolor="green")
blue.pen(pencolor="blue", fillcolor="blue")
magenta.pen(pencolor="magenta", fillcolor="magenta")
purple.pen(pencolor="purple", fillcolor="purple")
black.pen(pencolor="black", fillcolor="black")

red.penup()
red.goto(-175,-30)
red.rt(270)
red.pendown()
time.sleep(0.5)

orange.penup()
orange.goto(-125,-30)
orange.rt(270)
orange.pendown()
time.sleep(0.5)

yellow.penup()
yellow.goto(-75,-30)
yellow.rt(270)
yellow.pendown()
time.sleep(0.5)

green.penup()
green.goto(-25,-30)
green.rt(270)
green.pendown()
time.sleep(0.5)

blue.penup()
blue.goto(25,-30)
blue.rt(270)
blue.pendown()
time.sleep(0.5)

magenta.penup()
magenta.goto(75,-30)
magenta.rt(270)
magenta.pendown()
time.sleep(0.5)

purple.penup()
purple.goto(125,-30)
purple.rt(270)
purple.pendown()
time.sleep(0.5)

black.penup()
black.goto(175,-30)
black.rt(270)
black.pendown()
time.sleep(0.5)

while True:
    turtle1 = random.choice([red, orange, yellow, green, blue, magenta, purple, black])
    turtle1.forward(random.randint(1, 5))
    if turtle1.ycor() > 250:
        break
    else:
        pass

turtle1.color('gold')
    
turtle.exitonclick()
