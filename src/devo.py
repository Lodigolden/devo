# --------------------------------------------------------------------------------------------------
# A development library to create code templates.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from projects.cpp_sw import create_cpp_project
from projects.python import create_python_project

import argparse


# --------------------------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("template", help="Enter the project type here")

    args = parser.parse_args()

    match args.template:
        case "cpp_sw":
            create_cpp_project()
        case "python":
            create_python_project()


if __name__ == "__main__":
    main()
