# AQI Prediction using Machine Learning

## Overview
This project uses Machine Learning to predict the Air Quality Index (AQI) based on air pollution data.

The model learns relationships between pollutants like PM2.5, PM10, NO2, and CO to estimate AQI levels.

-----

## Objective
To build a predictive model that:
- Estimates AQI using historical pollution data
- Identifies which pollutants impact air quality the most

-----

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

-----

## Dataset
- Source: https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india
- File used: `air_quality.csv`

The dataset contains:
- Pollution metrics (PM2.5, PM10, NO2, CO, etc.)
- AQI values
- City and date information

-----

## How It Works

### 1. Data Cleaning
- Removed missing values using `dropna()`

### 2. Feature Selection
- Inputs: PM2.5, PM10, NO2, CO  
- Output: AQI  

### 3. Model Used
- Random Forest Regressor  

### 4. Training
- 80% training data  
- 20% testing data  

-----

## Results

- Mean Absolute Error (MAE): **16.28**

On average, the model predicts AQI within ~16 units of the actual value.

-----

## Key Insights

- PM2.5 has the highest impact on AQI (~83%)  
- PM10 contributes moderately  
- NO2 and CO have smaller effects  

-----

## Visualization

Below is a comparison of Actual vs Predicted AQI:

![AQI Prediction Graph](graph.png)

-----

## Future Improvements

- Add more features like temperature and humidity  
- Use deep learning models  
- Build a real-time AQI prediction web app  
- Integrate satellite data for better predictions  

-----

## Project Structure
aqi-predictor/
│── data/
│── main.py
│── README.md
│── graph.png


-----

## Acknowledgements

This project was built as part of a learning exercise by replicating existing machine learning approaches for AQI prediction.

Dataset source: Kaggle  
