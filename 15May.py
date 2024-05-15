#Here I am creating a quick Bazier curve with controllabe curvature (I add it in find_midpoint function) - this will help me draw my heart <3 

import turtle

def draw_bezier(p0, controlP, p1, steps=100):
    turtle.penup()
    turtle.goto(p0)
    turtle.pendown()
    
    for i in range(steps + 1):
        t = i / steps  # parameter t ranges from 0 to 1
        #Bézier curve
        #** is the exponent, note to self
        x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * controlP[0] + t**2 * p1[0]
        y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * controlP[1] + t**2 * p1[1]
        turtle.goto(x, y)

def find_midpoint(p0, p2):
    mid_x = (p0[0] + p2[0]) / 2
    mid_y = (p0[1] + p2[1]) / 2
    return (mid_x + 100 , mid_y)

p0 = (0, 0)   
p1 = (0, 150)  
controlP = find_midpoint(p0,p1) 

draw_bezier(p0, controlP, p1)

turtle.done()