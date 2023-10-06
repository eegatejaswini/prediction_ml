import streamlit as st
from model import app.py

# Set the title and description of the app
st.title("Heart Disease Prediction")
st.write("This app predicts the probability of heart disease based on user input.")

# Input fields for user data
st.sidebar.title("User Input")
male = st.sidebar.radio("Gender:", ("Male", "Female"))
age = st.sidebar.slider("Age:", 20, 90, 40)
currentSmoker = st.sidebar.radio("Are you a current smoker?", ("Yes", "No"))
cigsPerDay = st.sidebar.slider("Cigarettes per day:", 0, 70, 0)
BPMeds = st.sidebar.radio("Are you on blood pressure medication?", ("Yes", "No"))
prevalentStroke = st.sidebar.radio("Do you have a prevalent stroke?", ("Yes", "No"))
prevalentHyp = st.sidebar.radio("Do you have prevalent hypertension?", ("Yes", "No"))
diabetes = st.sidebar.radio("Do you have diabetes?", ("Yes", "No"))
totChol = st.sidebar.slider("Total cholesterol:", 100, 600, 200)
sysBP = st.sidebar.slider("Systolic blood pressure:", 80, 250, 120)
diaBP = st.sidebar.slider("Diastolic blood pressure:", 40, 150, 80)
BMI = st.sidebar.slider("Body Mass Index (BMI):", 15.0, 45.0, 25.0)
heartRate = st.sidebar.slider("Heart rate:", 40, 200, 75)
glucose = st.sidebar.slider("Glucose level:", 40, 400, 100)

# Button to trigger the prediction
if st.sidebar.button("Predict"):
    male = 1 if male == "Male" else 0
    currentSmoker = 1 if currentSmoker == "Yes" else 0
    BPMeds = 1 if BPMeds == "Yes" else 0
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0
    TenYearCHD = 0  # Placeholder for TenYearCHD since we're predicting it

    # Call the prediction function
    prediction_result = predict_heart_disease(
        male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,
        totChol, sysBP, diaBP, BMI, heartRate, glucose, TenYearCHD
    )

    # Display the prediction result
    st.subheader("Prediction Result:")
    st.write(prediction_result)
