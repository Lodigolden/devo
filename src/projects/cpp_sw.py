# --------------------------------------------------------------------------------------------------
# Creates a C++ (Software) project.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

import os
import shutil
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
        self.create_cmake_file()
        self.create_gitignore_file()

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
    def create_gitignore_file(self):
        """
        Creates a .gitignore file in the root directory.
        """

        super()._create_break()
        cprint("Creating .gitignore file", attrs=["bold"])

        gitignore_location = os.path.abspath(os.path.join(self.file_path, ".gitignore"))
        shutil.copy(gitignore_location, os.getcwd())

        print(".gitignore file created")
