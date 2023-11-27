# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pickle

# Step 2: Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Step 3: Select the relevant features and the target variable (CO2 emissions)
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Step 4: Split your data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Create and train the Random Forest model
random_forest_model = RandomForestRegressor(random_state=42)
random_forest_model.fit(X_train_scaled, y_train)

# Step 8: Save the trained Random Forest model to a pickle file
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(random_forest_model, model_file)