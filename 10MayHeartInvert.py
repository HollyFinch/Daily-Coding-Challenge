#First step to inverting the heart shape

import turtle

pencil = turtle.Turtle()
pencil.shape("turtle")

def invert_movement(command, value=None):
  if command == 'forward':
    return 'backward', value * -1
  elif command == 'backward':
    return 'forward', value * -1
  elif command == 'left':
    return 'right', value * -1
  elif command == 'right':
    return 'left', value * -1
  elif command == 'circle':
    return 'circle', value[0], value[1] * -1  
  elif command == 'setheading':
    return 'setheading', value * -1  
  else:
    return command, value 

#note to self: this is a list of commands, not a function, DUH!
heart_shape = [
    ('color', "red"),
    ('setheading', 0),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),
    ('forward', 1),
    ('right', 3.4),#
    ('circle', (50, 90)), 
    ('circle', (20, 100)),  
    ('setheading', -120),
    ('circle', (100, 10)), 
    ('right', 160)
]

def invert_shape(shape):
    inverted_shape = [invert_movement(command, value) for command, value in shape]
    return inverted_shape

leftHeart = invert_shape(heart_shape)

print(leftHeart)

for command, *args in leftHeart:
    getattr(pencil, command)(*args)

pencil.penup()
pencil.goto(0, 0)
pencil.pendown()

for command, value in heart_shape:
    if isinstance(value, tuple):
        getattr(pencil, command)(*value)
    else:
        getattr(pencil, command)(value)    

turtle.done()

#to be continued!.... not perfect, but code works well