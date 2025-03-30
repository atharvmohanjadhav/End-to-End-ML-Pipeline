from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        mode_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=mode_evaluation_config)
        model_evaluation.log_mlflow()

if __name__=="__main__":
    try:
        logger.info(f"-----> stage {STAGE_NAME} started <-----")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f"-----> stage {STAGE_NAME} completed <-----")
    except Exception as e:
        logger.exception(e)
        raise e
