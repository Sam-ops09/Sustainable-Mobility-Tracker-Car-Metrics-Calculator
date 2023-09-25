import csv
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained models
models = {}
model_names = ['linear_model', 'ridge_model', 'lasso_model', 'elastic_net_model']

# Load each model and store it in the 'models' dictionary
for model_name in model_names:
    with open(f'{model_name}.pkl', 'rb') as model_file:
        models[model_name] = pickle.load(model_file)

# Function to load fuel consumption data from the CSV file
def load_fuel_consumption_data():
    fuel_consumption_data = {}  # Dictionary to store fuel consumption data
    makes = set()  # Set to store unique make values

    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            company = row['MAKE']
            model = row['MODEL']
            fuel_consumption = float(row['FUELCONSUMPTION_COMB_MPG'])

            # Check if the company (make) is in the dictionary
            if company not in fuel_consumption_data:
                fuel_consumption_data[company] = {}

            # Check if the model is in the dictionary for this company
            if model not in fuel_consumption_data[company]:
                fuel_consumption_data[company][model] = []

            # Append the fuel consumption value to the correct model list
            fuel_consumption_data[company][model].append(fuel_consumption)

            # Add the make to the set of makes
            makes.add(company)

    return fuel_consumption_data, sorted(list(makes))

# Load fuel consumption data and get a list of unique companies (makes)
fuel_consumption_data, companies = load_fuel_consumption_data()

# Define the home route
@app.route('/')
def home():
    selected_company = request.args.get('selected_company', companies[0])
    return render_template('index.html', companies=companies, selected_company=selected_company)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Extract input features from the form
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    best_model_name = None
    best_prediction = None

    # Iterate through the models and make predictions
    for model_name, model in models.items():
        prediction = model.predict(final_features)[0]
        if best_model_name is None or prediction > best_prediction:
            best_model_name = model_name
            best_prediction = prediction

    # Render the prediction results
    return render_template('index.html', best_model=f'Selected Model: {best_model_name}', best_prediction=f'Prediction: {round(best_prediction, 2)}')

# Define the index route
@app.route('/index')
def index():
    selected_company = request.args.get('selected_company', 'default_company')
    return render_template('index.html', selected_company=selected_company)

# Define the route for displaying scatter plots
@app.route('/graph_representation')
def graph_representation():
    selected_make = request.args.get('selected_make')
    return render_template('graph.html', fuel_consumption_data=fuel_consumption_data, makes=companies, selected_make=selected_make)

# Function to get unique makes and their associated models
def get_unique_models():
    makes_and_models = {}

    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            make = row['MAKE']
            model = row['MODEL']
            if make not in makes_and_models:
                makes_and_models[make] = [model]
            else:
                makes_and_models[make].append(model)
    return makes_and_models

# Function to get model specifications based on make and model
def get_model_specs(make, model):
    specs = {}

    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['MAKE'] == make and row['MODEL'] == model:
                # Assign the specifications to the dictionary
                specs = {
                    'Make': row['MAKE'],
                    'Model': row['MODEL'],
                    'Fuel Consumption Comb (L/100 km)': row['FUELCONSUMPTION_COMB'],
                    'CO2 Emissions (g/km)': row['CO2EMISSIONS'],
                    'Engine Size (L)': row['ENGINESIZE'],
                    'Cylinders': row['CYLINDERS'],
                    'Vehicle Class': row['VEHICLECLASS'],
                    'Transmission': row['TRANSMISSION']
                }
                break  # No need to continue once specs are found

    return specs

# Define the route for comparing two vehicle models
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    # Get the unique makes and their associated models
    makes_and_models = get_unique_models()

    if request.method == 'POST':
        make1 = request.form.get('make1')
        model1 = request.form.get('model1')
        make2 = request.form.get('make2')
        model2 = request.form.get('model2')

        # Get specifications for the selected models
        specs1 = get_model_specs(make1, model1)
        specs2 = get_model_specs(make2, model2)

        # Render the comparison results
        return render_template('compare.html', makes_and_models=makes_and_models, specs1=specs1, specs2=specs2)

    return render_template('compare.html', makes_and_models=makes_and_models)

if __name__ == "__main__":
    app.run(debug=True)