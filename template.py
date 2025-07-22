import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "C:\\RT\\MLPROJECT\\ADF_DATABRICKS"


# List of files & folders to create
list_of_files = [
    f"{project_name}/data/raw/.gitkeep",                     # local CSVs folder
    f"{project_name}/notebooks/transform.ipynb",             # Databricks notebook(s)
    f"{project_name}/pipelines/adf_pipeline.json",           # exported pipeline JSON
    f"{project_name}/scripts/upload_to_adls.py",             # Python script to upload data
    f"{project_name}/diagrams/architecture.png",             # architecture diagram
    f"{project_name}/README.md",                             # project readme
    f"{project_name}/requirements.txt"                       # python requirements
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"✅ Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create empty file
        logging.info(f"📝 Created empty file: {filepath}")

    else:
        logging.info(f"⚠️ File already exists: {filepath}")
        