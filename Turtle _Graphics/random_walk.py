import turtle

import random
t=turtle
tim=t.Turtle()
# generate random rgb colors
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
# fix distance
distance=30
# directions
directions=[0,90,180,270]
tim.pensize(12)
tim.color(random_color())
tim.speed('fastest')
# walk in random directions
for i in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))