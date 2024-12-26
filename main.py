from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
STAGE_NAME="Data ingestion stage"

logger.info("welcome to our custom logging data science")

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion=DataValidationTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except  Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME="Data transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    data_transformation=DataValidationTrainingPipeline()
    data_transformation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e