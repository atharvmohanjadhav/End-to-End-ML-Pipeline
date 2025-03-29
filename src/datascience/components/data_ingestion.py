from urllib import request
import zipfile
import os
from src.datascience.entity.config_entity import (DataIngestionConfig)
from src.datascience import logger
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # function for downloading zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers= request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with followig info: \n{headers}")
        else:
            logger.info(f"File already exist!")

    # function for extracting the zip file
    def extract_zip_file(self):
        """
        zipfile_path: str
        this function returns None
        
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
