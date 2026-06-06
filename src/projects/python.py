# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

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
        super()._create_file(".gitignore")
        super()._create_file("pyproject.toml")

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
