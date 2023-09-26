# Import the necessary libraries
import pandas as pd
from sklearn.linear_model import ElasticNet
import pickle

# Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Select the relevant features and the target variable
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Split your data into training and testing sets (if not already done)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Elastic Net Regression model
elastic_net_model = ElasticNet(alpha=1.0, l1_ratio=0.5)  # You can adjust the alpha and l1_ratio parameters
elastic_net_model.fit(X_train, y_train)

# Evaluate the model (optional)
from sklearn.metrics import mean_squared_error, r2_score
y_pred = elastic_net_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save the trained Elastic Net Regression model to a pickle file
with open('elastic_net_model.pkl', 'wb') as model_file:
    pickle.dump(elastic_net_model, model_file)
    
sample_input = [[1.5, 4, 6]]

# Make a prediction
predicted_co2_emission = elastic_net_model.predict(sample_input)

# Print the prediction
print(f"Predicted CO2 Emission: {predicted_co2_emission[0]}")