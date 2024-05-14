# server.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import util
import os
import logging

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, '..', 'UI')
app.mount("/static", StaticFiles(directory=UI_DIR), name="static")

@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse(os.path.join(UI_DIR, 'app.html'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/classify_image/")
async def classify_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        if not contents:
            logging.error("No file content received")
            raise HTTPException(status_code=400, detail="No file content received")

        image_data = util.get_cv2_image_from_base64_string(contents)
        if image_data is None:
            logging.error("Failed to convert image data")
            raise HTTPException(status_code=400, detail="Failed to convert image data")

        results = util.classify_image(image_base64_data=contents, file_path=None)
        return {"results": results}
    except Exception as e:
        logging.exception("Unexpected error occurred")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    util.load_saved_artifacts()
    print("Serving from:", UI_DIR)
    uvicorn.run(app, host="127.0.0.1", port=8000)
