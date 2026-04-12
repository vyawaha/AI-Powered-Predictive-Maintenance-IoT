from src.data_loader import load_data
from src.data_preprocessing import preprocess_data
from src.train_model import train_model
from src.visualize import plot_results
import pandas as pd

# Step 1
data = load_data("data/iot_sensor_data.csv")

# Step 2
X, y = preprocess_data(data)

# Step 3
y_test, y_pred = train_model(X, y)

# Step 4
plot_results(y_test, y_pred)

# Step 5 (save predictions)
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

results.to_csv("outputs/predictions.csv", index=False)

print("Pipeline Completed")
