# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

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

        super().__init__("python")

        super()._create_break()
        cprint("Creating Python Project", attrs=["bold"])

        self.create_directories()
        self.create_gitignore_file()
        self.create_pytoml_file()

        super()._create_break()
        cprint("Python Project Created", "green", attrs=["bold"])
        super()._create_break()

    # ----------------------------------------------------------------------------------------------
    def create_directories(self):
        """
        Creates all directories for a new Python project.
        """

        super()._create_break()
        cprint("Creating directories")

        super()._create_directory("src")
        super()._create_directory("tests")

        print("Directories created")

    # ----------------------------------------------------------------------------------------------
    def create_gitignore_file(self):
        """
        Creates a .gitignore file in the root directory.
        """

        super()._create_break()
        cprint("Creating .gitignore file", attrs=["bold"])

        gitignore_location = os.path.abspath(os.path.join(self.file_path, ".gitignore"))
        shutil.copy(gitignore_location, os.getcwd())

        print(".gitignore file created")

    # ----------------------------------------------------------------------------------------------
    def create_pytoml_file(self):
        """
        Creates a pyproject.toml file in the root directory.
        """

        super()._create_break()
        cprint("Creating pyproject.toml file", attrs=["bold"])

        pytoml_location = os.path.abspath(os.path.join(self.file_path, "pyproject.toml"))
        shutil.copy(pytoml_location, os.getcwd())

        print("pyproject.toml file created")
