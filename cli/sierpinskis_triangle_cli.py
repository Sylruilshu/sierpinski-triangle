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
    A utility to visualise Sierpinski's triangle
    """
    X = pixels
    Y = round(X * sin(radians(60)), 2)
    AREA = (X * Y) / 2
    TRIANGLE_POINTS = {1: (0, Y), 2: (X, Y), 3: (X / 2, 0)}

    def generate_random_initial_point() -> tuple:
        random_x_coord = round(uniform(0, X), 2)
        random_y_coord = round(uniform(0, Y), 2)
        return (random_x_coord, random_y_coord)

    def determine_starting_point() -> tuple:
        random_index = randint(1, 3)
        return TRIANGLE_POINTS[random_index]

    def midpoint(a: tuple, b: tuple) -> tuple:
        return (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2))

    def area_of_triangle(point_1: tuple, point_2: tuple, point_3: tuple) -> int:
        x1, y1 = point_1[0], point_1[1]
        x2, y2 = point_2[0], point_2[1]
        x3, y3 = point_3[0], point_3[1]
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def is_inside_triangle(random_point: tuple) -> bool:
        a1 = area_of_triangle(random_point, TRIANGLE_POINTS[2], TRIANGLE_POINTS[3])
        a2 = area_of_triangle(TRIANGLE_POINTS[1], random_point, TRIANGLE_POINTS[3])
        a3 = area_of_triangle(TRIANGLE_POINTS[1], TRIANGLE_POINTS[2], random_point)
        return AREA == (a1 + a2 + a3)

    def generate_random_point() -> tuple:
        while True:
            random_point = generate_random_initial_point()
            if is_inside_triangle(random_point):
                break

        return random_point

    root = Tk()
    root.title("Sierpinski's Triangle")
    canvas = Canvas(root, width=X, height=Y, bg="#000000")
    canvas.pack()

    random_point = generate_random_point()
    for _ in range(iterations):
        canvas.create_rectangle(random_point * 2, outline="teal")
        random_starting_point = determine_starting_point()
        average_point = midpoint(random_point, random_starting_point)
        random_point = average_point

    root.mainloop()


main()
