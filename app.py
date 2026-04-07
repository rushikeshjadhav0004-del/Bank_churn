import streamlit as st
import pandas as pd
import pickle
import joblib

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="💳",
    layout="centered"
)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("best_model.pkl")
# -------------------------------
# TITLE SECTION
# -------------------------------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
        💳 Customer Churn Prediction App
    </h1>
    <p style='text-align: center; color: gray;'>
        Predict whether a customer will leave the bank or stay
    </p>
    <hr>
""", unsafe_allow_html=True)

# -------------------------------
# INPUT UI
# -------------------------------
st.sidebar.header("📌 Enter Customer Details")

credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)
age = st.sidebar.slider("Age", 18, 100, 35)
tenure = st.sidebar.slider("Tenure (Years)", 0, 10, 5)
balance = st.sidebar.number_input("Account Balance", 0.0, 250000.0, 50000.0, step=1000.0)
num_products = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
has_card = st.sidebar.selectbox("Has Credit Card?", [0, 1])
is_active = st.sidebar.selectbox("Is Active Member?", [0, 1])
salary = st.sidebar.number_input("Estimated Salary", 0.0, 200000.0, 60000.0, step=1000.0)

# -------------------------------
# PREDICTION BUTTON
# -------------------------------
if st.button("🚀 Predict Churn"):
    
    input_data = pd.DataFrame([[
        credit_score,
        age,
        tenure,
        balance,
        num_products,
        has_card,
        is_active,
        salary
    ]], columns=[
        'CreditScore', 'Age', 'Tenure', 'Balance',
        'NumOfProducts', 'HasCrCard', 'IsActiveMember',
        'EstimatedSalary'
    ])

    prediction = model.predict(input_data)[0]

    prob = model.predict_proba(input_data)[0][1]

    # -------------------------------
    # RESULT DISPLAY
    # -------------------------------
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ Customer will CHURN")
    else:
        st.success(f"✅ Customer will STAY")

    st.metric(label="Churn Probability", value=f"{prob:.2%}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
