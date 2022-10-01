## Importing Libraries
import pandas as pd
import numpy as np


# Loading data
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())


# Printing the number of rows and columns
print(len(diabetes_data))
print(len(diabetes_data.columns))


# Finding Dataframe Summary
print(diabetes_data.describe())


# Finding NUll Values
print(diabetes_data.isnull().sum())


# Replace NaN values with 0
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)


# Finding Null Values (2)
print(diabetes_data.isnull().sum())


# Finding rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])


# Finding data types
print(diabetes_data.info())


# Finding unique values of Outcome column
print(diabetes_data.Outcome.unique())
## Answer = ['1' '0' 'O']


# Replacing 'O' with '0' in the Outcome column
for index in range(0,len(diabetes_data["Outcome"])):
    string = str(diabetes_data["Outcome"].iat[index])
    replace = string.replace('O', '0')
    diabetes_data["Outcome"].iat[index] = replace
    
diabetes_data["Outcome"] = pd.to_numeric(diabetes_data["Outcome"])


# Finding unique values of Outcome column (2)
print(diabetes_data.Outcome.unique())
## Answer = ['1' '0']