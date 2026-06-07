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

        super().create_break()
        cprint("Creating Python Project", attrs=["bold"])

        super().create_directories(["src", "tests"])
        super().create_files([".gitignore", "pyproject.toml"])

        super().create_break()
        cprint("Python Project Created", "green", attrs=["bold"])
        super().create_break()
