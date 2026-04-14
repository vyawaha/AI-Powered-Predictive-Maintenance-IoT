import streamlit as st
import requests
import matplotlib.pyplot as plt

st.title("AI Predictive Maintenance Dashboard")

# Inputs
temp = st.slider("Temperature", 0, 100, 50)
vib = st.slider("Vibration", 0.0, 5.0, 1.0)
curr = st.slider("Current", 0, 20, 10)

# Predict
if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={
            "temperature": temp,
            "vibration": vib,
            "current": curr
        }
    )

    st.success(response.json()["prediction"])

# 📊 Fake sensor trend graph (simulation)
st.subheader("Sensor Trend Visualization")

time = list(range(10))
temp_data = [temp + i*0.5 for i in time]
vib_data = [vib + i*0.1 for i in time]

fig, ax = plt.subplots()

ax.plot(time, temp_data, label="Temperature")
ax.plot(time, vib_data, label="Vibration")

ax.set_xlabel("Time")
ax.set_ylabel("Values")
ax.legend()

st.pyplot(fig)
