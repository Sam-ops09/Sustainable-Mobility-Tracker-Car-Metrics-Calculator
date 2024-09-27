# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.linear_model import Ridge
import pickle

# Step 2: Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Step 3: Select the relevant features and the target variable (CO2 emissions)
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Step 4: Split your data into training and testing sets (if you haven't already)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train the Ridge Regression model
ridge_model = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization
ridge_model.fit(X_train, y_train)

# Step 7: Save the trained Ridge Regression model to a pickle file
with open('ridge_model.pkl', 'wb') as model_file:
    pickle.dump(ridge_model, model_file)
    
sample_input = [[2, 4, 9.9]]

# Make a prediction
predicted_co2_emission = ridge_model.predict(sample_input)

# Print the prediction
print(f"Predicted CO2 Emission: {predicted_co2_emission[0]}")
