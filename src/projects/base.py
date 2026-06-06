# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import os
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
    def _create_break(self):
        """
        Prints a deliminator in the console.
        """

        print(
            "----------------------------------------------------------------------------------------------------"
        )
