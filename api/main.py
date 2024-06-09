from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from azureml.core import Workspace, Model
import os

# pip install azureml-core
# pip install azure-storage-blob azure-ai-ml

app = FastAPI()

# Setup CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Class names
CLASS_NAMES = ['Bacterial Spot',
 'Early Blight',
 'Late Blight',
 'Leaf Mold',
 'Septoria Leaf Spot',
 'Two Spotted Spider Mites',
 'Target Spot',
 'YellowLeaf Curl Virus',
 'Mosaic Virus',
 'Healthy']

# Load the workspace from the saved config file
def get_workspace():
    ws = Workspace.from_config()  # Ensure you have the config.json file in your project or specify path
    return ws

# Load model from Azure Machine Learning
def load_model_from_aml(workspace, model_name):
    model = Model(workspace, model_name)
    model_path = model.download(exist_ok=True)
    return tf.keras.models.load_model(model_path)

# Instantiate workspace and load model
workspace = get_workspace()
MODEL = load_model_from_aml(workspace, 'Rohan_Tomato_Classification_Model')

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    
    predictions = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)