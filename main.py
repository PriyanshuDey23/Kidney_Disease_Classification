from src.Kidney_Disease_Classification import logger

from Kidney_Disease_Classification import logger

# Call the pipeline  (src\Kidney_Disease_Classification\pipeline\stage_01_data_ingestion.py) in main .py 

from Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj=DataIngestionTrainingPipeline()  # Calling the class
    obj.main()                           # Calling the main method,Start the data ingestion part
    logger.info(f" Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

# After executing , Artifacts folder , zip file download , unzip of the file will happen


# src\Kidney_Disease_Classification\pipeline\stage_02_prepare_base_model.py

from Kidney_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Prepare Base Model Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj=PrepareBaseModelTrainingPipeline()  # Calling the class
    obj.main()                           # Calling the main method,Start the data ingestion part
    logger.info(f" Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e


# After executing we will  get artifacts\prepare_base_model


# src\Kidney_Disease_Classification\pipeline\stage_03_training.py

# from Kidney_Disease_Classification.pipeline.stage_03_training import ModelTrainingPipeline

# STAGE_NAME="Training Stage"
# try:
#     logger.info(f"Stage {STAGE_NAME} Started")
#     obj=ModelTrainingPipeline()  # Calling the class
#     obj.main()                           # Calling the main method,Start the data ingestion part
#     logger.info(f" Stage {STAGE_NAME} Completed")

# except Exception as e:
#     logger.exception(e)
#     raise e


# After executing we will  artifacts\training



#  src\Kidney_Disease_Classification\pipeline\stage_04_evaluation.py

from Kidney_Disease_Classification.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME="Evaluation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj=EvaluationPipeline()  # Calling the class
    obj.main()                           # Calling the main method,Start the data ingestion part
    logger.info(f" Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e

# After executing scores.json created
