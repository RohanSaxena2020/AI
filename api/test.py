import os

print("Connection String from ENV:", os.getenv("AZURE_STORAGE_CONNECTION_STRING"))

# Proceed with your other imports and setup...
from fastapi import FastAPI, File, UploadFile
# Your other code...

