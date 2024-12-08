import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Preprocess Data to Extract Temperature, Relative Humidity, and Solar Radiation
def preprocess_temp_data(data):
    data['Tamb'] = pd.to_numeric(data['Tamb'], errors='coerce')  # Use Tamb for Temperature
    data['RH'] = pd.to_numeric(data['RH'], errors='coerce')  # Relative Humidity
    data['GHI'] = pd.to_numeric(data['GHI'], errors='coerce')  # Use GHI for Solar Radiation
    
    # Drop rows with missing values
    data = data.dropna(subset=['Tamb', 'RH', 'GHI'])  # Drop rows if any of these are NaN
    
    return data

# 1. Scatter Plot: RH vs. Temperature (Tamb)
def plot_scatter_rh_temp(data, data_name, save_as):
    # Scatter plot for RH vs. Tamb (Temperature)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='RH', y='Tamb', color='b')
    plt.title(f'Relative Humidity vs. Temperature ({data_name})')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.tight_layout()
    plt.savefig(f"../results/temperature_analysis/{data_name}/{save_as}")
    plt.close()

# 2. Scatter Plot: RH vs. Solar Radiation (GHI)
def plot_scatter_rh_sr(data, data_name, save_as):
    # Scatter plot for RH vs. GHI (Solar Radiation)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='RH', y='GHI', color='g')
    plt.title(f'Relative Humidity vs. Solar Radiation ({data_name})')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Solar Radiation (W/m²)')
    plt.tight_layout()
    plt.savefig(f"../results/temperature_analysis/{data_name}/{save_as}")
    plt.close()

# 3. Correlation Matrix: RH, Temperature, and Solar Radiation
def plot_correlation_matrix(data, data_name, save_as):
    # Calculate the correlation matrix
    correlation_matrix = data[['RH', 'Tamb', 'GHI']].corr()
    
    # Plot the correlation matrix using a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix: RH, Temperature (Tamb), and Solar Radiation (GHI) ({data_name})')
    plt.tight_layout()
    plt.savefig(f"../results/temperature_analysis/{data_name}/{save_as}")
    plt.close()

# 4. Linear Regression: RH vs. Temperature (Tamb)
def plot_rh_vs_temp_regression(data, data_name, save_as):
    # Prepare the data
    X = data[['RH']]  # Independent variable (Relative Humidity)
    y = data['Tamb']  # Dependent variable (Temperature - Tamb)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Plot the regression line
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='RH', y='Tamb', color='b', label='Data points')
    plt.plot(data['RH'], model.predict(X), color='r', label='Regression line')
    plt.title(f'Linear Regression: RH vs. Temperature (Tamb) ({data_name})')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Temperature (°C)')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f"../results/temperature_analysis/{data_name}/{save_as}")
    plt.close()

# 5. Linear Regression: RH vs. Solar Radiation (GHI)
def plot_rh_vs_sr_regression(data, data_name, save_as):
    # Prepare the data
    X_sr = data[['RH']]  # Independent variable (Relative Humidity)
    y_sr = data['GHI']  # Dependent variable (Solar Radiation - GHI)

    # Create a linear regression model
    model_sr = LinearRegression()
    model_sr.fit(X_sr, y_sr)

    # Plot the regression line
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='RH', y='GHI', color='g', label='Data points')
    plt.plot(data['RH'], model_sr.predict(X_sr), color='r', label='Regression line')
    plt.title(f'Linear Regression: RH vs. Solar Radiation (GHI) ({data_name})')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Solar Radiation (W/m²)')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f"../results/temperature_analysis/{data_name}/{save_as}")
    plt.close()

########################### Temperature Analysis for Benin ###########################

data1 = preprocess_temp_data(benin_data)

# Plot Scatter Plot: RH vs. Temperature (Tamb)
plot_scatter_rh_temp(data1, 'benin', 'Benin_RH_vs_Temperature.png')

# Plot Scatter Plot: RH vs. Solar Radiation (GHI)
plot_scatter_rh_sr(data1, 'benin', 'Benin_RH_vs_Solar_Radiation.png')

# Plot Correlation Matrix for RH, Temperature (Tamb), and Solar Radiation (GHI)
plot_correlation_matrix(data1, 'benin', 'Benin_Correlation_Matrix.png')

# Plot Linear Regression for RH vs. Temperature (Tamb)
plot_rh_vs_temp_regression(data1, 'benin', 'Benin_RH_vs_Temperature_Regression.png')

# Plot Linear Regression for RH vs. Solar Radiation (GHI)
plot_rh_vs_sr_regression(data1, 'benin', 'Benin_RH_vs_Solar_Radiation_Regression.png')

########################### Temperature Analysis for Sierraleone ###########################

data2 = preprocess_temp_data(sierraleone_data)

# Plot Scatter Plot: RH vs. Temperature (Tamb)
plot_scatter_rh_temp(data2, 'sierraleone', 'Sierraleone_RH_vs_Temperature.png')

# Plot Scatter Plot: RH vs. Solar Radiation (GHI)
plot_scatter_rh_sr(data2, 'sierraleone', 'Sierraleone_RH_vs_Solar_Radiation.png')

# Plot Correlation Matrix for RH, Temperature (Tamb), and Solar Radiation (GHI)
plot_correlation_matrix(data2, 'sierraleone', 'Sierraleone_Correlation_Matrix.png')

# Plot Linear Regression for RH vs. Temperature (Tamb)
plot_rh_vs_temp_regression(data2, 'sierraleone', 'Sierraleone_RH_vs_Temperature_Regression.png')

# Plot Linear Regression for RH vs. Solar Radiation (GHI)
plot_rh_vs_sr_regression(data2, 'sierraleone', 'Sierraleone_RH_vs_Solar_Radiation_Regression.png')

########################### Temperature Analysis for Togo ###########################

data3 = preprocess_temp_data(togo_data)

# Plot Scatter Plot: RH vs. Temperature (Tamb)
plot_scatter_rh_temp(data3, 'togo', 'Togo_RH_vs_Temperature.png')

# Plot Scatter Plot: RH vs. Solar Radiation (GHI)
plot_scatter_rh_sr(data3, 'togo', 'Togo_RH_vs_Solar_Radiation.png')

# Plot Correlation Matrix for RH, Temperature (Tamb), and Solar Radiation (GHI)
plot_correlation_matrix(data3, 'togo', 'Togo_Correlation_Matrix.png')

# Plot Linear Regression for RH vs. Temperature (Tamb)
plot_rh_vs_temp_regression(data3, 'togo', 'Togo_RH_vs_Temperature_Regression.png')

# Plot Linear Regression for RH vs. Solar Radiation (GHI)
plot_rh_vs_sr_regression(data3, 'togo', 'Togo_RH_vs_Solar_Radiation_Regression.png')