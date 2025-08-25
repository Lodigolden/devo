# --------------------------------------------------------------------------------------------------
# Creates a C++ (Software) project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from helpers.directory import create_directory

import os
import shutil
from termcolor import colored, cprint


# --------------------------------------------------------------------------------------------------
def create_cpp_project():
    """
    Creates a C++ (Software) project.

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating C++ (Software) Project", attrs=["bold"])

    create_directories()
    create_cmake_file()
    create_gitignore_file()

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("C++ (Software) Project Created", "green", attrs=["bold"])
    print(
        "----------------------------------------------------------------------------------------------------"
    )


# --------------------------------------------------------------------------------------------------
def create_directories():
    """
    Creates all directories for a new C++ (Software) project

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating directories", attrs=["bold"])

    create_directory("src")
    create_directory("inc")
    create_directory("tests")

    print("Directories created")


# --------------------------------------------------------------------------------------------------
def create_cmake_file():
    """
    Creates a CMakeLists.txt file in the root directory.

    """

    print(
        "----------------------------------------------------------------------------------------------------"
    )
    cprint("Creating CMakeLists.txt file", attrs=["bold"])

    cmake_location = os.path.abspath(
        os.path.join(
            os.path.abspath(__file__), "..", "..", "templates", "CMakeLists.txt"
        )
    )
    shutil.copy(cmake_location, os.getcwd())

    print("CMakeLists.txt file created")


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

    print(gitignore_location)

    try:
        shutil.copy(gitignore_location, os.getcwd())
        print(".gitignore file created")
    except PermissionError:
        cprint("Error: Permission denied during copy operation.")
    except Exception as e:
        cprint(f"An unexpected error occured: { e }")
