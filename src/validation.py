from fastapi import HTTPException

# Numeric Limits

MONTHLY_CHARGES_MIN = 18.25
MONTHLY_CHARGES_MAX = 118.75

TENURE_MIN = 0
TENURE_MAX = 72

TOTAL_CHARGES_MIN = 0.0
TOTAL_CHARGES_MAX = 8684.80

# Allowed Categories

GENDER = ["Male", "Female"]

YES_NO = ["Yes", "No"]

PHONE_SERVICE = ["Yes", "No"]

MULTIPLE_LINES = [
    "Yes",
    "No",
    "No phone service"
]

INTERNET_SERVICE = [
    "DSL",
    "Fiber optic",
    "No"
]

ONLINE_SERVICE = [
    "Yes",
    "No",
    "No internet service"
]

CONTRACT = [
    "Month-to-month",
    "One year",
    "Two year"
]

PAPERLESS_BILLING = [
    "Yes",
    "No"
]

PAYMENT_METHOD = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
]


def validate_monthly_charges(value):
    if value < MONTHLY_CHARGES_MIN or value > MONTHLY_CHARGES_MAX:
        raise HTTPException(
            status_code=400,
            detail=f"MonthlyCharges must be between {MONTHLY_CHARGES_MIN} and {MONTHLY_CHARGES_MAX}."
        )

def validate_tenure(value):
    if value < TENURE_MIN or value > TENURE_MAX:
        raise HTTPException(
            status_code=400,
            detail=f"Tenure must be between {TENURE_MIN} and {TENURE_MAX}."
        )

def validate_total_charges(value):
    if value < TOTAL_CHARGES_MIN or value > TOTAL_CHARGES_MAX:
        raise HTTPException(
            status_code=400,
            detail=f"TotalCharges must be between {TOTAL_CHARGES_MIN} and {TOTAL_CHARGES_MAX}."
        )

def validate_category(value, allowed_values, field_name):
    if value not in allowed_values:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Invalid value '{value}' for {field_name}. "
                f"Allowed values are: {allowed_values}"
            )
        )

def validate_customer(customer):
    validate_monthly_charges(customer.MonthlyCharges)
    validate_total_charges(customer.TotalCharges)
    validate_tenure(customer.tenure)

    validate_category(customer.gender, GENDER, "Gender")

    validate_category(customer.Partner, YES_NO, "Partner")

    validate_category(customer.Dependents, YES_NO, "Dependents")

    validate_category(customer.PhoneService, PHONE_SERVICE, "PhoneService")

    validate_category(customer.MultipleLines, MULTIPLE_LINES, "MultipleLines")

    validate_category(customer.InternetService, INTERNET_SERVICE, "InternetService")

    validate_category(customer.OnlineSecurity, ONLINE_SERVICE, "OnlineSecurity")

    validate_category(customer.OnlineBackup, ONLINE_SERVICE, "OnlineBackup")

    validate_category(customer.DeviceProtection, ONLINE_SERVICE, "DeviceProtection")

    validate_category(customer.TechSupport, ONLINE_SERVICE, "TechSupport")

    validate_category(customer.StreamingTV, ONLINE_SERVICE, "StreamingTV")

    validate_category(customer.StreamingMovies, ONLINE_SERVICE, "StreamingMovies")

    validate_category(customer.Contract, CONTRACT, "Contract")

    validate_category(customer.PaperlessBilling, PAPERLESS_BILLING, "PaperlessBilling")

    validate_category(customer.PaymentMethod, PAYMENT_METHOD, "PaymentMethod")