import streamlit as st
import pickle
import numpy as np

# Load model
with open("model/model.pkl") as f:
    model = pickle.load(f)

st.title("Real-Time Credit Card Fraud Detection")
st.write("Enter transaction details to test the model")

# Example features (change according to your dataset)
amount = st.number_input("Transaction Amount", min_value=0.0, step=0.1)
oldbalanceOrg = st.number_input("Old Balance (Origin)")
newbalanceOrig = st.number_input("New Balance (Origin)")
oldbalanceDest = st.number_input("Old Balance (Destination)")
newbalanceDest = st.number_input("New Balance (Destination)")

if st.button("Predict"):
    features = np.array([[amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠ Fraud Detected!")
    else:
        st.success("✔ Transaction is Legitimate")
