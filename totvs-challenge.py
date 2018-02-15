#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:27:47 2018

@author: rafaelleite
"""

# Recurrent Neural Network



# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the training set
dataset_train = pd.read_csv('datasets/real_sales_train.csv')
training_set = dataset_train.iloc[:,0:2].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Creating a data structure with 7 timesteps and t+1 output
timesteps = 7
X_train = []
y_train = []
range_end = len(dataset_train)
for i in range(timesteps, range_end):
    X_train.append(training_set_scaled[i-timesteps:i])
    y_train.append(training_set_scaled[i])
X_train, y_train = np.array(X_train), np.array(y_train)

# Reshaping
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 2))

# Part 2 - Building the RNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

# Initialising the RNN
regressor = Sequential()

# Adding the input layer and the LSTM layer
regressor.add(LSTM(units = 300, input_shape = (timesteps, 2)))

# Adding the output layer
regressor.add(Dense(units = 2))

# Compiling the RNN
regressor.compile(optimizer = 'RMSprop', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, epochs = 50, batch_size = 1)

# Part 3 - Making the predictions and visualising the results

# Getting the real sales amounts
dataset_test = pd.read_csv('datasets/real_sales_test.csv')
test_set = dataset_test.iloc[:,0:2].values
faturamento_real = np.concatenate((training_set[0:range_end], test_set), axis = 0)

# Getting the predicted sales amounts
faturamento_real_escalado = sc.fit_transform(faturamento_real)
inputs = []
for i in range(range_end, 17):
    inputs.append(faturamento_real_escalado[i-timesteps:i])
inputs = np.array(inputs)
inputs = np.reshape(inputs, (inputs.shape[0], inputs.shape[1], 2))

predicted_sales_amount = regressor.predict(inputs)
predicted_sales_amount = sc.inverse_transform(predicted_sales_amount)

# Visualising the results
plt.plot(faturamento_real[range_end:,1], color = 'red', label = 'Real Sales Amount')
plt.plot(predicted_sales_amount[:,1], color = 'blue', label = 'Predicted Sales')
plt.title('Sales Forecast')
plt.xlabel('Time')
plt.ylabel('Sales Amount')
plt.legend()
plt.show()

# Part 4 - Forecast for the next 6 days

#creating array with the next 6 days forecasts
inputs_forecast = []
for i in range(range_end, 17):
    inputs_forecast.append(faturamento_real_escalado[i-timesteps:i])    
proximos_dias = np.array([    [[1,0.15863574],[0,0.32075725],[0.2,0.38609812],[0.4,0.63792434],[0.6,0.41116043],[0.8,0.05466487],[1,0.146379]],      
                              [[0,0.32075725],[0.2,0.38609812],[0.4,0.63792434],[0.6,0.41116043],[0.8,0.05466487],[1,0.146379], [0,0]],     
                              [[0.2,0.38609812],[0.4,0.63792434],[0.6,0.41116043],[0.8,0.05466487],[1,0.146379], [0,0], [0,0]],   
                              [[0.4,0.63792434],[0.6,0.41116043],[0.8,0.05466487],[1,0.146379], [0,0], [0,0], [0,0]] ,       
                              [[0.6,0.41116043],[0.8,0.05466487],[1,0.146379], [0,0], [0,0], [0,0], [0,0]],       
                              [[0.8,0.05466487],[1,0.146379], [0,0], [0,0], [0,0], [0,0], [0,0]]])
inputs_forecast = np.concatenate((inputs_forecast, proximos_dias))

forecast_sales_amount = regressor.predict(inputs_forecast)
forecast_sales_amount = sc.inverse_transform(forecast_sales_amount)

output = dataset_train
output = np.concatenate((output, forecast_sales_amount))


# Visualising the results
plt.plot(faturamento_real[0:,1], color = 'red', label = 'Real Sales Amount')
plt.plot(output[:,1], color = 'blue', label = 'Predicted Sales')
plt.title('Sales Forecast')
plt.xlabel('Time')
plt.ylabel('Sales Amount')
plt.legend()
plt.show()







