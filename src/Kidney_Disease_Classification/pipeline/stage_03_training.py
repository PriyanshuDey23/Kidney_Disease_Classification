from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification.components.prepare_callbacks import PrepareCallbacks
from Kidney_Disease_Classification.components.training import Training
from Kidney_Disease_Classification import logger


STAGE_NAME= "Training Stage"

class ModelTrainingPipeline:
    def __init__(self):  # initializing empty constructor
        pass

    def main(self):
        config=ConfigurationManager()    
        PrepareCallbacksConfig=config.get_prepare_callback_config()
        prepare_callbacks=PrepareCallbacks(config=PrepareCallbacksConfig)
        callback_list=prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callbacks_list=callback_list
        )


# For integrating DVC we will use in this way
if __name__ =='__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj=ModelTrainingPipeline()  # Calling the class
        obj.main()                           # Calling the main method
        logger.info(f" Stage {STAGE_NAME} Completed")

    except Exception as e:
        logger.exception(e)
        raise e

# call the pipeline in main.py