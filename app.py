
import streamlit as st
import joblib
import numpy as np

model = joblib.load("loan_model.pkl")

st.title("Loan Approval Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])

income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")

credit_history = st.selectbox(
    "Credit History",
    [0, 1]
)

gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 0 if education == "Graduate" else 1

if st.button("Predict"):

    features = np.array([[
        gender,
        married,
        education,
        income,
        loan_amount,
        credit_history
    ]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
