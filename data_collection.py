import turtle as t
import random
import numpy as np


def generate_color() -> np.array:
    return np.array([random.random(), random.random(), random.random()])


saves = list(np.load("save/colors.npy"))

wn = t.Screen()
wn.tracer(0)
turtle = t.Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.penup()

color = generate_color()
turtle.color(color)
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
wn.update()


def clicked(x, y):
    global color
    if (int(y > 0) + random.random()) >= 0:
        saves.append(np.append(color, int(y > 0)))

    color = generate_color()
    turtle.color(color)
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    wn.update()
    np.save("save/colors.npy", np.array(list(saves)))
    print(len(saves))


wn.onclick(clicked)
wn.mainloop()
