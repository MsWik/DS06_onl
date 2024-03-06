from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import onnxruntime as rt
import numpy as np

app = FastAPI()
session = rt.InferenceSession('regressor.model.onnx')

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Store: float = Form(...),
    Flag: float = Form(...),
    Temperature: float = Form(...),
    Fuel_Price: float = Form(...),
    CPI: float = Form(...),
    Unemployment: float = Form(...),
    Year: float = Form(...),
):
    
    input = {
        "Store": np.array([[Store]], dtype=np.float32),
        "Holiday_Flag": np.array([[Flag]], dtype=np.float32),
        "Temperature": np.array([[Temperature]], dtype=np.float32),
        "Fuel_Price": np.array([[Fuel_Price]], dtype=np.float32),
        "CPI": np.array([[CPI]], dtype=np.float32),
        "Unemployment": np.array([[Unemployment]], dtype=np.float32),
        "Year": np.array([[Year]], dtype=np.float32)
    }
    prediction_result = session.run(None, input)[0][0][0]
    return templates.TemplateResponse("index.html", {"request": request, "prediction_result": prediction_result})