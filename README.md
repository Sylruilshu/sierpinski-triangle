# Sierpinski's Triangle

[![pre-commit hooks](https://github.com/Sylruilshu/sierpinskis-triangle/actions/workflows/ci.yaml/badge.svg)](https://github.com/Sylruilshu/sierpinskis-triangle/actions/workflows/ci.yaml)

**Overview**

This project makes use of tkinter to visualise Sierpinskis triangle and has two main variants.

1. Static:

    Simply constructs and displays the triangle based on preconfigured values. i.e window/triangle size and amount of points used.

2. Cli:

    This variant employs command line arguments and has two versions, both allowing the user to determine the values used to generate the triangle.

    -   Version 1 - does not validate if the initial point is inside the triangle.

    -   Version 2 - does validate if the initial point is inside the triangle.

## Local environment setup

1. Navigate to the root of the project, and create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Once the virtual environment is created, activate it:

    **Linux**

    ```bash
    source venv/bin/activate
    ```

    **Windows**

    ```powershell
    .\venv\Scripts\activate.bat
    ```

3. Install the necessary dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4. Install the pre-commit hooks (optional but recommended)

    ```bash
    pre-commit install
    ```

## Usage

- Run the following command to view available command line arguments:

    ```bash
    python cli/sierpinskis_triangle_v1.py --help
    ```

- To generate the triangle using sensible defaults, run:

    ```bash
    python cli/sierpinskis_triangle_v1.py
    ```

## Installing new dependencies

This project uses `pip-compile` to [manage dependencies](https://youtu.be/LAig6s9Hkj0).

Before adding new dependencies, [ensure you have `pip-tools` installed](https://pypi.org/project/pip-tools/) (this package provides the `pip-compile` command).

To add a new dependency:

-   Add the package name of the new dependency to the `requirements.in` file.
-   Run the following command to pin the dependency and its transitive dependencies in the `requirements.txt` file.

    ```bash
    pip-compile requirements.in
    ```

-   Once the `requirements.txt` file has been regenerated, in an activated virtual environment, run:

    ```bash
    pip install -r requirements.txt