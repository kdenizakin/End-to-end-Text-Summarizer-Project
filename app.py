
from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline

text = "Text Summarization Tool"

fast_api_app = FastAPI()

@fast_api_app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@fast_api_app.get("/train", tags=["authentication"])
async def index():
    try:
        os.system("py main.py")
        return Response("Trainign finished!!!")
    except Exception as e:
        print(e)
        return Response("Error!!")
    
    
@fast_api_app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predicts(text)
        return text
    except Exception as e:
        raise e
    

if __name__ ==  "__main__":
    uvicorn.run(fast_api_app, host="0.0.0.0", port=8080)
    