# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from .base import Project

# --------------------------------------------------------------------------------------------------
class Python(Project):
    # ----------------------------------------------------------------------------------------------
    def __init__(self):
        """
        The default constructor initializes the base class. 
        """

        super().__init__("python")

    # ----------------------------------------------------------------------------------------------
    def create_project(self):
        """
        Passes project lists to parent method.
        """

        directories = ["src", "tests"]
        files = [".gitignore", "pyproject.toml"]

        super()._create_project(directories, files)
