import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Preprocess Data to Extract Wind Speed and Wind Direction
def preprocess_wind_data(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data['Hour'] = data['Timestamp'].dt.hour
    return data

# 1. Radial Bar Plot for Wind Speed (WS and WSgust)
def plot_radial_bar_wind_speed(data, data_name, save_as):
    # Plot Wind Speed Distribution using Radial Bar Plot
    plt.figure(figsize=(8, 6))
    sns.histplot(data['WS'], kde=True, color='b', label='Wind Speed (WS)', bins=30)
    plt.title('Wind Speed Distribution')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"../results/wind_analysis/{data_name}/{save_as}")
    plt.close()

def plot_wind_rose(data, data_name, save_as):
    # Plot Wind Rose for Wind Direction (WD)
    ax = WindroseAxes.from_ax()
    
    wind_data = data['WD']
    wind_speed = data['WS'] 
    
    # Create the wind rose plot without specifying color
    ax.bar(wind_data, wind_speed, bins=12, normed=True, opening=0.8, edgecolor='white')
    
    plt.title('Wind Rose (Wind Direction Distribution)')
    plt.savefig(f"../results/wind_analysis/{data_name}/{save_as}")
    plt.close()


########################### Wind Analysis for Benin ###########################

data1 = preprocess_wind_data(benin_data)

# Plot Radial Bar Plot for Wind Speed
plot_radial_bar_wind_speed(data1, 'benin', 'Benin_Wind_Speed_Distribution.png')

# Plot Wind Rose for Wind Direction
plot_wind_rose(data1, 'benin', 'Benin_Wind_Rose.png')

########################### Wind Analysis for Sierraleone ###########################

data2 = preprocess_wind_data(sierraleone_data)

# Plot Radial Bar Plot for Wind Speed
plot_radial_bar_wind_speed(data2, 'sierraleone', 'Sierraleone_Wind_Speed_Distribution.png')

# Plot Wind Rose for Wind Direction
plot_wind_rose(data2, 'sierraleone', 'Sierraleone_Wind_Rose.png')

########################### Wind Analysis for Togo ###########################

data3 = preprocess_wind_data(togo_data)

# Plot Radial Bar Plot for Wind Speed
plot_radial_bar_wind_speed(data3, 'togo', 'Togo_Wind_Speed_Distribution.png')

# Plot Wind Rose for Wind Direction
plot_wind_rose(data3, 'togo', 'Togo_Wind_Rose.png')
