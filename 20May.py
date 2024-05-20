# https://realitystudio.co.uk/

import turtle 

pen = turtle.Turtle()

tri_size = 100

pen.fillcolor("lime")
pen.begin_fill()
for i in range(3):
    pen.forward(tri_size)
    pen.left(120)
pen.end_fill()

pen.up()
pen.goto(tri_size,0)
pen.down()

pen.fillcolor("blue")
pen.begin_fill()
for i in range(3):
    pen.forward(tri_size)
    pen.left(120)
pen.end_fill()

pen.left(120)
pen.forward(tri_size)
pen.right(60)

pen.fillcolor("red")
pen.begin_fill()
for i in range(3):
    pen.forward(tri_size)
    pen.right(120)
pen.end_fill()

turtle.done()