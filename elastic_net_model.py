# Import necessary libraries
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
import pickle

# Load your dataset
df = pd.read_csv("FuelConsumption.csv")

# Select relevant features and the target variable
features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']
target = 'CO2EMISSIONS'
X = df[features]
y = df[target]

# Split your data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Elastic Net Regression model
elastic_net_model = ElasticNet(alpha=1.0, l1_ratio=0.5)
elastic_net_model.fit(X_train, y_train)

# Save the trained Elastic Net Regression model to a pickle file
with open('elastic_net_model.pkl', 'wb') as model_file:
    pickle.dump(elastic_net_model, model_file)