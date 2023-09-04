import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Initialize the Flask App
app = Flask(__name__)

# Load the trained models
linear_model = pickle.load(open('linear_model.pkl', 'rb'))
ridge_model = pickle.load(open('ridge_model.pkl', 'rb'))
lasso_model = pickle.load(open('lasso_model.pkl', 'rb'))
elastic_net_model = pickle.load(open('elastic_net_model.pkl', 'rb'))

# Default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

# To use the predict button in our web-app
@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # Predict using the Linear Regression model
    linear_prediction = linear_model.predict(final_features)

    # Predict using the Ridge Regression model
    ridge_prediction = ridge_model.predict(final_features)

    # Predict using the Lasso Regression model
    lasso_prediction = lasso_model.predict(final_features)

    # Predict using the Elastic Net Regression model
    elastic_net_prediction = elastic_net_model.predict(final_features)

    return render_template('index.html',
        linear_prediction='Linear Regression Prediction: {}'.format(round(linear_prediction[0], 2)),
        ridge_prediction='Ridge Regression Prediction: {}'.format(round(ridge_prediction[0], 2)),
        lasso_prediction='Lasso Regression Prediction: {}'.format(round(lasso_prediction[0], 2)),
        elastic_net_prediction='Elastic Net Regression Prediction: {}'.format(round(elastic_net_prediction[0], 2)))

if __name__ == "__main__":
    app.run(debug=True)