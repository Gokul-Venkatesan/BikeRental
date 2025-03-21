'''
The goal of this program is to identify patterns in weather-related variables (such as temperature, humidity, and wind speed) to predict rental prices
for various vehicles using machine learning, specifically the Linear Regression model

Working concept using Machine Learning, Linear Regression model, which is a supervised technique

Objective: By analyzing past data, the program identifies patterns or trends in how weather conditions affect rental prices,
which can then be used for forecasting future rental prices under similar conditions.

Gokul - 19-Mar-2025
updated with input capture from Angular and return the predictions back to UI, 20-Mar-2025
removed predictions to write to file and added a clause to show only positive number with basic validation for input variables, 21-Mar-2025
'''

from flask import Flask, request, jsonify #Flask to create web interface

from flask_cors import CORS  # <-- Import CORS, Cross-Origin Resource Sharing

import pickle
import pandas as pd #To interact with my CSV file
import numpy as np
from sklearn.linear_model import LinearRegression #Scikit-learn is used to train the model and make predictions

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load your trained model (assuming it's already created and saved)
model = pickle.load(open('model.pkl', 'rb'))

#Route for Flask to identify the service
@app.route('/BikeRental', methods=['POST'])

def BikeRental():
    try:
        if request.content_type != 'application/json':
            return jsonify({"error": "Unsupported Media Type. Please send data as application/json."}), 415

        if request.method == 'POST':
        # Get the data from the request
            data = request.get_json()
        elif request.method == 'GET':
            return jsonify({"message": "GET request received"})

        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Extract features (temperature, humidity, windspeed) from the request
        temperature = data['temperature']
        humidity = data['humidity']
        windspeed = data['windspeed']

        if temperature == 0 or temperature < 20 or temperature > 50:
            return jsonify({"error": "Invalid temperature data"}), 400

        if humidity == 0 or humidity < .05 or humidity > .25:
            return jsonify({"error": "Invalid humidity data"}), 400

        if windspeed == 0 or windspeed < 10 or windspeed > 20:
             return jsonify({"error": "Invalid windspeed data"}), 400
        
        if temperature is None or humidity is None or windspeed is None:
            return jsonify({"error": "Missing required data"}), 400

        # Prepare the input for the model (assuming a 2D array is expected)
        input_data = pd.DataFrame([[data['temperature'], data['humidity'], data['windspeed']]], 
                          columns=['temperature', 'humidity', 'windspeed']) #pass variables as dataframe

        # Make a prediction using the model
        predictions = model.predict(input_data)[0]
        predictions = round(predictions, 2)

        # Validate predictions for -ve value
        if predictions <= 0:
            predictions = 0

        # Return the prediction as a JSON response
        return jsonify({'predictions': predictions})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

