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

import pickle
import pandas as pd #To interact with my CSV file
import numpy as np
from sklearn.linear_model import LinearRegression #Scikit-learn is used to train the model and make predictions

#Function that reads the excel file, analyze the input variables to predict the rental based on training data

#Load your dataset
df = pd.read_csv('bikes.csv')

#Prepare your input features (X) and target (y)
# Assuming the dataset has 'X' as the independent variable and 'Y' as the target variable

#Multiple Inputs
X = df[['temperature','humidity','windspeed']]

y = df['rentals']    # Target

#Initialize the model and train it
model = LinearRegression()
model.fit(X, y)

# Save the model
with open('Model.pkl', 'wb') as file:
    pickle.dump(model, file)
