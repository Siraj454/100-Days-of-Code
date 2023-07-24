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



distance=30
# directions
directions=[360]
#tim.pensize(2)
tim.color(random_color())
tim.speed('fastest')
# walk in random directions

def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
          tim.color(random_color())
          tim.circle(100)
          #tim.left(10)
          current_heading=tim.heading()+10
          tim.setheading(current_heading)
   
spirograph(5)
secreen=t.Screen()
secreen.exitonclick()