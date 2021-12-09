import turtle as t
import random
import numpy as np


def generate_color() -> np.array:
    return np.array([random.random(), random.random(), random.random()])


sigmoid = lambda x: 1 / (1 + np.exp(-x))


def predict(layer, w):
    return sigmoid(layer.dot(w))


weights = np.load("save/weights.npy")

wn = t.Screen()
wn.tracer(0)
turtle = t.Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.penup()


def clicked(x, y):
    global color

    turtle.clear()
    color = generate_color()
    turtle.color(color)
    turtle.begin_fill()
    prediction = predict(color, weights)
    turtle.goto(0, 50)
    turtle.write(
        tuple(int(rgb * 255) for rgb in color),
        align="center", font=("Courier New", 32, "bold")
    )
    turtle.goto(0, 0)
    turtle.write(
        prediction,
        align="center", font=("Courier New", 32, "bold")
    )
    turtle.goto(0, -50)
    turtle.write(
        'Green' if prediction >= 0.5 else 'Not Green',
        align="center", font=("Courier New", 32, "bold")
    )
    turtle.end_fill()
    wn.update()


wn.onclick(clicked)
clicked(0, 0)
wn.mainloop()
