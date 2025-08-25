# --------------------------------------------------------------------------------------------------
# Creates a Python project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from helpers.directory import create_directory

import os
import shutil
from termcolor import colored, cprint


# --------------------------------------------------------------------------------------------------
def create_python_project():
    """
    Creates a Python project.

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating Python Project", attrs=["bold"])

    create_directories()
    create_gitignore_file()
    create_pytoml_file()

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Python Project Created", "green", attrs=["bold"])
    print(
        "----------------------------------------------------------------------------------------------------"
    )


# --------------------------------------------------------------------------------------------------
def create_directories():
    """
    Creates all directories for a new Python project

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating directories")

    create_directory("src")
    create_directory("tests")

    print("Directories created")


# --------------------------------------------------------------------------------------------------
def create_gitignore_file():
    """
    Creates a .gitignore file in the root directory.

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating .gitignore file", attrs=["bold"])

    gitignore_location = os.path.abspath(
        os.path.join(os.path.abspath(__file__), "..", "..", "templates", ".gitignore")
    )
    shutil.copy(gitignore_location, os.getcwd())

    print(".gitignore file created")

# --------------------------------------------------------------------------------------------------
def create_pytoml_file():
    """
    Createes a pyproject.toml file in the root directory.

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating pyproject.toml file", attrs=["bold"])

    gitignore_location = os.path.abspath(
        os.path.join(os.path.abspath(__file__), "..", "..", "templates", "pyproject.toml")
    )
    shutil.copy(gitignore_location, os.getcwd())

    print("pyproject.toml file created")
