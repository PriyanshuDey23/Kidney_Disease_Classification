from Kidney_Disease_Classification.constrants import * # Import Everything
from Kidney_Disease_Classification.utils.common import read_yaml,create_directories 
from Kidney_Disease_Classification.entity.config_entity import *

class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,  # Return Box Type  # Ctrl+click to check the file path
            params_filepath=PARAMS_FILE_PATH):

            self.config=read_yaml(config_filepath)
            self.params=read_yaml(params_filepath)

            # From common.py
            create_directories([self.config.artifacts_root]) # I can call using the key name using Box Type

    def get_data_ingestion_config(self) -> DataIngestionConfig: # calling Data ingest config
        config=self.config.data_ingestion  # Storing the config

        create_directories([config.root_dir]) # Check config 

        # Define the custom return type of the function, check config, storing it
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir    
        )

        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
          
          
        config=self.config.prepare_base_model

        create_directories([config.root_dir])

          

          # From config and params.yaml  
        prepare_base_model_config=PrepareBaseModelConfig(
                root_dir=Path(config.root_dir),
                base_model_path=Path(config.base_model_path),
                updated_base_model_path=Path(config.updated_base_model_path),
                params_image_size=self.params.IMAGE_SIZE,
                params_learning_rate=self.params.LEARNING_RATE,
                params_include_top=self.params.INCLUDE_TOP,
                params_weights=self.params.WEIGHTS,
                params_classes=self.params.CLASSES
            )
        return prepare_base_model_config
    