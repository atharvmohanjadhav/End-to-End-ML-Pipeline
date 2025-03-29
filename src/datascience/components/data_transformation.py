import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        df = pd.read_csv(self.config.data_path)
        train,test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info(f"Split Data into train and test")
        logger.info(f"train data shape: {train.shape}")
        logger.info(f"test data shape: {test.shape}")

        print(train.shape)
        print(test.shape)