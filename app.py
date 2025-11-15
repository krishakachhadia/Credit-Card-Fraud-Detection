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
# Cyberpunk CSS (Glitch + RGB + Terminal + Typing)
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
    animation: glitch-anim2 3s infinite linear alternate-reverse;
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

/* TYPING EFFECT */
.typing-text {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #00E4FF;
    font-size: 22px;
    color: #00E4FF;
    margin-bottom: 12px;
    text-shadow: 0 0 10px #00E4FF;
    animation: typing 4s steps(40), blink .8s step-end infinite alternate;
}
@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}
@keyframes blink {
    50% { border-color: transparent }
}

/* CYBER TERMINAL BOX */
.terminal-box {
    background: rgba(10, 20, 40, 0.85);
    border: 2px solid #00E4FF;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 25px;
    font-family: 'Courier New';
    color: #00FF9C;
    font-size: 17px;
    height: 140px;
    overflow: hidden;
    box-shadow: 0 0 15px #00E4FF;
    animation: glowPulse 2s infinite alternate;
}
@keyframes glowPulse {
    0% { box-shadow: 0 0 10px #00E4FF; }
    100% { box-shadow: 0 0 25px #00FF6A; }
}
.terminal-line {
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid #00FF9C;
    animation: typingTerminal 4s steps(60), blinkCursor .75s step-end infinite alternate;
}
@keyframes typingTerminal {
    from { width: 0 }
    to { width: 100% }
}
@keyframes blinkCursor {
    50% { border-color: transparent }
}

/* NEON INPUT BOX BORDER */
.neon-box {
    border: 3px solid;
    border-radius: 12px;
    padding: 20px;
    animation: rgbGlow 4s infinite;
}
@keyframes rgbGlow {
    0% { border-color: #00E4FF; }
    25% { border-color: #00FF6A; }
    50% { border-color: #FF00E6; }
    75% { border-color: #FFE600; }
    100% { border-color: #00E4FF; }
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
# CYBER TERMINAL ANIMATION BOX
# ------------------------------------------------------
st.markdown("""
<div class="terminal-box">
    <div class="terminal-line">
        Initializing SwipeSuraksha Cyber Terminal...  
        Running Fraud Pattern Recognition Engine...  
        Loading Transaction Intelligence Modules...  
        System Ready: Enter Transaction Details Below.
    </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# INPUT SECTION (Neon Border)
# ------------------------------------------------------
st.markdown('<div class="neon-box">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    time = st.number_input("⏱ Transaction Time", min_value=0.0, step=1.0)
with col2:
    amount = st.number_input("💰 Transaction Amount", min_value=0.0, step=0.1)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------------
# PREDICTION
# ------------------------------------------------------
if st.button("🔍 Predict Fraud"):

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
