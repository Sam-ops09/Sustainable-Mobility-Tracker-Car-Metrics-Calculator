# Sustainable-Mobility-Tracker

## Overview

This is a Flask web application that predicts fuel consumption and compares vehicle models based on CO2 emissions. It uses machine learning models to make predictions.

## Features

- Predicts fuel consumption using machine learning models.
- Compares vehicle models based on CO2 emissions.
- Visualizes data with line plots.

## File Structure

```
Directory structure:
└── Sam-ops09-Sustainable-Mobility-Tracker-Car-Metrics-Calculator/
    ├── neural_network_model.py
    ├── ridge_model.py
    ├── xgboost_model.pkl
    ├── Doc.md
    ├── elastic_net_model.py
    ├── .github/
    │   └── dependabot.yml
    ├── app.py
    ├── neural_network_model.pkl
    ├── Random_Forest_model.py
    ├── elastic_net_model.pkl
    ├── documentation.md
    ├── linear_model.py
    ├── FuelConsumption.csv
    ├── requirements.txt
    ├── ridge_model.pkl
    ├── XGBoost_model.py
    ├── random_forest_model.pkl
    ├── linear_model.pkl
    ├── Docs/
    │   ├── Final year/
    │   │   └── FIRST_review.pptx
    │   ├── Sustainable Mobility Tracker.docx
    │   ├── Final Review.pptx
    │   ├── Copy of Query_Response_Sheet-Batch_ID.xlsx
    │   ├── Minor project Report - Copy.docx
    │   └── Minor project Report.docx
    ├── README.md
    ├── templates/
    │   ├── index.html
    │   ├── graph.html
    │   └── compare.html
    ├── lasso_model.py
    ├── lasso_model.pkl
    └── static/
        └── css/
            ├── graph.css
            ├── compare.css
            └── style.css

```
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

# Fuel Consumption Prediction Web App

This Flask web application excels in predicting fuel consumption for vehicles through a well-structured codebase that emphasizes error rate reduction and accuracy improvement. The following key features contribute to enhanced performance across diverse machine learning models:

## Model Integration and Selection

The application integrates multiple machine learning models, each offering a unique approach to predicting fuel consumption. These models include:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net Regression
- Neural Network Models
- XGBoost
- Random Forest

### Dynamic Model Selection

The application dynamically selects the most suitable model for a given input, ensuring accuracy and minimizing error rates. The selection process involves comparing predictions from all models and choosing the one with the closest prediction to the actual value. This dynamic model selection mechanism significantly contributes to the overall accuracy of the predictions.

## Data Handling and Preprocessing

### Comprehensive Fuel Consumption Data

The application utilizes a comprehensive dataset ('FuelConsumption.csv') containing detailed information on various vehicle makes, models, and their corresponding fuel consumption values.

### Feature Extraction

The code efficiently extracts relevant features from user input, creating a representation suitable for model prediction. These features include engine size, cylinder count, and fuel consumption in the city.

## Code Structure

The code is organized into a modular and clear structure, promoting readability and maintainability. Key components include:

- **app.py**: The main script orchestrating the Flask web application, model loading, data preprocessing, and dynamic model selection.
- **Model Pickle Files**: Serialized models ('.pkl' files) containing pre-trained instances of various machine learning algorithms.
- **Templates Folder**: HTML templates ('index.html', 'compare.html', 'graph.html') for rendering user interfaces.
- **Static Folder**: Houses static files ('style.css', 'script.js') for enhancing the user interface.

## Continuous Improvement

The codebase welcomes contributions for further enhancement. Whether refining existing models, introducing new algorithms, or improving user interfaces, collaboration is encouraged to drive continuous improvement in prediction accuracy and error rate reduction.

## Conclusion

This Fuel Consumption Prediction Web App stands as a testament to the synergy between diverse machine learning models, thoughtful model selection, and robust data handling. The structured codebase ensures efficiency, accuracy, and a foundation for ongoing enhancements.

## Acknowledgments

- This project is for educational purposes.

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
