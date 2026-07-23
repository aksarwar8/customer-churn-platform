from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Model configuration
MODEL_PATH = BASE_DIR / "models" / "catboost_pipeline.pkl"

# Logging configuration
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "api.log"

# API configuration
APP_NAME = "Customer Churn Prediction API"
API_VERSION = "1.0.0"

# Risk level thresholds
HIGH_RISK_THRESHOLD = 70
MEDIUM_RISK_THRESHOLD = 40