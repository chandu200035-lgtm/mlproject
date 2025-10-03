import os
import pickle
import pandas as pd
from logger import logger
from custom_exception import CustomException
import sys

def save_object(file_path, obj):
    """
    Saves a Python object to a file using pickle.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logger.info(f"Object saved successfully to {file_path}")
    except Exception as e:
        logger.error("Failed to save object", exc_info=True)
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Loads a Python object from a pickle file.
    """
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        logger.info(f"Object loaded successfully from {file_path}")
        return obj
    except Exception as e:
        logger.error("Failed to load object", exc_info=True)
        raise CustomException(e, sys)


def read_csv(file_path):
    """
    Reads a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        logger.info(f"CSV loaded: {file_path}, Shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to read CSV: {file_path}", exc_info=True)
        raise CustomException(e, sys)
