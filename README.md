# 🔧 AI-Powered Predictive Maintenance System for IoT Devices

![GitHub repo size](https://img.shields.io/badge/Repo-Optimized-blue)
![ML Model](https://img.shields.io/badge/Model-RandomForest-success)
![Deployment](https://img.shields.io/badge/API-Flask-orange)
![UI](https://img.shields.io/badge/UI-Streamlit-red)

---

## 🚀 Overview
An end-to-end AI system that predicts machine failures using IoT sensor data with real-time API and interactive dashboard visualization.

---

## 🌍 Real-World Applications
- Manufacturing Industry
- Automotive Systems
- Aviation Maintenance
- Power Plants
- Industrial IoT Monitoring

---

## 🎯 Objective
Predict machine health using sensor data:
- Temperature 🌡️  
- Vibration 📳  
- Current ⚡  

Outputs:
- Normal Operation ✅  
- Failure Risk ⚠️  

---

## 🧠 Problem Statement
Machines fail unexpectedly causing:
- High maintenance cost
- Downtime
- Safety risks

This system helps predict failures in advance using AI.

---

## 🏗️ System Architecture

IoT Sensor Data
↓
Data Preprocessing
↓
Machine Learning Model (Random Forest)
↓
Flask API (Backend)
↓
Streamlit Dashboard (Frontend)
↓
Prediction Output

---

## ⚙️ Tech Stack
- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- Streamlit  
- Matplotlib  

---

## 📊 Dataset
Simulated IoT sensor dataset:
- temperature
- vibration
- current
- failure label

---

## 🤖 Machine Learning Model
- Random Forest Classifier
- Binary Classification:
  - 0 → Normal
  - 1 → Failure

---

## 🚀 Features
✔ Real-time prediction API  
✔ Interactive dashboard  
✔ IoT simulation  
✔ ML-based failure detection  
✔ End-to-end pipeline  

---

## 🖥️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Train model
python train.py
3. Run backend API
python app.py
4. Run dashboard
streamlit run dashboard.py
📁 Project Structure
AI-Predictive-Maintenance/
│
├── data/
├── models/
├── src/
├── app.py
├── train.py
├── dashboard.py
├── requirements.txt
├── README.md
📌 Project Note
⚠️ Large datasets and trained models are excluded using .gitignore to keep the repository lightweight and reproducible.

🙏 Credits
Special thanks to Umesh Yadav Sir for guidance and mentorship.

👨‍💻 Author
Muktai Vyawahare