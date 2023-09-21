# Import the necessary libraries
import pandas as pd
from sklearn.linear_model import Lasso
import pickle

# Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Select the relevant features and the target variable
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Split your data into training and testing sets (if not already done)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Lasso Regression model
lasso_model = Lasso(alpha=1.0)  # You can adjust the alpha parameter for regularization
lasso_model.fit(X_train, y_train)

# Evaluate the model (optional)
from sklearn.metrics import mean_squared_error, r2_score
y_pred = lasso_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save the trained Lasso Regression model to a pickle file
with open('lasso_model.pkl', 'wb') as model_file:
    pickle.dump(lasso_model, model_file)