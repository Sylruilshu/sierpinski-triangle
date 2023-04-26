from random import uniform, randint
from tkinter import Tk, Canvas
from math import sin, radians
import click


def generate_random_initial_point(x: float, y: float) -> tuple[float, float]:
    random_x_coord = round(uniform(0, x), 2)
    random_y_coord = round(uniform(0, y), 2)
    return (random_x_coord, random_y_coord)


def determine_starting_point(triangle_vertices: dict[tuple]) -> tuple[float, float]:
    random_index = randint(1, 3)
    return triangle_vertices[random_index]


def midpoint(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    return (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2))


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
    type=float,
    help="Set window/triangle size",
)
def main(iterations: int, pixels: float) -> None:
    """
    A utility to visualise Sierpinski's triangle (no initial point validation)
    """
    width = pixels
    height = round(width * sin(radians(60)), 2)
    triangle_vertices = {1: (0, height), 2: (width, height), 3: (width / 2, 0)}

    root = Tk()
    root.title("Sierpinski's Triangle")
    canvas = Canvas(root, width=width, height=height, bg="#000000")
    canvas.pack()

    random_point = generate_random_initial_point(width, height)

    for _ in range(iterations):
        canvas.create_rectangle(random_point * 2, outline="teal")
        random_starting_point = determine_starting_point(triangle_vertices)
        average_point = midpoint(random_point, random_starting_point)
        random_point = average_point

    root.mainloop()


main()
