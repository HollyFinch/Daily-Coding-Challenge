#improved Sierpinski

import turtle

def draw_triangle(t, size):
    t.fillcolor("gold")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_sierpinski(t, size, depth):
    if depth == 0:
        draw_triangle(t, size)
    else:
        draw_sierpinski(t, size / 2, depth - 1)
        t.forward(size / 2)
        draw_sierpinski(t, size / 2, depth - 1)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        draw_sierpinski(t, size / 2, depth - 1)
        t.left(60)
        t.backward(size / 2)
        t.right(60)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    draw_sierpinski(t, 300, 3) 
    turtle.done()

if __name__ == "__main__":
    main()
