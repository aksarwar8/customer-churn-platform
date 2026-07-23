import pandas as pd


def engineer_features(df):
    # Average monthly spend
    df["AvgMonthlySpend"] = (
        df["TotalCharges"] / df["tenure"].replace(0, 1)
    )

    # Count subscribed services
    service_columns = [
        "PhoneService",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]

    df["TotalServices"] = (
        df[service_columns]
        .eq("Yes")
        .sum(axis=1)
    )

    # Family feature
    df["HasFamily"] = (
        (df["Partner"] == "Yes") &
        (df["Dependents"] == "Yes")
    ).astype(int)

    # Tenure group
    df["TenureGroup"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["New", "Growing", "Established", "Loyal"],
        include_lowest=True
    )

    # Spending group (fixed training boundaries)
    df["SpendingGroup"] = pd.cut(
        df["MonthlyCharges"],
        bins=[18.25, 50.40, 84.00, 118.75],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    return df