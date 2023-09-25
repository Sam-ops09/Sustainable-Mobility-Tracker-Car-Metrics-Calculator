# Fuel Consumption Prediction Web Application

This is a Flask-based web application for predicting fuel consumption using machine learning models. The application provides features to select different machine learning models and compare vehicle specifications.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the Application](#starting-the-application)
  - [Home Page](#home-page)
  - [Prediction Page](#prediction-page)
  - [Comparison Page](#comparison-page)
  - [Graph Representation Page](#graph-representation-page)
- [Data Sources](#data-sources)
- [License](#license)

## Features

- Predict fuel consumption using multiple machine learning models.
- Select from a range of machine learning models (Linear Regression, Ridge Regression, Lasso Regression, Elastic Net Regression).
- Compare specifications of different vehicle models.
- Visualize fuel consumption data with scatter plots.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Flask
- NumPy
- scikit-learn
- pickle

### Installation

1. Clone this repository to your local machine using `git clone`.

2. Install the required Python packages using `pip`:

```bash
pip install flask numpy scikit-learn
```

## Usage

### Starting the Application

To start the Flask application, navigate to the project directory in your terminal and run:

```bash
python app.py
```

The application will run on `http://localhost:5000/`.

### Home Page

- The home page (`/`) displays a dropdown menu to select a vehicle make (company).

### Prediction Page

- Access the prediction page by selecting a make from the dropdown and clicking "Predict" or by navigating to `/predict`.
- Enter numerical features related to the vehicle, and the application will predict fuel consumption using the selected machine learning model.
- The result includes the selected model and the predicted fuel consumption.

### Comparison Page

- Access the comparison page by clicking "Compare" in the navigation bar or by navigating to `/compare`.
- Compare specifications of two different vehicle models, including fuel consumption, CO2 emissions, engine size, cylinders, vehicle class, and transmission.

### Graph Representation Page

- Access the graph representation page by clicking "Graph Representation" in the navigation bar or by navigating to `/graph_representation`.
- Visualize fuel consumption data with scatter plots. Select a vehicle make (company) to see scatter plots for that make.

## Data Sources

The application uses fuel consumption data from the `FuelConsumption.csv` file. The data includes information about vehicle makes, models, and fuel consumption in miles per gallon (MPG).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
