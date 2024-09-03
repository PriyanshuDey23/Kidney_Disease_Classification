from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification.components.prepare_base_model import prepareBaseModel
from Kidney_Disease_Classification import logger

STAGE_NAME= "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline():
    def __init__(self):  # initializing empty constructor
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model=prepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=PrepareBaseModelTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e
    
# call the pipeline in main.py