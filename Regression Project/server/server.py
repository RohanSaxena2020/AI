from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
from util import load_model, predict_scoring_average

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model()

class PredictionInput(BaseModel):
    sg_ott: float
    sg_app: float
    sg_atg: float
    sg_putting: float

@app.post("/predict/")
async def predict(input_data: PredictionInput):
    try:
        result = predict_scoring_average(model, input_data.dict())
        return {"scoring_average": result}
    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
