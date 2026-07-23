import pandas as pd

from api.predictor import pipeline, predict_customer


def test_model_loaded():
    assert pipeline is not None


def test_prediction_output():

    sample = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 24,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 75.5,
        "TotalCharges": 1812.0
    }

    result = predict_customer(sample)

    assert "prediction" in result
    assert "probability" in result
    assert "risk_level" in result

    assert result["prediction"] in ["Churn", "No Churn"]
    assert 0 <= result["probability"] <= 100
    assert result["risk_level"] in ["Low", "Medium", "High"]