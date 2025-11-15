import streamlit as st
import numpy as np
import pickle

# ------------------------------
# Load Model + Scaler
# ------------------------------
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("Credit Card Fraud Detection")
st.write("Enter details to predict if the transaction is fraudulent")

# User Inputs
time = st.number_input("Transaction Time (seconds)", min_value=0.0, step=1.0)
amount = st.number_input("Transaction Amount", min_value=0.0, step=0.1)

# ------------------------------
# Make Prediction
# ------------------------------
if st.button("Predict"):
    
    # Create a feature array of 30 values
    # Order: Time, V1–V28, Amount
    input_features = [time] + [0]*28 + [amount]  # Auto fill V1–V28 as zeros

    # Convert to 2D array for model
    input_array = np.array(input_features).reshape(1, -1)

    # Scale using the saved scaler
    scaled_input = scaler.transform(input_array)

    # Predict
    prediction = model.predict(scaled_input)[0]

    # Output
    if prediction == 1:
        st.error("⚠ Fraud Detected!")
    else:
        st.success("✔ Legitimate Transaction")

