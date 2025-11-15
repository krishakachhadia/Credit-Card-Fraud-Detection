import streamlit as st
import numpy as np
import pickle
import random

# ------------------------------------------------------
# Load Model & Scaler
# ------------------------------------------------------
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ------------------------------------------------------
# Page Config
# ------------------------------------------------------
st.set_page_config(page_title="SwipeSuraksha", layout="centered")

# ------------------------------------------------------
# CYBERPUNK CSS (Glitch + RGB + Typing)
# ------------------------------------------------------
st.markdown("""
<style>

body {
    background-color: #0A0F24;
}
.css-18e3th9, .css-1d391kg {
    background-color: #0A0F24 !important;
}

/* GLITCH TEXT ANIMATION */
.glitch {
    font-family: 'Courier New';
    font-size: 55px;
    font-weight: 900;
    text-align: center;
    color: #00E4FF;
    position: relative;
    display: inline-block;
    margin: 25px auto 5px;
    text-shadow: 
        0 0 10px #00E4FF,
        0 0 20px #00E4FF,
        0 0 40px #00E4FF;
}

.glitch:before {
    content: attr(data-text);
    position: absolute;
    left: -3px;
    top: 0;
    color: #FF00E6;
    text-shadow: -2px 0 #FF00E6;
    animation: glitch-anim 2s infinite linear alternate-reverse;
}
.glitch:after {
    content: attr(data-text);
    position: absolute;
    left: 3px;
    top: 0;
    color: #00FF6A;
    text-shadow: 2px 0 #00FF6A;
    animation: glitch-anim2 2.5s infinite linear alternate-reverse;
}

@keyframes glitch-anim {
    0% { clip-path: inset(10% 0 45% 0); transform: translate(-3px,-3px); }
    20% { clip-path: inset(20% 0 40% 0); transform: translate(3px,3px); }
    40% { clip-path: inset(40% 0 20% 0); transform: translate(-3px,2px); }
    60% { clip-path: inset(60% 0 15% 0); transform: translate(2px,-3px); }
    80% { clip-path: inset(15% 0 50% 0); transform: translate(-3px,1px); }
    100% { clip-path: inset(30% 0 30% 0); transform: translate(3px,-2px); }
}

@keyframes glitch-anim2 {
    0% { clip-path: inset(5% 0 60% 0); transform: translate(3px,2px); }
    25% { clip-path: inset(30% 0 30% 0); transform: translate(-3px,-2px); }
    50% { clip-path: inset(50% 0 10% 0); transform: translate(2px,3px); }
    75% { clip-path: inset(10% 0 40% 0); transform: translate(-2px,-3px); }
    100% { clip-path: inset(40% 0 40% 0); transform: translate(3px,1px); }
}

/* Clean Neon Title Instruction */
.neon-instruction {
    font-size: 24px;
    text-align: center;
    color: #00E4FF;
    text-shadow: 0 0 15px #00E4FF;
    margin-top: 10px;
    margin-bottom: 25px;
}

/* BUTTON */
.stButton>button {
    background-color: #00E4FF;
    color: black;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
    box-shadow: 0 0 20px #00E4FF;
}
.stButton>button:hover {
    background-color: #00FF6A;
    box-shadow: 0 0 25px #00FF6A;
}

/* RESULT CARD */
.result {
    font-size: 24px;
    padding: 20px;
    border-radius: 12px;
    font-weight: 600;
    text-align: center;
    margin-top: 20px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# GLITCH TITLE
# ------------------------------------------------------
st.markdown('<div class="glitch" data-text="SwipeSuraksha">SwipeSuraksha</div>', unsafe_allow_html=True)

# ------------------------------------------------------
# CLEAN CYBERPUNK INSTRUCTION LINE
# ------------------------------------------------------
st.markdown(
    '<p class="neon-instruction">⚡ Initiate Fraud Scan — Enter Your Transaction Details Below</p>',
    unsafe_allow_html=True
)

# ------------------------------------------------------
# INPUT FIELDS
# ------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    time = st.number_input("⏱ Transaction Time", min_value=0.0, step=1.0)

with col2:
    amount = st.number_input("💰 Transaction Amount", min_value=0.0, step=0.1)

# ------------------------------------------------------
# PREDICTION
# ------------------------------------------------------
if st.button("🔍 Predict Fraud"):

    # Generate synthetic PCA features (so model can detect fraud)
    synthetic_pca = [random.uniform(-3, 3) for _ in range(28)]
    input_features = [time] + synthetic_pca + [amount]

    scaled = scaler.transform(np.array(input_features).reshape(1, -1))

    prediction = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1] * 100

    if prediction == 1:
        st.markdown(
            f'<div class="result" style="background-color:#B91C1C;">⚠ FRAUD DETECTED!<br><br>Risk Score: {prob:.2f}%</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="result" style="background-color:#14532D;">✔ LEGITIMATE TRANSACTION<br><br>Fraud Probability: {prob:.2f}%</div>',
            unsafe_allow_html=True
        )
