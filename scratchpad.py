# Rough workings!

from random import uniform, randint
from tkinter import Tk, Canvas


STARTING_POINTS = {1: (0, 866.03), 2: (1000.0, 866.03), 3: (500, 0)}
X = 1000
Y = 866.03


def initial_point() -> tuple:
    random_x_point = round(uniform(0, X), 2)
    random_y_point = round(uniform(0, Y), 2)
    random_point = (random_x_point, random_y_point)
    return random_point


def starting_index() -> tuple:
    random_starting_index = randint(1, 3)
    second = STARTING_POINTS[random_starting_index]
    return second


def midpoint(a: tuple, b: tuple) -> tuple:
    mid = (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2))
    return mid


def initial_setup() -> tuple:
    first_point = initial_point()
    index_point = starting_index()
    return midpoint(first_point, index_point)


window = Tk()
canvas = Canvas(window, width=X, height=Y, bg="#000000")
canvas.pack()

last_point = initial_setup()

for _ in range(100000):
    index_point = starting_index()
    average = midpoint(last_point, index_point)
    last_point = average

    canvas.create_rectangle(last_point * 2, outline="teal")

window.mainloop()
