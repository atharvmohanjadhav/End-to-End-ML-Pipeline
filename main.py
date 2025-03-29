from src.datascience import logger
from src.datascience.pipeline.data_ingestion_1 import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_2 import DataValidationTrainingPipeline

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

