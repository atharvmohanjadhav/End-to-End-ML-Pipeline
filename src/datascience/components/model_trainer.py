import pandas as pd
import os
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config

    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        x_train = train_df.drop([self.config.target_column],axis=1)
        x_test = train_df.drop([self.config.target_column],axis=1)

        y_train = train_df[[self.config.target_column]]
        y_test = test_df[[self.config.target_column]]

        elr = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        elr.fit(x_train,y_train)

        joblib.dump(elr,os.path.join(self.config.root_dir,self.config.model_name))

