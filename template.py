#### Execute this file to automatically create all the files and folders.

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

### list of files and folders

list_of_files = [
    ### github - automatically takes the code from git for deployment, used for cicd deployment 
    ### workflows is another file
    ### gitkeep is a hidden file, will be deleted later on
    ".github/workflows/.gitkeep",
    ### __init__.py is the constructor file needed if we want to import something from another folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utlis/__init__.py",
    f"src/{project_name}/utlis/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]



for filepath in list_of_files:
    ### iterates through the list_of_files and gives each path according to the os
    """ To try - 1. Open CMD
        2. Type python - this activates the python interpreter, which is an interactive environment where you can execute Python code line by line.
        3. Type - from pathlib import Path
        4. Specify a path, say - path = "config/config.yaml"
        5. Type - Path(path)
        6. This gives output - WindowsPath('config/config.yaml'), i.e., the details of the os.
    """
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)

    ### For creating a file directory if it doesn not exist already
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        ### used to get logs on the terminal
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    ### creating filepath if it doesn't exist already or if its size is zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")

### open terminal, write os.path.getsize("README.md")