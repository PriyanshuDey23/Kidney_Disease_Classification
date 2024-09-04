import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os

class PredictPipeline:
    def __init__(self,filename):
        self.filename=filename  # It will take the image from browser and it will do the prediction on top of it

    def predict(self):
        # Load model
        model=load_model(os.path.join("artifacts","training","model.h5")) 

        imagename=self.filename  # Load the file that we wll be uploading
        test_image=image.load_img(imagename,target_size=(224,224)) # output size
        test_image=image.img_to_array(test_image)   # Convert to numpy array
        test_image=np.expand_dims(test_image,axis=0) # Expand the shape of an array.
        result=np.argmax(model.predict(test_image),axis=1)  # Returns the indices of the maximum values along an axis.
        print(result) # Predicted result

        if result[0] == 1:
            prediction="Tumor"
            return [{"image":prediction}]
        else:
            prediction="Normal"
            return [{"image" : prediction}]