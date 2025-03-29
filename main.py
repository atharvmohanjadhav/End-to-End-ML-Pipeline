from src.datascience import logger
from src.datascience.pipeline.data_ingestion_1 import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_2 import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_3 import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_4 import ModelTrainerPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f"-----> stage {STAGE_NAME} started <-----")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"-----> stage {STAGE_NAME} completed <-----")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"-----> stage {STAGE_NAME} started <-----")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f"-----> stage {STAGE_NAME} completed <-----")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation Stage"
try:
    logger.info(f"-----> stage {STAGE_NAME} started <-----")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f"-----> stage {STAGE_NAME} completed <-----")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f"-----> stage {STAGE_NAME} started <-----")
    obj = DataTransformationPipeline()
    obj.initiate_data_Transformation()
    logger.info(f"-----> stage {STAGE_NAME} completed <-----")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Trainer Stage'

try:
    logger.info(f"-----> stage {STAGE_NAME} started <-----")
    obj = ModelTrainerPipeline()
    obj.initiate_model_trainer()
    logger.info(f"-----> stage {STAGE_NAME} completed <-----")
except Exception as e:
    logger.exception(e)
    raise e
