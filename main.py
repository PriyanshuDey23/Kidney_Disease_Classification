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
