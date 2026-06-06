# --------------------------------------------------------------------------------------------------
# Creates a Zephyr project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

from termcolor import colored, cprint

# --------------------------------------------------------------------------------------------------
class Zephyr(Project):
    # ----------------------------------------------------------------------------------------------
    def __init__(self):
        """
        The default constructor initializes the base class, and creates a Zephyr project.
        """

        super().__init__("zephyr")

        super()._create_break()
        cprint("Creating Zephyr Project", attrs=["bold"])

        self.create_directories()
        super()._create_file(".gitignore")
        super()._create_file("CMakeLists.txt")
        super()._create_file("prj.conf")

        super()._create_break()
        cprint("Zephyr Project Created", "green", attrs=["bold"])
        super()._create_break()

    # ----------------------------------------------------------------------------------------------
    def create_directories(self):
        """
        Creates all directories for a new Zephyr project.
        """

        super()._create_break()
        cprint("Creating directories", attrs=["bold"])

        super()._create_directory("boards")
        super()._create_directory("scripts")
        super()._create_directory("src")

        print("Directories created")
