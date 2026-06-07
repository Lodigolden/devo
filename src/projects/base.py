# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import os
import shutil
from termcolor import colored, cprint

# --------------------------------------------------------------------------------------------------
# Base class for project instantiation.
# --------------------------------------------------------------------------------------------------
class Project():
    # ----------------------------------------------------------------------------------------------
    def __init__(self, asset_path):
        """
        The parameterized constructor creates a file path object to the location of assets.

        Args:
            asset_path: Path to all files created during build.
        """

        self.file_path = os.path.abspath(
            os.path.join(os.path.abspath(__file__), "..", "..", "templates", asset_path)
        )

    # ----------------------------------------------------------------------------------------------
    def create_break(self):
        """
        Prints a deliminator in the console.
        """

        print(
            "----------------------------------------------------------------------------------------------------"
        )

    # ----------------------------------------------------------------------------------------------
    def create_directories(self, directories):
        """
        Creates all directories for a project.

        Args:
            directories: A list of all directories to be created.
        """

        self.create_break()
        cprint("Creating directories...", attrs=['bold'])

        for directory in directories:
            self._create_directory(directory)

        print("Directories created.")

    # ----------------------------------------------------------------------------------------------
    def create_files(self, files):
        """
        Creates all files for a project.

        Args:
            files: A list of all files to be created.
        """

        for file in files:
            self._create_file(file)

    # ----------------------------------------------------------------------------------------------
    def _create_directory(self, new_directory):
        """
        Creates a new directory.

        Args:
            new_directory: The name of the new directory.
        """

        new_directory_path = os.path.join(os.getcwd(), new_directory)

        try:
            os.mkdir(new_directory_path)
            print(
                f"Directory '{ new_directory }' created successfully at: { new_directory_path }"
            )
        except FileExistsError:
            cprint(
                f"Directory '{ new_directory }' already exists at: { new_directory_path }",
                "red",
            )
        except OSError as e:
            cprint(f"Error creating directory: { e }", "red")
    
    # ----------------------------------------------------------------------------------------------
    def _create_file(self, file_name):
        """
        Creates a new file from the templates folder.

        Args:
            file_name: The name of the file.
        """

        self.create_break()
        cprint(f"Creating { file_name } file...", attrs=['bold'])

        file_location = os.path.abspath(os.path.join(self.file_path, file_name))
        shutil.copy(file_location, os.getcwd())

        print(f"{ file_name } file created.")
