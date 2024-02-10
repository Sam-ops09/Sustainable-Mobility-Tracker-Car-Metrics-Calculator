# Fuel Consumption Prediction Web App

This Flask web application is designed to predict fuel consumption for vehicles using machine learning models. It allows users to input certain features of a vehicle and receive a prediction from a selection of trained models.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- NumPy
- scikit-learn
- pickle

You can install these dependencies using `pip`:

```bash
pip install flask numpy scikit-learn
```

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/fuel-consumption-prediction.git
```

2. Change your working directory to the project folder:

```bash
cd fuel-consumption-prediction
```

3. Run the Flask application:

```bash
python app.py
```

The application should now be running locally at `http://127.0.0.1:5000/`.

## Working Explanation

1. **Importing Dependencies**:
   - You start by importing necessary libraries such as `csv`, `numpy` (as `np`), `Flask`, `request`, `render_template`, and `pickle`.

2. **Loading Trained Models**:
   - You load pre-trained machine learning models (linear regression, ridge regression, lasso regression, and elastic net regression) using `pickle`. These models are stored in a dictionary called `models`.

3. **Loading Fuel Consumption Data**:
   - You define a function `load_fuel_consumption_data()` to read fuel consumption data from a CSV file named 'FuelConsumption.csv'. The data is stored in a dictionary `fuel_consumption_data`, which organizes the data by car make and model. You also create a set `makes` to store unique car makes.

4. **Flask App Initialization**:
   - You initialize a Flask app with `app = Flask(__name__)`.

5. **Home Route** (`/`):
   - The home route is defined with the `home()` function. It allows users to select a car make from a dropdown menu. The selected make is passed as a parameter (`selected_company`) to the 'index.html' template.

6. **Prediction Route** (`/predict`):
   - The prediction route is defined with the `predict()` function. It processes a POST request, extracts input features from a form, and makes predictions using the loaded machine learning models. It selects the best model based on the highest prediction and renders the result on the 'index.html' template.

7. **Index Route** (`/index`):
   - This route is similar to the home route but is accessed separately. It also allows users to select a car make from a dropdown menu, and the selected make is passed as `selected_company` to the 'index.html' template.

8. **Graph Representation Route** (`/graph_representation`):
   - This route is used to display scatter plots based on the selected car make. It takes `selected_make` as a parameter and renders the 'graph.html' template, passing the fuel consumption data and makes for plotting.

9. **Function to Get Unique Makes and Models**:
   - `get_unique_models()` extracts unique car makes and their associated models from the data.

10. **Function to Get Model Specifications**:
    - `get_model_specs()` retrieves specifications (e.g., fuel consumption, CO2 emissions) based on the selected car make and model.

11. **Compare Route** (`/compare`):
    - This route allows users to compare specifications of two different vehicle models. Users can select two makes and models from dropdown menus, and the selected specifications are displayed on the 'compare.html' template.

12. **Running the App**:
    - The app runs with `if __name__ == "__main__": app.run(debug=True)`.

Overall, the Flask application loads pre-trained machine learning models, handles user input and predictions, displays data visualizations, and allows users to compare vehicle specifications. It combines machine learning with web functionality to provide an interactive experience for users interested in exploring and comparing vehicle data.

## Usage

### Home Page

- Access the home page by opening a web browser and navigating to `http://127.0.0.1:5000/`.
- Select a vehicle make (company) from the dropdown menu.
- Click the "Predict" button to see the fuel consumption prediction using the best model.

### Comparing Vehicle Models

- Access the comparison page by clicking on the "Compare Vehicle Models" link in the navigation bar.
- Select two different vehicle makes and models to compare their specifications.

### Viewing Scatter Plots

- Access the scatter plot page by clicking on the "View Scatter Plots" link in the navigation bar.
- Select a vehicle make to view scatter plots of fuel consumption data for different models of that make.

## Project Structure

The project has the following structure:

```
fuel-consumption-prediction/
    ├── app.py                
    ├── linear_model.pkl       
    ├── ridge_model.pkl        
    ├── lasso_model.pkl         
    ├── elastic_net_model.pkl   
    ├── linear_model.py       
    ├── ridge_model.py        
    ├── lasso_model.py        
    ├── elastic_net_model.py
    ├── neural_network_model.py
    ├── neural_network_model.pkl
    ├── random_forest_model.py
    ├── random_forest_model.pkl
    ├── ridge_model.py
    ├── ridge_model.pkl
    ├── XGBoost_model.py
    ├── XGBoost_model.py
    ├── FuelConsumption.csv     
    ├── templates/             
    │   ├── index.html        
    │   ├── compare.html       
    │   ├── graph.html   
    ├── static/                 
    │   ├── style.css          
    │   ├── script.js        
    ├── README.md     
```

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
