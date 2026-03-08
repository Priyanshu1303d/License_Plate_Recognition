import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")

project_name = "license_plate_recognition"

list_of_files = [

    ".env",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",

    # configs
    "configs/model_config.yaml",

    # src
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/detector/__init__.py",
    f"src/{project_name}/detector/yolo_detector.py",

    f"src/{project_name}/ocr/__init__.py",
    f"src/{project_name}/ocr/plate_reader.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/inference_pipeline.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/image_utils.py",
    f"src/{project_name}/utils/visualization.py",

    f"src/{project_name}/tests/__init__.py",
    f"src/{project_name}/tests/test_detector.py",

    "Research/.gitkeep",

    # models
    "models/.gitkeep",

    # results
    "results/predictions/.gitkeep",
    "results/metrics/.gitkeep",
    "results/visualizations/.gitkeep",

    # app
    "app/streamlit_app.py",
    "app/examples/.gitkeep",

]


def create_project_structure():
    """Create project structure"""

    created_folders = set()
    created_files = []

    for file_path_str in list_of_files:

        file_path = Path(file_path_str)
        folder = file_path.parent

        if folder != Path(".") and str(folder) not in created_folders:
            folder.mkdir(parents=True, exist_ok=True)
            created_folders.add(str(folder))
            logging.info(f"Created folder: {folder}")

        if not file_path.exists() or file_path.stat().st_size == 0:
            with open(file_path, "w") as f:
                if file_path.name == ".gitkeep":
                    f.write("# keep directory in git\n")

            created_files.append(str(file_path))
            logging.info(f"Created file: {file_path}")

    print("\n======================================")
    print(f"Folders created: {len(created_folders)}")
    print(f"Files created: {len(created_files)}")
    print("======================================")

if __name__ == "__main__":
    create_project_structure()