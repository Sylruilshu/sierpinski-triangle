# Sierpinski's Triangle

[![pre-commit hooks](https://github.com/Sylruilshu/sierpinskis-triangle/actions/workflows/ci.yaml/badge.svg)](https://github.com/Sylruilshu/sierpinskis-triangle/actions/workflows/ci.yaml)

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

## Running the program

Run the following command to view avaliable command line arguments:
```bash
python cli/sierpinskis_triangle_cli.py --help
```

To generate the triangle using sensible defaults, run:
```bash
python cli/sierpinskis_triangle_cli.py
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