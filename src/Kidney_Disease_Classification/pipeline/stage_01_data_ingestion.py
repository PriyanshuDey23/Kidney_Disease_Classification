from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification.components.data_ingestion import DataIngestion
from Kidney_Disease_Classification import logger


STAGE_NAME= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):  # initializing empty constructor
        pass


    def main(self):
        config=ConfigurationManager()
        data_ingestin_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestin_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=DataIngestionTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py