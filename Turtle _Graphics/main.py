from turtle import Turtle
import random
tim=Turtle()

# draw square
step=100


def draw_shapes(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(step) 
        tim.right(angle)
colors=['red','blue','green']
for sides in range(3,7):
    color=random.choice(colors)
    tim.color(color)
    draw_shapes(sides)