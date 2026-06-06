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

        super()._create_break()
        cprint("Creating C++ (Software) Project", attrs=["bold"])

        self.create_directories()
        super()._create_file("CMakeLists.txt")
        super()._create_file(".gitignore")

        super()._create_break()
        cprint("C++ (Software) Project Created", "green", attrs=["bold"])
        super()._create_break()

    # ----------------------------------------------------------------------------------------------
    def create_directories(self):
        """
        Creates all directories for a new C++ (SW) project.
        """

        super()._create_break()
        cprint("Creating directories", attrs=["bold"])

        super()._create_directory("build")
        super()._create_directory("inc")
        super()._create_directory("src")
        super()._create_directory("tests")

        print("Directories created")
