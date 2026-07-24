from fastapi import FastAPI
from api.schemas import CustomerData,PredictionResponse
from api.predictor import predict_customer
from api.exceptions import global_exception_handler
from config.settings import API_VERSION
from src.validation import validate_customer

from config.settings import APP_NAME, API_VERSION

app = FastAPI(
    title=APP_NAME,
    version=API_VERSION
)
app.add_exception_handler(
    Exception,
    global_exception_handler
)

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running!"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "model_loaded": True,
        "version": API_VERSION
    }
@app.get("/model-info", tags=["Model"])
def model_info():
    return {
        "model_name": "Customer Churn Prediction",
        "algorithm": "CatBoost Classifier",
        "target": "Churn",
        "version": API_VERSION,
        "developer": "Sarwar Karim",
        "status": "Production"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):

    validate_customer(customer)

    result = predict_customer(customer.model_dump())

    return result