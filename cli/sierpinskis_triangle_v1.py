from random import uniform, randint
from tkinter import Tk, Canvas
from math import sin, radians
import click


@click.command()
@click.option(
    "--iterations",
    "-i",
    default=100000,
    type=int,
    help="Amount of points to generate",
)
@click.option(
    "--pixels",
    "-p",
    default=500,
    type=int,
    help="Set window/triangle size",
)
def main(iterations: int, pixels: int) -> None:
    """
    A utility to visualise Sierpinski's triangle (no initial point validation)
    """
    X = pixels
    Y = round(X * sin(radians(60)), 2)
    TRIANGLE_VERTICES = {1: (0, Y), 2: (X, Y), 3: (X / 2, 0)}

    def generate_random_initial_point() -> tuple:
        random_x_coord = round(uniform(0, X), 2)
        random_y_coord = round(uniform(0, Y), 2)
        return (random_x_coord, random_y_coord)

    def determine_starting_point() -> tuple:
        random_index = randint(1, 3)
        return TRIANGLE_VERTICES[random_index]

    def midpoint(a: tuple, b: tuple) -> tuple:
        return (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2))

    root = Tk()
    root.title("Sierpinski's Triangle")
    canvas = Canvas(root, width=X, height=Y, bg="#000000")
    canvas.pack()

    random_point = generate_random_initial_point()
    for _ in range(iterations):
        canvas.create_rectangle(random_point * 2, outline="teal")
        random_starting_point = determine_starting_point()
        average_point = midpoint(random_point, random_starting_point)
        random_point = average_point

    root.mainloop()


main()
