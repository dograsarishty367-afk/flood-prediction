import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

print("\n==============================")
print(" FLOOD PREDICTION ML PROJECT ")
print("==============================\n")

# -----------------------------
# Load Dataset
# -----------------------------

print("Loading dataset...\n")

df = pd.read_csv("flood.csv")

print("Dataset Shape:", df.shape)

print("\nColumns in Dataset:")
print(df.columns)

print("\nFirst 5 rows:\n")
print(df.head())

# -----------------------------
# Check Missing Values
# -----------------------------

print("\nChecking missing values...\n")
print(df.isnull().sum())

# -----------------------------
# Basic Statistics
# -----------------------------

print("\nDataset Statistics\n")
print(df.describe())


# -----------------------------
# Visualization 1
# Flood Probability Distribution
# -----------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["FloodProbability"], bins=30, kde=True)
plt.title("Flood Probability Distribution")
plt.xlabel("Flood Probability")
plt.ylabel("Count")
plt.show()


# -----------------------------
# Visualization 2
# Correlation Heatmap
# -----------------------------

plt.figure(figsize=(14,10))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()


# -----------------------------
# Prepare Data for ML
# -----------------------------

print("\nPreparing data for machine learning...\n")

X = df.drop("FloodProbability", axis=1)
y = df["FloodProbability"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data size:", X_train.shape)
print("Testing data size:", X_test.shape)


# -----------------------------
# Train Model
# -----------------------------

print("\nTraining Random Forest Model...\n")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed!")


# -----------------------------
# Predictions
# -----------------------------

print("\nMaking predictions...\n")

predictions = model.predict(X_test)

# -----------------------------
# Model Evaluation
# -----------------------------

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")

print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# -----------------------------
# Visualization 3
# Actual vs Predicted
# -----------------------------

plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions)
plt.xlabel("Actual Flood Probability")
plt.ylabel("Predicted Flood Probability")
plt.title("Actual vs Predicted Flood Probability")
plt.show()


# -----------------------------
# Feature Importance
# -----------------------------

print("\nFeature Importance\n")

importances = model.feature_importances_
features = X.columns

importance_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
})

importance_df = importance_df.sort_values(by="Importance", ascending=False)

print(importance_df)


# -----------------------------
# Visualization 4
# Feature Importance Graph
# -----------------------------

plt.figure(figsize=(10,6))
sns.barplot(
    x="Importance",
    y="Feature",
    data=importance_df
)

plt.title("Feature Importance for Flood Prediction")
plt.show()


# -----------------------------
# Example Prediction
# -----------------------------

print("\nExample Prediction\n")

sample = X_test.iloc[0].values.reshape(1,-1)

prediction = model.predict(sample)

print("Predicted Flood Probability:", prediction[0])

print("\nProject execution completed successfully!") 
