import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data/iot_sensor_data.csv")

# Features & target
X = df[['temperature', 'vibration', 'current']]
y = df['failure']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "models/model.pkl")

print("Model trained and saved successfully!")
