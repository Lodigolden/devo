# --------------------------------------------------------------------------------------------------
# Creates a Zephyr project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

import os
import shutil
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
        self.create_gitignore_file()
        self.create_cmake_file()
        self.create_conf_file()

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
    def create_cmake_file(self):
        """
        Creates a CMakeLists.txt file in the root directory.
        """

        super()._create_break()
        cprint("Creating CMakeLists.txt file", attrs=["bold"])

        cmake_location = os.path.abspath(os.path.join(self.file_path, "CMakeLists.txt"))
        shutil.copy(cmake_location, os.getcwd())

        print("CMakeLists.txt file created")

    # ----------------------------------------------------------------------------------------------
    def create_conf_file(self):
        """
        Creates a prj.conf file in the root directory.
        """

        super()._create_break()
        cprint("Creating prf.conf file", attrs=["bold"])

        conf_location = os.path.abspath(os.path.join(self.file_path, "prj.conf"))
        shutil.copy(conf_location, os.getcwd())

        print("prj.conf file created")
