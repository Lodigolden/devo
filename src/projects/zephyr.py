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

        super().create_break()
        cprint("Creating Zephyr Project", attrs=["bold"])

        super().create_directories(["boards", "scripts", "src"])
        super().create_files([".gitignore", "CMakeLists.txt", "prj.conf"])

        super().create_break()
        cprint("Zephyr Project Created", "green", attrs=["bold"])
        super().create_break()
