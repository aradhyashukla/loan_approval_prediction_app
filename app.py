import streamlit as st
st.write("NEW VERSION LOADED")
import pandas as pd
import joblib

# Load Model
try:
     model = joblib.load("loan_model.pkl")
     st.write("Model loaded") 
     st.write(model.feature_names_in_)
except Exception as e:
     st.error(f"Error loading model: {e}")  

st.title("🏦 Loan Approval Prediction System")

st.write("Enter applicant details below:")

# Input Fields
age = st.number_input("Age", min_value=18, max_value=100, value=25)

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

education = st.selectbox(
    "Education",
    ["High School", "Bachelor", "Master", "Doctorate"]
)

person_income = st.number_input(
    "Person Income",
    min_value=0
)

employee_experience = st.number_input(
    "Employee Experience",
    min_value=0
)

home_ownership = st.selectbox(
    "Home Ownership",
    ["RENT", "OWN", "MORTGAGE"]
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_intent = st.selectbox(
    "Loan Intent",
    ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
)

loan_interest_rate = st.number_input(
    "Loan Interest Rate",
    min_value=0.0
)

loan_percentage = st.number_input(
    "Loan Percentage",
    min_value=0.0
)

credit_history = st.number_input(
    "Credit History",
    min_value=0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0
)

previous_loan = st.number_input(
    "Previous Loan",
    min_value=0
)

# Prediction Button
if st.button("Predict Loan Status"):

    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education': [education],
        'Person Income': [person_income],
        'Employee Experience': [employee_experience],
        'Home Onwership': [home_ownership],
        'Loan Amount': [loan_amount],
        'Loan Intent': [loan_intent],
        'Loan interest Rate': [loan_interest_rate],
        'Loan percentage': [loan_percentage],
        'Credit History': [credit_history],
        'Credit Score': [credit_score],
        'Previous Loan': [previous_loan]
    })

    # Gender Encoding
    input_data['Gender'] = input_data['Gender'].map({
        'male': 1,
        'female': 0
    })

    # Education Encoding
    input_data['Education'] = input_data['Education'].map({
        'High School': 0,
        'Bachelor': 1,
        'Master': 2,
        'Doctorate': 3
    })

    # Home Ownership Encoding
    input_data['Home Onwership'] = input_data['Home Onwership'].map({
        'RENT': 0,
        'OWN': 1,
        'MORTGAGE': 2
    })

    # Loan Intent Encoding
    input_data['Loan Intent'] = input_data['Loan Intent'].map({
        'PERSONAL': 0,
        'EDUCATION': 1,
        'MEDICAL': 2,
        'VENTURE': 3,
        'HOMEIMPROVEMENT': 4,
        'DEBTCONSOLIDATION': 5
    })

    st.write(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
