import os
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import pandas as pd
from pathlib import Path
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import read_yaml,create_dirs,save_json
import os
# os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/atharvmohanjadhav/DS-Project.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"] = "atharvmohanjadhav"
# os.environ["MLFLOW_TRACKING_PASSWORD"] = "4a58f038508d5a342bdb03ad3effba338e994414"

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2

    def log_mlflow(self):
        test_df = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_df.drop([self.config.target_column],axis=1)
        y_test = test_df[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            y_pred = model.predict(x_test)

            (rmse,mae,r2) = self.eval_metrics(y_test,y_pred)
            scores = {"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metrics_file_path),data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)

            if tracking_uri_type != "file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model,"model")


