# Fuel Consumption Prediction Web App

This Flask web application predicts fuel consumption for vehicles using machine learning models. The project focuses on improving prediction accuracy and reducing error rates across various machine learning algorithms.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Highlights](#project-highlights)
- [Handling Outliers](#handling-outliers)
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

3. **Fallback Mechanism** (Not Mentioned):
   - A fallback mechanism is implemented to handle cases where the given input does not exist in the CSV file or the input values don't match. In such scenarios, a default prediction from a selected model is used, introducing a level of robustness to the application.

4. **Error Percentage Calculation**:
   - The application calculates the error percentage based on the closest prediction and the actual CO2 value. This provides a quantitative measure of prediction accuracy, allowing users to assess the reliability of the predicted values.

5. **Model Training and Loading**:
   - Machine learning models are trained and saved as pickle files (`*.pkl`). During runtime, these pre-trained models are loaded into the application. This ensures that the models have already learned patterns from historical data, contributing to improved accuracy.

6. **Data Loading and Organization**:
   - Fuel consumption data is loaded from the CSV file and organized by car make and model. This structured organization allows for efficient retrieval of data relevant to the selected input, facilitating accurate predictions.

## Handling Outliers

Outliers in the data can significantly impact the performance of machine learning models. To address this issue, the following techniques have been employed:

1. **Data Preprocessing**:
   - Prior to training the machine learning models, the dataset undergoes preprocessing steps. These steps include identifying and handling outliers, ensuring a cleaner and more robust dataset.

2. **Outlier Detection Techniques**:
   - Statistical techniques such as Z-score and IQR (Interquartile Range) are employed to detect and handle outliers. Outliers are either removed or transformed to mitigate their impact on model training.

3. **Feature Scaling**:
   - Feature scaling techniques, such as Min-Max scaling or Standardization, are applied to ensure that outliers do not disproportionately influence the learning process. Scaling helps in achieving better convergence during model training.

4. **Robust Models**:
   - The inclusion of robust machine learning models, such as Random Forest and XGBoost, inherently provides resilience against outliers. These models are less sensitive to extreme values, contributing to improved overall performance.

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
