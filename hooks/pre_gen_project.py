"""
Initializes a Git repository in the current directory with the main branch.
Assumes that Git is installed on the system.
"""

import os
import subprocess

# Get the current working directory
project_path = os.getcwd()

# Initialize a Git repository with the main branch
subprocess.run(['git', 'init', '-b', 'main', project_path])
