```markdown
# Fuel Consumption Prediction Web App

This Flask web application predicts fuel consumption for vehicles using machine learning models. The project focuses on improving prediction accuracy and reducing error rates across various machine learning algorithms.

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

## Project Highlights

### Error Rate Reduction and Accuracy Improvement

The primary focus of this project is to enhance prediction accuracy and reduce error rates. The following strategies have been implemented:

1. **Multiple Models Integration**:
   - Various machine learning models, including linear regression, ridge regression, lasso regression, elastic net regression, neural network models, XGBoost, and Random Forest, are integrated to benefit from diverse modeling approaches.

2. **Model Selection Based on Prediction Accuracy**:
   - The application dynamically selects the best model for a given input by comparing predictions across all models. The model with the closest prediction to the actual value is chosen.

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
