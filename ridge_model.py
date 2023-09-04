# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Step 2: Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Step 3: Select the relevant features and the target variable (CO2 emissions)
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Step 4: Split your data into training and testing sets (if you haven't already)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train the Ridge Regression model
ridge_model = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization
ridge_model.fit(X_train, y_train)

# Step 6: Evaluate the model (optional)
# You can evaluate the model's performance on the test set using metrics like Mean Squared Error (MSE) or R-squared.
y_pred = ridge_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Step 7: Save the trained Ridge Regression model to a pickle file
with open('ridge_model.pkl', 'wb') as model_file:
    pickle.dump(ridge_model, model_file)
