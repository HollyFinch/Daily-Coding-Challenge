# I will attempt to draw a simplistic heart today

import turtle

pencil = turtle.Turtle()
pencil.shape("turtle")

def draw_half_of_heart():
    pencil.color("red")
    pencil.setheading(90)

    for i in range(20):
        pencil.forward(1)
        pencil.right(3)

    pencil.circle(50, 90)
    pencil.circle(20, 100)
    pencil.setheading(-120)
    pencil.circle(100, 10)
    pencil.right(160)


#to be continued. This is a loop, not a heart

turtle.done()