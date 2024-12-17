from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingpipeline

STAGE_NAME = 'Data Ingestion Stage'

try:

    logger.info(f"{STAGE_NAME} started")
    data_ingestion_pipeline = DataIngestionTrainingpipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e