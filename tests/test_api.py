from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200

def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"

    assert data["model_loaded"] is True


def test_model_info():
    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model_name"] == "Customer Churn Prediction"
    assert data["algorithm"] == "CatBoost Classifier"
    assert data["target"] == "Churn"
    assert data["version"] == "1.0.0"
    assert data["developer"] == "Sarwar Karim"
    assert data["status"] == "Production"


def test_predict():
    payload = {
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

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "probability" in data
    assert "risk_level" in data