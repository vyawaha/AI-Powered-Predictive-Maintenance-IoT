import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Predictive Maintenance AI", layout="wide")

st.title("⚙️ AI Predictive Maintenance System (IoT Simulation)")
st.markdown("Industrial-level dashboard for machine failure prediction")

# ===============================
# LOAD MODEL
# ===============================
@st.cache_resource
def load_model():
    try:
        return joblib.load("models/predictive_maintenance_model.pkl")
    except:
        return None

model = load_model()

# ===============================
# OUTPUT FILE PATH
# ===============================
output_file = "outputs/predictions.csv"

if not os.path.exists("outputs"):
    os.makedirs("outputs")

if not os.path.exists(output_file):
    pd.DataFrame(columns=["temperature", "vibration", "current", "pressure", "rpm", "prediction"]).to_csv(output_file, index=False)

# ===============================
# SENSOR SIMULATION
# ===============================
def generate_sensor_data():
    temperature = np.random.normal(70, 5)
    vibration = np.random.normal(3, 1)
    current = np.random.normal(8, 2)
    pressure = np.random.normal(2 ,0.5)
    rpm = np.random.normal(4, 8)
    return temperature, vibration, current, pressure, rpm

# ===============================
# PREDICTION
# ===============================
def predict(temp, vib, curr,pre,rpm):
    if model:
        result = model.predict([[temp, vib, curr, pre, rpm]])[0]
        return "FAILURE" if result == 1 else "NORMAL"
    else:
        # fallback logic
        if temp > 80 or vib > 8 or curr > 15 or pre > 10 or rpm > 8:
            return "FAILURE"
        return "NORMAL"

# ===============================
# UI BUTTON
# ===============================
if st.button("🔄 Generate Sensor Reading & Predict"):

    temp, vib, curr, pre, rpm = generate_sensor_data()
    prediction = predict(temp, vib, curr, pre, rpm)
    prediction="prediction"

    # ===============================
    # SHOW METRICS
    # ===============================
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("🌡 Temperature", f"{temp:.2f}")
    col2.metric("📳 Vibration", f"{vib:.2f}")
    col3.metric("⚡ Current", f"{curr:.2f}")
    col4.metric(" Pressure", f"{pre:.2f}")
    col5.metric(" Rpm", f"{pre:.2f}")

    # ===============================
    # ALERT SYSTEM
    # ===============================
    if prediction == "FAILURE":
        st.error("⚠️ MACHINE FAILURE DETECTED!")
    else:
        st.success("✅ Machine Operating Normally")

    # ===============================
    # SAVE RESULTS
    # ===============================
    new_data = pd.DataFrame([{
        "temperature": temp,
        "vibration": vib,
        "current": curr,
        "pressure": pre,
        "rpm": rpm
        
    }])

    df = pd.read_csv(output_file)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(output_file, index=False)

    # ===============================
    # DISPLAY HISTORY
    # ===============================
    st.subheader("📊 Prediction History")
    st.dataframe(df)

    # ===============================
    # VISUALIZATION
    # ===============================
    if len(df) > 1:
        st.subheader("📈 Sensor Trends")

        fig, ax = plt.subplots()
        ax.plot(df["temperature"], label="Temperature")
        ax.plot(df["vibration"], label="Vibration")
        ax.plot(df["current"], label="Current")
        ax.plot(df["pressure"], label="Pressure")
        ax.plot(df["rpm"], label="rpm")

        ax.legend()
        st.pyplot(fig)
