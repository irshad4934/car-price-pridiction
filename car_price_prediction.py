# -*- coding: utf-8 -*-
"""Car Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AXb8PWEMrAE5IijX3p-HuQ5N5J86TLcr

Importing the Dependencies
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

"""Data Collection and Processing"""

# loading the data from csv file to pandas dataframe
car_dataset = pd.read_csv('/content/car data.csv')

# inspecting the first 5 rows of the dataframe
car_dataset.head()

# checking the number of rows and columns
car_dataset.shape

# getting some information about the dataset
car_dataset.info()

# checking the number of missing values
car_dataset.isnull().sum()

# checking the distribution of categorical data
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())

"""Encoding the Categorical Data"""

# encoding "Fuel_Type" Column
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

# encoding "Seller_Type" Column
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# encoding "Transmission" Column
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

car_dataset.head()

"""Splitting the data and Target"""

X = car_dataset.drop(['Car_Name','Selling_Price'],axis=1)
Y = car_dataset['Selling_Price']

print(X)

print(Y)

"""Splitting Training and Test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state=2)

"""Model Training

1. Linear Regression
"""

# loading the linear regression model
lin_reg_model = LinearRegression()

lin_reg_model.fit(X_train,Y_train)

"""Model Evaluation"""

# prediction on Training data
training_data_prediction = lin_reg_model.predict(X_train)

# R squared Error
error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

"""Visualize the actual prices and Predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

# prediction on Training data
test_data_prediction = lin_reg_model.predict(X_test)

# R squared Error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

"""2. Lasso Regression"""

# loading the linear regression model
lass_reg_model = Lasso()

lass_reg_model.fit(X_train,Y_train)

"""Model Evaluation"""

# prediction on Training data
training_data_prediction = lass_reg_model.predict(X_train)

# R squared Error
error_score = metrics.r2_score(Y_train, training_data_prediction)
print("R squared Error : ", error_score)

"""Visualize the actual prices and Predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

# prediction on Training data
test_data_prediction = lass_reg_model.predict(X_test)

# R squared Error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared Error : ", error_score)

plt.scatter(Y_test, test_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(" Actual Prices vs Predicted Prices")
plt.show()

