import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv("FuelConsumption.csv")

# Use the required features
selected_features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']
cdf = df[selected_features]

# Training Data and Predictor Variable
x = cdf[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']]
y = cdf['CO2EMISSIONS']

# Create and train the linear regression model
linear_model = LinearRegression()
linear_model.fit(x, y)

# Save the trained model to a file
with open('linear_model.pkl', 'wb') as model_file:
    pickle.dump(linear_model, model_file)
