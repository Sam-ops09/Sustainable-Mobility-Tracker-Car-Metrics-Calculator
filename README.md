# Sustainable-Mobility-Tracker

## Overview

This is a Flask web application that predicts fuel consumption and compares vehicle models based on CO2 emissions. It uses machine learning models to make predictions.

## Features

- Predicts fuel consumption using machine learning models.
- Compares vehicle models based on CO2 emissions.
- Visualizes data with line plots.

## Prerequisites

Before running this application, you need to have the following installed:

- Python (version 3.x)
- Flask
- NumPy
- scikit-learn
- pickle

You can install the required packages using pip:

```bash
pip install Flask numpy scikit-learn
```

## Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/fuel-consumption-prediction.git
cd fuel-consumption-prediction
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your web browser and navigate to http://localhost:5000 to access the application.

## Usage

- Home Page: Select a car make and model to predict fuel consumption and see the closest prediction along with the error percentage.
- Compare Page: Compare two vehicle models based on specifications.
- Graph Page: Visualize fuel consumption data with line plots.

## Data Source

The fuel consumption data is sourced from a CSV file named `FuelConsumption.csv`.

## Machine Learning Models

The application uses the following machine learning models for prediction:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net Regression

## Acknowledgments

- This project is for educational purposes.

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
