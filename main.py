from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingpipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingpipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingpipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationTrainingpipeline
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
    data_transformation_pipeline = DataTransformationTrainingpipeline()
    data_transformation_pipeline.initiate_data_trasnformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training Stage'

try:

    logger.info(f"{STAGE_NAME} started")
    model_trainer_pipeline = ModelTrainerTrainingpipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'

try:

    logger.info(f"{STAGE_NAME} started")
    model_evaluation_pipeline = ModelEvaluationTrainingpipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
