# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from base import Project

import os
import shutil
from termcolor import colored, cprint

# --------------------------------------------------------------------------------------------------
class Python(Project):
    # ----------------------------------------------------------------------------------------------
    def __init__(self):
        """
        The default constructor initializes the base class, and creates a Python project. 
        """

        super().__init__()

        print(
        "----------------------------------------------------------------------------------------------------"
        )
        cprint("Creating Python Project", attrs=["bold"])

        self.create_directories()
        self.create_gitignore_file()
        self.create_pytoml_file()

        print(
            "----------------------------------------------------------------------------------------------------"
        )
        cprint("Python Project Created", "green", attrs=["bold"])
        print(
            "----------------------------------------------------------------------------------------------------"
        )

    # ----------------------------------------------------------------------------------------------
    def create_directories(self):
        """
        Creates all directories for a new Python project.
        """

        print(
        "----------------------------------------------------------------------------------------------------"
        )
        cprint("Creating directories")

        super()._create_directory("src")
        super()._create_directory("tests")

        print("Directories created")

    # ----------------------------------------------------------------------------------------------
    def create_gitignore_file(self):
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

    # ----------------------------------------------------------------------------------------------
    def create_pytoml_file():
        """
        Creates a pyproject.toml file in the root directory.
        """

        print(
        "----------------------------------------------------------------------------------------------------"
        )
        cprint("Creating pyproject.toml file", attrs=["bold"])

        gitignore_location = os.path.abspath(
            os.path.join(
                os.path.abspath(__file__), "..", "..", "templates", "pyproject.toml"
            )
        )
        shutil.copy(gitignore_location, os.getcwd())

        print("pyproject.toml file created")
