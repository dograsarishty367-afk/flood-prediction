# Flood Prediction Using Machine Learning

## Project Overview
This project predicts the probability of flooding using environmental and geographical factors such as rainfall intensity, river management, deforestation, drainage systems, and urbanization.

The model is trained using a Random Forest Regressor to estimate flood probability based on multiple environmental indicators.

---

## Dataset
The dataset contains 50,000 samples with 21 features representing different environmental conditions.

Important features include:
- MonsoonIntensity
- TopographyDrainage
- RiverManagement
- Deforestation
- Urbanization
- ClimateChange
- DrainageSystems
- PopulationScore
- WetlandLoss
- PoliticalFactors

Target variable:
FloodProbability

---

## Machine Learning Model
Random Forest Regressor

Why this model:
- Handles complex relationships
- Works well with tabular data
- Reduces overfitting

---

## Model Performance
R² Score ≈ 0.73  
Mean Squared Error: very low

---

## Visualizations
This project includes:
- Flood probability distribution
- Correlation heatmap
- Actual vs predicted plot
- Feature importance graph

---

## Project Structure
flood_prediction_project
│
├── flood_prediction.py
├── flood_prediction.ipynb
├── flood.csv
└── README.md

---

## How to Run

Clone the repository

git clone https://github.com/dograsarishty367-afk/flood-prediction.git

Install libraries

pip install pandas numpy matplotlib seaborn scikit-learn

Run the model

python3 flood_prediction.py

---

## Future Improvements
- Use real rainfall and river level data
- Try additional ML models
- Build a web interface
- Integrate real-time weather APIs

---

## Author
Sarishty Dogra
