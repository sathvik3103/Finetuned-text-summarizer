from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingpipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingpipeline

STAGE_NAME = 'Data Ingestion Stage'

try:

    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionTrainingpipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation Stage'

try:

    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataTransformationTrainingpipeline()
    data_ingestion_pipeline.initiate_data_trasnformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e