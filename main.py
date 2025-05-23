from fastapi import FastAPI
from pydantic import BaseModel
from App.model.model import predict_pipeline
from App.model.model import __version__ as model_version


app = FastAPI()

class TextIn(BaseModel):
    text:str

class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return{"health_check":"ok","model_version":model_version}

@app.post("/predict",response_model=PredictionOut)
def predict(payload:TextIn):
    language = predict_pipeline(payload.text)
    return {"language":language}

