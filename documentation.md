# Flask Application Documentation

## Introduction

This documentation provides an overview of the features, endpoints, and usage of the Flask application designed to compare vehicle models based on their specifications and predict fuel efficiency.

## Table of Contents

1. [Overview](#introduction)
2. [Getting Started](#getting-started)
3. [Endpoints](#endpoints)
   - [Home](#home)
   - [Prediction](#prediction)
   - [Graph Representation](#graph-representation)
   - [Comparison](#comparison)
4. [Data Sources](#data-sources)
5. [Models](#models)
6. [Running the Application](#running-the-application)

## Getting Started

To use this Flask application, ensure you have the following prerequisites:

- Python installed on your system.
- Required libraries and dependencies (Flask, NumPy, Chart.js, etc.) installed.
- Trained machine learning models (Linear, Ridge, Lasso, Elastic Net) available as pickle files.

Clone the project repository and place the trained model pickle files in the project directory.

## Endpoints

### Home

- **URL**: `/`
- **Description**: The home page where you can select a company and input features for fuel efficiency prediction.

### Prediction

- **URL**: `/predict`
- **Description**: Endpoint for making fuel efficiency predictions based on input features.

### Graph Representation

- **URL**: `/graph_representation`
- **Description**: Displays a scatter plot of company-wise fuel efficiency for a selected make.

### Comparison

- **URL**: `/compare`
- **Description**: Allows users to compare specifications of two vehicle models.

## Data Sources

- Data for fuel consumption and vehicle specifications is sourced from a CSV file named `FuelConsumption.csv`.

## Models

- Trained machine learning models are used for fuel efficiency prediction:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Elastic Net Regression

## Running the Application

1. Install the required dependencies by running: `pip install -r requirements.txt`.

2. Place the trained model pickle files (`linear_model.pkl`, `ridge_model.pkl`, `lasso_model.pkl`, `elastic_net_model.pkl`) in the project directory.

3. Run the Flask application by executing: `python app.py`.

4. Access the application via a web browser using the provided URL.

## Usage

1. Visit the home page to select a company and input features for fuel efficiency prediction.

2. Navigate to the "Graph Representation" page to view a scatter plot of fuel efficiency for a selected make.

3. Use the "Comparison" page to compare specifications of two vehicle models.

## Conclusion

This documentation provides an overview of the Flask application's functionality, endpoints, data sources, models, and usage instructions. It serves as a guide for using and understanding the application.

