import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):

    df = df.dropna()

# 🔥 FEATURE ENGINEERING (VERY IMPORTANT)
    df['temp_vib'] = df['temperature'] * df['vibration']
    df['power_load'] = df['current'] * df['temperature']

    X = df[['temperature', 'vibration', 'current', 'pressure', 'rpm']]
    y = df['failure']

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return X, y