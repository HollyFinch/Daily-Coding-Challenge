#first draft of SIERPINSKI TRIANGLE 📐


import turtle

t = turtle.Turtle()

sideLength = 100

t.fillcolor("gold")
t.begin_fill()

for i in range(3):
    t.left(120)
    t.forward(sideLength)
t.end_fill()

t.fillcolor("white")
t.begin_fill()

t.left(180)
t.forward(sideLength/2)

t.right(60)
t.forward(sideLength/2)

for i in range(2):
    t.right(120)
    t.forward(sideLength/2)

t.end_fill()

turtle.done()