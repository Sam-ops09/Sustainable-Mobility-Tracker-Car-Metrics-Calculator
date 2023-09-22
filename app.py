import csv
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained models
linear_model = pickle.load(open('linear_model.pkl', 'rb'))
ridge_model = pickle.load(open('ridge_model.pkl', 'rb'))
lasso_model = pickle.load(open('lasso_model.pkl', 'rb'))
elastic_net_model = pickle.load(open('elastic_net_model.pkl', 'rb'))

def get_unique_companies():
    unique_companies = set()
    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            unique_companies.add(row['MAKE'])
    return sorted(list(unique_companies))  # Sort the companies alphabetically

@app.route('/')
def home():
    companies = get_unique_companies()
    selected_company = request.args.get('selected_company', companies[0])
    # Your code for fetching and processing data based on the selected company goes here
    return render_template('index.html', companies=companies, selected_company=selected_company)

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    linear_prediction = linear_model.predict(final_features)
    ridge_prediction = ridge_model.predict(final_features)
    lasso_prediction = lasso_model.predict(final_features)
    elastic_net_prediction = elastic_net_model.predict(final_features)

    best_model = 'Linear Regression'
    best_prediction = linear_prediction[0]
    
    # if linear_prediction[0] > best_prediction:
    #     best_model = 'Linear Regression'
    #     best_prediction = linear_prediction[0]

    if ridge_prediction[0] > best_prediction:
        best_model = 'Ridge Regression'
        best_prediction = ridge_prediction[0]

    if lasso_prediction[0] > best_prediction:
        best_model = 'Lasso Regression'
        best_prediction = lasso_prediction[0]

    if elastic_net_prediction[0] > best_prediction:
        best_model = 'Elastic Net Regression'
        best_prediction = elastic_net_prediction[0]

    return render_template('index.html',
        best_model=f'Selected Model: {best_model}',
        best_prediction=f'Prediction: {round(best_prediction, 2)}')

@app.route('/index')
def index():
    selected_company = request.args.get('selected_company', 'default_company')
    # Your code for fetching and processing data based on the selected company goes here
    return render_template('index.html', selected_company=selected_company)

@app.route('/graph_representation')
def graph_representation():
    # Add code here to read data from the CSV file
    fuel_consumption_data = {}
    makes = set()  # Create a set to store unique "MAKE" values

    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Assuming you have 'MAKE' column in your CSV
            company = row['MAKE']
            model = row['MODEL']
            fuel_consumption = float(row['FUELCONSUMPTION_COMB_MPG'])
            
            if company not in fuel_consumption_data:
                fuel_consumption_data[company] = {}  # Change to a dictionary for models
            
            if model not in fuel_consumption_data[company]:
                fuel_consumption_data[company][model] = []  # Initialize an empty list for each model
            
            fuel_consumption_data[company][model].append(fuel_consumption)  # Append to the correct model list

            # Add the "MAKE" value to the set
            makes.add(company)

    # Print some data to check if it's loaded correctly
    selected_make = request.args.get('selected_make')

    # Convert the set of "MAKE" values to a list for dropdown options
    makes_list = list(makes)

    # You can now pass fuel_consumption_data and makes_list to the template
    return render_template('graph.html', fuel_consumption_data=fuel_consumption_data, makes=makes_list, selected_make=selected_make)

# Define a function to read the available models from the CSV file
def get_available_models():
    available_models = set()  # Use a set to ensure unique model names

    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            available_models.add(row['MODEL'])

    return sorted(list(available_models))  # Sort the models alphabetically

# Modify the get_unique_makes function to also get models
def get_unique_makes():
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
    specs = {}  # Initialize an empty dictionary to store model specifications

    # Open and read the CSV file
    with open('FuelConsumption.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['MAKE'] == make and row['MODEL'] == model:
                # Assign the specifications to the dictionary
                specs['Make'] = row['MAKE']
                specs['Model'] = row['MODEL']
                specs['Fuel Consumption Comb (L/100 km)'] = row['FUELCONSUMPTION_COMB']
                specs['CO2 Emissions (g/km)'] = row['CO2EMISSIONS']
                specs['Engine Size (L)'] = row['ENGINESIZE']
                specs['Cylinders'] = row['CYLINDERS']
                specs['Vehicle Class'] = row['VEHICLECLASS']
                specs['Transmission'] = row['TRANSMISSION']

    return specs

# Modify the /compare route
@app.route('/compare', methods=['GET', 'POST'])
def compare():
    makes_and_models = get_unique_makes()

    if request.method == 'POST':
        make1 = request.form.get('make1')
        model1 = request.form.get('model1')
        make2 = request.form.get('make2')
        model2 = request.form.get('model2')

        specs1 = get_model_specs(make1, model1)
        specs2 = get_model_specs(make2, model2)

        return render_template('compare.html', makes_and_models=makes_and_models, specs1=specs1, specs2=specs2)

    return render_template('compare.html', makes_and_models=makes_and_models)


if __name__ == "__main__":
    app.run(debug=True)