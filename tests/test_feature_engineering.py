import pandas as pd

from src.feature_engineering import engineer_features


def create_sample_df():
    return pd.DataFrame([{
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 24,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "Yes",
        "StreamingTV": "Yes",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 80.0,
        "TotalCharges": 1920.0
    }])


def test_engineered_columns_created():
    df = create_sample_df()

    engineered = engineer_features(df)

    expected_columns = [
        "AvgMonthlySpend",
        "TotalServices",
        "HasFamily",
        "TenureGroup",
        "SpendingGroup"
    ]

    for col in expected_columns:
        assert col in engineered.columns


def test_avg_monthly_spend():
    df = create_sample_df()

    engineered = engineer_features(df)

    assert engineered.loc[0, "AvgMonthlySpend"] == 80.0


def test_total_services():
    df = create_sample_df()

    engineered = engineer_features(df)

    assert engineered.loc[0, "TotalServices"] == 5


def test_has_family():
    df = create_sample_df()

    engineered = engineer_features(df)

    assert engineered.loc[0, "HasFamily"] == 1


def test_tenure_group():
    df = create_sample_df()

    engineered = engineer_features(df)

    assert str(engineered.loc[0, "TenureGroup"]) == "Growing"


def test_spending_group():
    df = create_sample_df()

    engineered = engineer_features(df)

    assert str(engineered.loc[0, "SpendingGroup"]) == "Medium"


def test_zero_tenure():
    df = create_sample_df()

    df.loc[0, "tenure"] = 0
    df.loc[0, "TotalCharges"] = 0

    engineered = engineer_features(df)

    assert engineered.loc[0, "AvgMonthlySpend"] == 0