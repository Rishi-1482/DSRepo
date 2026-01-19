import os
import yaml
from src.datascience_project import logger
import json
import joblib
from ensure import ensure_annotations
from box.config_box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        ValueError: If the yaml file is empty
        e: Empty file error
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("The yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """Creates directories given in the list

    Args:
        path_to_directories (list[Path]): List of directory paths to create
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory at: {path}")