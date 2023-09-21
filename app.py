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

if __name__ == "__main__":
    app.run(debug=True)
