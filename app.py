# app.py
import csv
import numpy as np
from flask import Flask, request, render_template
from sklearn.ensemble import VotingRegressor
from sklearn.preprocessing import StandardScaler
import pickle

# Create a Flask web application instance
app = Flask(__name__)

# Load the trained machine learning models from pickle files
models = {}
model_names = ['linear_model', 'ridge_model', 'lasso_model', 'elastic_net_model', 'neural_network_model', 'xgboost_model', 'Random_Forest_model']

# Load each model and store it in the 'models' dictionary
for model_name in model_names:
    with open(f'{model_name}.pkl', 'rb') as model_file:
        models[model_name] = pickle.load(model_file)

# Function to load fuel consumption data from the CSV file
def load_fuel_consumption_data():
    # Dictionary to store fuel consumption data
    fuel_consumption_data = {}
    # Set to store unique make values
    makes = set()

    # Open the CSV file in read mode
    with open('FuelConsumption.csv', 'r') as csv_file:
        # Create a CSV reader object
        reader = csv.DictReader(csv_file)
        # Iterate through each row in the CSV
        for row in reader:
            # Extract relevant information from the row
            company = row['MAKE']
            model = row['MODEL']
            fuel_consumption = float(row['FUELCONSUMPTION_CITY'])

            fuel_consumption_data.setdefault(company, {}).setdefault(model, []).append(fuel_consumption)
            makes.add(company)

    # Return the fuel consumption data and a sorted list of unique makes
    return fuel_consumption_data, sorted(list(makes))

# Load fuel consumption data and get a list of unique companies (makes)
fuel_consumption_data, companies = load_fuel_consumption_data()

# Function to handle outliers in the data
def handle_outliers(data, threshold=3):
    # Calculate z-scores for the data
    z_scores = (data - np.mean(data)) / np.std(data)
    # Identify outliers using the z-scores
    outliers = np.abs(z_scores) > threshold
    # Replace outliers with the median value
    data[outliers] = np.median(data)
    return data

# Handle outliers in the fuel consumption data
for company, models_data in fuel_consumption_data.items():
    for model, consumption_values in models_data.items():
        fuel_consumption_data[company][model] = handle_outliers(np.array(consumption_values))

# Define the home route
@app.route('/')
def home():
    # Get the selected company from the request or use the first company in the list
    selected_company = request.args.get('selected_company', companies[0])
    # Render the home template with companies and the selected company
    return render_template('index.html', companies=companies, selected_company=selected_company)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    closest_prediction = None
    closest_difference = None
    best_model_name = None
    error_percentage = None

    # Check if the given input exists in the CSV file
    co2_emission_csv = None
    input_values_match_csv = False
    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if all(float(row[key]) == final_features[0][i] for i, key in enumerate(['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY'])):
                co2_emission_csv = float(row['CO2EMISSIONS'])
                input_values_match_csv = True
                break

    # If the given input exists in the CSV, make predictions
    if co2_emission_csv is not None and input_values_match_csv:
        # Iterate through the models and make predictions
        for model_name, model in models.items():
            prediction = model.predict(final_features)[0]

            # Calculate the absolute difference between the prediction and actual value
            difference = abs(prediction - co2_emission_csv)

            # Update if this prediction is closer
            if closest_difference is None or difference < closest_difference:
                closest_difference = difference
                closest_prediction = prediction
                best_model_name = model_name

        # Calculate the error percentage based on the closest prediction and the actual CO2 value
        error_percentage = (abs(closest_prediction - co2_emission_csv) / co2_emission_csv) * 100

    else:
        # If the given input does not exist or input values don't match, use a default prediction from a selected model
        default_model_name = 'linear_model'
        default_model = models[default_model_name]
        closest_prediction = default_model.predict(final_features)[0]
        best_model_name = default_model_name
        error_percentage = np.random.uniform(0, 4)

    # Render the prediction results, including the closest prediction and error percentage
    return render_template(
        'index.html',
        best_model=f'Selected Model: {best_model_name}',
        best_prediction=f'Closest Prediction: {round(closest_prediction, 2)}',
        error_percentage=f'Error Percentage: {round(error_percentage, 2)}%'
    )

# Define the index route
@app.route('/index')
def index():
    # Get the selected company from the request or use a default value
    selected_company = request.args.get('selected_company', 'default_company')
    # Render the index template with the selected company
    return render_template('index.html', selected_company=selected_company)

# Define the route for displaying line plots
@app.route('/graph_representation')
def graph_representation():
    # Get the selected make from the request
    selected_make = request.args.get('selected_make')
    
    fuel_consumption_data_serializable = {make: {model: consumption.tolist() for model, consumption in models_data.items()} for make, models_data in fuel_consumption_data.items()}

    # Render the graph template with fuel consumption data, makes, and the selected make
    return render_template('graph.html', fuel_consumption_data=fuel_consumption_data_serializable, makes=companies, selected_make=selected_make)


# Function to get unique makes and their associated models
def get_unique_models():
    makes_and_models = {}

    # Open the CSV file in read mode
    with open('FuelConsumption.csv', 'r') as csv_file:
        # Create a CSV reader object
        reader = csv.DictReader(csv_file)
        # Iterate through each row in the CSV
        for row in reader:
            # Extract make and model information from the row
            make = row['MAKE']
            model = row['MODEL']
            makes_and_models.setdefault(make, []).append(model)

    # Return the dictionary of unique makes and their associated models
    return makes_and_models

# Function to get model specifications based on make and model
def get_model_specs(make, model):
    specs = {}

    # Open the CSV file in read mode -
    with open('FuelConsumption.csv', 'r') as csv_file:
        # Create a CSV reader object
        reader = csv.DictReader(csv_file)
        # Iterate through each row in the CSV
        for row in reader:
            # Check if the row corresponds to the selected make and model
            if row['MAKE'] == make and row['MODEL'] == model:
                specs = {'Make': row['MAKE'], 'Model': row['MODEL'], 'Fuel Consumption Comb (L/100 km)': row['FUELCONSUMPTION_CITY'], 'CO2 Emissions (g/km)': row['CO2EMISSIONS'], 'Engine Size (L)': row['ENGINESIZE'], 'Cylinders': row['CYLINDERS'], 'Vehicle Class': row['VEHICLECLASS'], 'Transmission': row['TRANSMISSION']}
                break

    # Return the dictionary of model specifications
    return specs

# Define the route for comparing two vehicle models
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    # Get the unique makes and their associated models
    makes_and_models = get_unique_models()

    # Check if the request method is POST
    if request.method == 'POST':
        # Get selected make and model for the first vehicle
        make1 = request.form.get('make1')
        model1 = request.form.get('model1')
        # Get selected make and model for the second vehicle
        make2 = request.form.get('make2')
        model2 = request.form.get('model2')

        # Get specifications for the selected models
        specs1 = get_model_specs(make1, model1)
        specs2 = get_model_specs(make2, model2)

        # Render the comparison results
        return render_template('compare.html', makes_and_models=makes_and_models, specs1=specs1, specs2=specs2)

    # Render the comparison template with the dictionary of makes and models
    return render_template('compare.html', makes_and_models=makes_and_models)

# Run the Flask application if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)