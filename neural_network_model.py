import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import pickle

# Load the dataset
df = pd.read_csv("FuelConsumption.csv")

# Select the relevant features and the target variable (CO2 emissions)
selected_features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']
df = df[selected_features]

# Split the data into training and testing sets
X = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY']]
y = df['CO2EMISSIONS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the Neural Network model with additional tuning parameters
neural_network_model = MLPRegressor(
    hidden_layer_sizes=(600, 50, 25),
    activation='relu',
    max_iter=4000,  # Increase max_iter
    learning_rate_init=0.001,
    alpha=0.0001,  # Add regularization
    random_state=42
)
neural_network_model.fit(X_train_scaled, y_train)

# Save the trained Neural Network model to a pickle file
with open('neural_network_model.pkl', 'wb') as model_file:
    pickle.dump(neural_network_model, model_file)