```markdown
# Fuel Consumption Prediction Web App

This Flask web application predicts fuel consumption for vehicles using machine learning models. Users input specific vehicle features and receive predictions from pre-trained models.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running the application, ensure the following dependencies are installed:

- Python 3.x
- Flask
- NumPy
- scikit-learn
- pickle

Install dependencies using `pip`:

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

The application is now running locally at `http://127.0.0.1:5000/`.

## Working Explanation

1. **Importing Dependencies**:
   - Libraries such as `csv`, `numpy` (as `np`), `Flask`, `request`, `render_template`, and `pickle` are imported.

2. **Loading Trained Models**:
   - Pre-trained machine learning models (linear regression, ridge regression, lasso regression, and elastic net regression) are loaded using `pickle` into a dictionary called `models`.

3. **Loading Fuel Consumption Data**:
   - The `load_fuel_consumption_data()` function reads fuel consumption data from 'FuelConsumption.csv', organizing it by car make and model in the `fuel_consumption_data` dictionary. Unique car makes are stored in the `makes` set.

4. **Flask App Initialization**:
   - A Flask app is initialized with `app = Flask(__name__)`.

5. **Home Route** (`/`):
   - The home route, defined by the `home()` function, allows users to select a car make from a dropdown menu. The selected make is passed as `selected_company` to the 'index.html' template.

6. **Prediction Route** (`/predict`):
   - The `predict()` function processes a POST request, extracts input features from a form, and makes predictions using the loaded machine learning models. The best model is selected based on the highest prediction and results are rendered on 'index.html'.

7. **Index Route** (`/index`):
   - Similar to the home route, it allows users to select a car make from a dropdown menu. The selected make is passed as `selected_company` to the 'index.html' template.

8. **Graph Representation Route** (`/graph_representation`):
   - This route displays scatter plots based on the selected car make. It takes `selected_make` as a parameter and renders the 'graph.html' template, passing fuel consumption data and makes for plotting.

9. **Function to Get Unique Makes and Models**:
   - `get_unique_models()` extracts unique car makes and their associated models from the data.

10. **Function to Get Model Specifications**:
    - `get_model_specs()` retrieves specifications (e.g., fuel consumption, CO2 emissions) based on the selected car make and model.

11. **Compare Route** (`/compare`):
    - Allows users to compare specifications of two different vehicle models. Users can select two makes and models from dropdown menus, and selected specifications are displayed on 'compare.html'.

12. **Running the App**:
    - The app runs with `if __name__ == "__main__": app.run(debug=True)`.

## Usage

### Home Page

- Access the home page at `http://127.0.0.1:5000/`.
- Select a vehicle make (company) from the dropdown menu.
- Click the "Predict" button to see the fuel consumption prediction using the best model.

### Comparing Vehicle Models

- Access the comparison page by clicking "Compare Vehicle Models" in the navigation bar.
- Select two different vehicle makes and models to compare their specifications.

### Viewing Scatter Plots

- Access the scatter plot page by clicking "View Scatter Plots" in the navigation bar.
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
    ├── requirement.txt
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
