import turtle

def draw_heart():
    
    t = turtle.Turtle()

    # ❤️
    for _ in range(3):
        t.forward(50)  
        t.right(90)     

    t.forward(25)
    t.left(90)
    t.forward(80)
    t.left(45)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.left(45)
    t.forward(80)
    t.left(150)
    t.forward(40)       
    t.right(180)

    # Draw right side of the heart
    for _ in range(2):
        t.forward(40)
        t.right(120)

    t.forward(40)

    # Draw bottom part of the heart
    t.right(180)
    t.forward(20)
    t.right(90)
    t.forward(45)

    t.right(90)
    t.circle(28, extent= -180)
    t.right(180)
    t.circle(28, extent= -180)

    t.right(90)
    t.forward(80)
    t.left(90)
    t.forward(30)

    turtle.done()

# Call the function to draw the ❤️
draw_heart()
