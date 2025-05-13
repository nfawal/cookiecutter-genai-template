"""
This script initializes a virtual environment using Poetry, then installs pre-commit.
It assumes that you have Python and pip installed on your system.
"""

import importlib
import subprocess

# Check if Poetry is installed
try:
    importlib.import_module('poetry')
except ImportError:
    print('Poetry is not installed. Install Poetry now.')
    subprocess.run(['pip', 'install', 'poetry'])

# Run poetry install to set up the virtual environment
subprocess.run(['poetry', 'install'])

# Run pre-commit install in the Git repository using the virtual environment
subprocess.run(['poetry', 'run', 'pre-commit', 'install'])
