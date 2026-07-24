import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction Platform")
st.write("Predict whether a customer is likely to churn.")

st.divider()

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

with col2:
    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=72,
        value=12
    )

st.divider()

st.header("Service Information")

col1, col2 = st.columns(2)

with col1:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No"]
    )

with col2:
    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No"]
    )

st.divider()

st.header("Billing Information")

col1, col2 = st.columns(2)

with col1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
        max_value=118.75,
        step=0.1
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=8684.80,
        value=1000.0,
        step=1.0
    )


st.divider()

if st.button("🔍 Predict Churn", use_container_width=True):

    customer = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=customer,
            timeout=5
        )

    except requests.exceptions.ConnectionError:

        st.error("❌ Cannot connect to the prediction server.")
        st.stop()

    except requests.exceptions.Timeout:

        st.error("⏳ The prediction server took too long to respond.")
        st.stop()

    except requests.exceptions.RequestException as e:

        st.error(f"Unexpected request error: {e}")
        st.stop()
    if response.status_code == 400:

        error = response.json()

        st.error(error["detail"])

        st.stop()

    elif response.status_code != 200:

        st.error("❌ Something went wrong on the server.")

        st.stop()

    result = response.json()

    prediction = result["prediction"]
    probability = result["probability"]
    risk = result["risk_level"]

    st.divider()

    st.header("Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Prediction",
            prediction
        )

    with col2:
        st.metric(
            "Probability",
            f"{probability}%"
        )

    with col3:
        st.metric(
            "Risk Level",
            risk
        )
    if prediction == "Churn":
        st.error("🔴 Customer is likely to churn")
    else:
        st.success("🟢 Customer is likely to stay")

    if risk == "High":
        st.error("⚠️ High Risk Customer")

    elif risk == "Medium":
        st.warning("🟡 Medium Risk Customer")

    else:
        st.success("🟢 Low Risk Customer")