import turtle
import random
wn = turtle.Screen()
def random_walk(t,steps):
    t.hideturtle()
    for i in range(steps):
        t.forward(random.randrange(51))
        t.right(random.randrange(181))
tess = turtle.Turtle()
tess.speed(0)
random_walk(tess, 50)
wn.mainloop()
