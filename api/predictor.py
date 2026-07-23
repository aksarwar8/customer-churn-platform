import joblib
import pandas as pd

from src.feature_engineering import engineer_features
from src.logger import logger
from config.settings import MODEL_PATH




pipeline = joblib.load(MODEL_PATH)

def predict_customer(customer_data: dict):

    logger.info("Prediction request received.")

    df = pd.DataFrame([customer_data])

    df = engineer_features(df)

    prediction = pipeline.predict(df)[0]

    probability = pipeline.predict_proba(df)[0][1]

    risk = probability * 100

    logger.info(
        f"Prediction={prediction}, Probability={risk:.2f}%"
    )

    return {
        "prediction": "Churn" if prediction else "No Churn",
        "probability": round(risk, 2),
        "risk_level":
            "High" if risk >= 70 else
            "Medium" if risk >= 40 else
            "Low"
    }