import os
from pathlib import Path
import logging

# List of files to be created for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.ipynb",
    "src/logger/logging.py",
    "src/exception/exception.py"
]

# Iterate through each file path in the list
for file_path in list_of_files:
    file_path = Path(file_path)  # Convert to Path object for compatibility
    file_dir, file_name = os.path.split(file_path)  # Split into directory and file name

    # Create the directory if it doesn't exist
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass  # Create an empty file
