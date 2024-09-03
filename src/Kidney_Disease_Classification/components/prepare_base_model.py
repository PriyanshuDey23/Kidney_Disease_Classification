import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf # For calling the vgg 16 from keras
from Kidney_Disease_Classification.config.configuration import PrepareBaseModelConfig
from pathlib import Path

class prepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config=config

    # First Method(VGG16)
    def get_base_model(self):
        self.model=tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        self.save_model(path=self.config.base_model_path,model=self.model) # Save the model


    # Second Method(Update Model)
    @staticmethod #Not adding inside my class method # Similar to python class, it is bound to a class rather than a object, I can use it from any point
    def prepare_full_model(model,classes,freeze_all,freeze_till,learning_rate):
        if freeze_all:  # Freezing all the layers as we will use pretrained model , will not train it
            for layer in model.layers:
                model.trainable=False
        elif (freeze_till is not None) and (freeze_till > 0): # No of Layer I want to freeze
            for layer in model.layers[:-freeze_till]:  # Freeze till that point
                model.trainable=False
        
        flatten_in=tf.keras.layers.Flatten()(model.output)
        prediction=tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)   

        full_model=tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        ) 

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    
    # Update the Base model with full model parameters
    def update_base_model(self): # It will take the WGG 16 model and update model and save it
        self.full_model=self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path,model=self.full_model)

    @staticmethod  # Save the model
    def save_model(path:Path,model:tf.keras.Model):
        model.save(path)
    