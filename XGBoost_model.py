# Step 1: Import the necessary libraries
import pandas as pd
from xgboost import XGBRegressor
import pickle

# Step 2: Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Step 3: Select the relevant features and the target variable (CO2 emissions)
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Step 4: Split your data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Create and train the XGBoost model
xgboost_model = XGBRegressor(random_state=42)
xgboost_model.fit(X_train, y_train)

# Step 8: Save the trained XGBoost model to a pickle file
with open('xgboost_model.pkl', 'wb') as model_file:
    pickle.dump(xgboost_model, model_file)

# Step 9: Make a prediction using the XGBoost model
sample_input = [[2, 4, 9.9]]
predicted_co2_emission_xgboost = xgboost_model.predict(sample_input)
print(f"Predicted CO2 Emission (XGBoost): {predicted_co2_emission_xgboost[0]}")
