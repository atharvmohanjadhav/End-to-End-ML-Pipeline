import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

"""
- ConfigBox is used to read the key from dict. e.g dict.key
- @ensure_annotations is used to take strict input in as it is format

"""
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read yaml file and returns
    Args--> path_to_yaml (str): path like input
    return--> ConfigBox type
    Raises--> 
        valuerror if yaml file empty
        e : empty file 

    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file} loaded succesfully!")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dirs(path_to_dirs:list,verbose=True):
    """
    create list of directories
    Args--> 
        path to dirs(list): list of path of directories
        ignore_log(bool,optional): ignore if multiple dirs is to be created.

    """
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path,data: dict):
    """
    save json data
    Args--> 
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path,"w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path) ->ConfigBox:
    """
    load the json file
    Args--> path (Path): path to json file
    return--> ConfigBox: data as as class attribute instead of dict

    """
    with open(path) as f:
        content=json.load(f)

    logger.info(f"json file loaded succefully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any,path:Path):
    """
    save binary file
    Args-->
    data(Any) : data to be saved as bianry
    path (Path): path to binary file

    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Args--> path (Path): path to binary file
    return--> Any: object stored in the file

    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data


    
