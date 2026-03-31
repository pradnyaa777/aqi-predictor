# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# step-1: load dataset
# this reads the CSV file into a DataFrame 
df = pd.read_csv("data/air_quality.csv")
print(df.head())


# check column names and data types
print(df.columns)
print(df.info())


# step-2: data cleaning
# remove rows with missing values
df = df.dropna()

# step-3: select features (inputs) and target (output)
# X= input features used for prediction
# y= target variables (what we want to predict)
X = df[["PM2.5","PM10","NO2","CO"]]
y = df["AQI"]


# step-4: split data into training and testing sets
# training set -> used to train the model 
# testing set -> used to evaluate   performance
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# step-5: train machine learning model (random forest)
# random forest is more powerful than linear regression for complex data 
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)


# step-6: feature importance
# shows which pollution factors impact AQI the most 
importances = model.feature_importances_

for i, col in enumerate(X.columns):
    print(col, importances[i])
    

# step-7: make predictions
y_pred = model.predict(X_test)

# show first few predictions
print("\nSample Predictions:")
print(y_pred[:10])


# step-8: evaluate model performance
# MAE = Mean absolute Error (the lower the better)
from sklearn.metrics import mean_absolute_error

error = mean_absolute_error(y_test, y_pred)
print("\nMAE:", error)


# step-9: visualization
# scatter plot comparing the actual vs predicted AQI 
plt.scatter(y_test, y_pred)


# reference line (perfect predictions)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')

plt.xlabel("Actual AQI")
plt.ylabel("Predicted AQI")
plt.title("Actual vs Predicted AQI")

plt.show()