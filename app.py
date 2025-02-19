# POST - Creating and adding data
# Get - Reading and retriving data
from flask import Flask,request,jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from Kidney_Disease_Classification.utils.common import decodeImage
from Kidney_Disease_Classification.pipeline.predict import PredictPipeline
import ast

# initialize the flask

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)
CORS(app)

# What ever input i will pass, It will save as  jpg format

class ClientApp:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier=PredictPipeline(self.filename)

@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template('index.html')



@app.route("/train",methods=["GET","POST"])
@cross_origin()
def trainRoute():
    os.system("Python main.py") # We can also use DVC repro 
    #os.system("dvc repro")
    return "Training done Successfully!"




@app.route("/predict",methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json['image'] # Take image from webapp
    decodeImage(image, clApp.filename) # Decoding
    result = clApp.classifier.predict()  # Predict from predict.py
    # Convert the string representation of the list into an actual Python list
    result_str = str(result)  # This is your string like "[{'image': 'Coccidiosis'}]"
    
    try:
        result_list = ast.literal_eval(result_str)  # Safely convert the string to a list
        if isinstance(result_list, list) and len(result_list) > 0:
            prediction = result_list[0].get('image', None)  # Extract the value of "image"
            if prediction:
                return f"The Kidney is {prediction}"  # Return only the value (e.g., "Coccidiosis")
            else:
                return "Prediction not available"
        else:
            return "Invalid result format"
    except (ValueError, SyntaxError):
        return "Error processing result"




if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0',port=8080,debug=True)