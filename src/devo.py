# --------------------------------------------------------------------------------------------------
# A development library to create code templates.
# --------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from projects.cpp_sw import Cpp_Sw
from projects.python import Python
from projects.zephyr import Zephyr

import argparse
import os
import yaml

# --------------------------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command', required=True)

    create_parser = subparser.add_parser('create')
    create_parser.add_argument('--t', required=True)

    args = parser.parse_args()

    if (args.command == 'create'):
        _create_project(args.t)

# --------------------------------------------------------------------------------------------------
def _create_project(project_type):
    """
    Creates a new project based on the type.

    Args:
        project_type: The type of project to create.
    """

    # Check if there's already a project.
    if os.path.isfile("devo.yaml"):
        print("This directory already contains a devo file.")
        return
    else:
        # Project description file:
        _create_config_file(project_type)
        proj = _get_project(project_type)
        proj.create_project()

# --------------------------------------------------------------------------------------------------
def _create_config_file(project_type):
    """
    Creates a project config file.

    Args:
        project_type: Architecture for the project.
    """

    devo_config = {
        'type': project_type
    }

    with open('devo.yaml', 'w') as devo_file:
        yaml.dump(devo_config, devo_file)

# --------------------------------------------------------------------------------------------------
def _get_project(project_type):
    """
    Returns a project object.
    """

    match project_type:
        case 'python':
            return Python()
        case 'cpp_sw':
            return Cpp_Sw()
        case 'zephyr':
            return Zephyr()

# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
