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


def area_of_triangle(
    point_1: tuple[float, float],
    point_2: tuple[float, float],
    point_3: tuple[float, float],
) -> float:
    x1, y1 = point_1[0], point_1[1]
    x2, y2 = point_2[0], point_2[1]
    x3, y3 = point_3[0], point_3[1]
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)


def is_inside_triangle(
    random_point: tuple[float, float], triangle_vertices: dict[tuple], area: float
) -> bool:
    a1 = area_of_triangle(random_point, triangle_vertices[2], triangle_vertices[3])
    a2 = area_of_triangle(triangle_vertices[1], random_point, triangle_vertices[3])
    a3 = area_of_triangle(triangle_vertices[1], triangle_vertices[2], random_point)
    return area == (a1 + a2 + a3)


def generate_random_point(
    x: float, y: float, triangle_vertices: dict[tuple], area: float
) -> tuple[float, float]:
    while True:
        random_point = generate_random_initial_point(x, y)
        if is_inside_triangle(random_point, triangle_vertices, area):
            break

    return random_point


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
    A utility to visualise Sierpinski's triangle (initial point validation)
    """
    width = pixels
    height = round(width * sin(radians(60)), 2)
    area = (width * height) / 2
    triangle_vertices = {1: (0, height), 2: (width, height), 3: (width / 2, 0)}

    root = Tk()
    root.title("Sierpinski's Triangle")
    canvas = Canvas(root, width=width, height=height, bg="#000000")
    canvas.pack()

    random_point = generate_random_point(width, height, triangle_vertices, area)

    for _ in range(iterations):
        canvas.create_rectangle(random_point * 2, outline="teal")
        random_vertex_point = determine_starting_point(triangle_vertices)
        average_point = midpoint(random_point, random_vertex_point)
        random_point = average_point

    root.mainloop()


main()
