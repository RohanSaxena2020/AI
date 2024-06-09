# run this -> pip install azure-storage-blob azure-ai-ml

from azure.storage.blob import BlobServiceClient, BlobClient
import tensorflow as tf
from PIL import Image
import numpy as np

model = None
class_names = [
    'Bacterial Spot',
    'Early Blight',
    'Late Blight',
    'Leaf Mold',
    'Septoria Leaf Spot',
    'Two Spotted Spider Mites',
    'Target Spot',
    'YellowLeaf Curl Virus',
    'Mosaic Virus',
    'Healthy'
]

CONNECTION_STRING = "your_connection_string_here" # Azure Storage account connection string
CONTAINER_NAME = "your_container_name" # Azure blob container name
MODEL_BLOB_NAME = "models/tomatoes.h5"

def download_model(model_blob_name, destination_file_path):
    """Download the model file from Azure Blob Storage."""
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=model_blob_name)
    
    try:
        with open(destination_file_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
            print(f"Model {model_blob_name} downloaded to {destination_file_path}.")
    except Exception as e:
        print(f"Failed to download model due to: {e}")

def predict(request):
    global model
    if model is None:
        download_model(
            MODEL_BLOB_NAME,
            "/tmp/tomatoes.h5",
        )
        model = tf.keras.models.load_model("/tmp/tomatoes.h5")

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256))  # image resizing
    )

    image = image / 255  # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:", predictions)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}
