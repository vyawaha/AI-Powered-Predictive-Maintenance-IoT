import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv("data/iot_sensor_data.csv")

# Features
X = df[['temperature', 'vibration', 'current']]

# Train anomaly model
model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(X)

# -1 = anomaly, 1 = normal
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

df.to_csv("data/iot_sensor_data_with_anomaly.csv", index=False)

print("Anomaly detection completed!")