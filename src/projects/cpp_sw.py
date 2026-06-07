# --------------------------------------------------------------------------------------------------
# Creates a C++ (Software) project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

from termcolor import colored, cprint

# --------------------------------------------------------------------------------------------------
class Cpp_Sw(Project):
    # ----------------------------------------------------------------------------------------------
    def __init__(self):
        """
        The default constructor initializes the base class, and creates a C++ (software) project.
        """

        super().__init__("cpp_sw")

        super().create_break()
        cprint("Creating C++ (Software) Project", attrs=["bold"])

        super().create_directories(["build", "inc", "src", "tests"])
        super().create_files(["CMakeLists.txt", ".gitignore"])

        super().create_break()
        cprint("C++ (Software) Project Created", "green", attrs=["bold"])
        super().create_break()
