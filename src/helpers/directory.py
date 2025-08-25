# --------------------------------------------------------------------------------------------------
# Utilities for creating and managing directories.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
import os
from termcolor import colored, cprint


# --------------------------------------------------------------------------------------------------
def create_directory(new_directory):
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
