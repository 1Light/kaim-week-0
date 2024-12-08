import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# 1. Function to plot Correlation Matrix for Solar Radiation and Temperature
def plot_correlation_matrix(data, data_name, columns, title, save_as):
    correlation = data[columns].corr()  # Calculate the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"../results/correlation_analysis/{data_name}/{save_as}")
    plt.close()

# 2. Function to plot Pair Plot for Solar Radiation and Temperature
def plot_pair_plot(data, data_name, columns, title, save_as):
    sns.pairplot(data[columns])
    plt.suptitle(title, y=1.02)
    plt.tight_layout()
    plt.savefig(f"../results/correlation_analysis/{data_name}/{save_as}")
    plt.close()

# 3. Function to plot Scatter Matrix for Wind Conditions and Solar Irradiance
def plot_scatter_matrix(data, data_name, columns, title, save_as):
    sns.pairplot(data[columns], kind="scatter")
    plt.suptitle(title, y=1.02)
    plt.tight_layout()
    plt.savefig(f"../results/correlation_analysis/{data_name}/{save_as}")
    plt.close()

# Define the columns for analysis
solar_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB']
wind_columns = ['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']

########################### Correlation Analysis for Benin ###########################

# For Correlation Matrix (Solar Radiation vs Temperature)
plot_correlation_matrix(benin_data, "benin", solar_columns, 'Benin - Correlation Matrix (Solar Radiation & Temperature)', 'Benin_Correlation_Matrix.png')

# For Pair Plot (Solar Radiation vs Temperature)
plot_pair_plot(benin_data, "benin", solar_columns, 'Benin - Pair Plot (Solar Radiation & Temperature)', 'Benin_Pair_Plot.png')

# For Scatter Matrix (Wind Conditions vs Solar Irradiance)
plot_scatter_matrix(benin_data, "benin", wind_columns, 'Benin - Scatter Matrix (Wind Conditions & Solar Irradiance)', 'Benin_Scatter_Matrix.png')

########################### Correlation Analysis for Sierraleone ###########################

# For Correlation Matrix (Solar Radiation vs Temperature)
plot_correlation_matrix(sierraleone_data, "sierraleone", solar_columns, 'Sierraleone - Correlation Matrix (Solar Radiation & Temperature)', 'Sierraleone_Correlation_Matrix.png')

# For Pair Plot (Solar Radiation vs Temperature)
plot_pair_plot(sierraleone_data, "sierraleone", solar_columns, 'Sierraleone - Pair Plot (Solar Radiation & Temperature)', 'Sierraleone_Pair_Plot.png')

# For Scatter Matrix (Wind Conditions vs Solar Irradiance)
plot_scatter_matrix(sierraleone_data, "sierraleone", wind_columns, 'Sierraleone - Scatter Matrix (Wind Conditions & Solar Irradiance)', 'Sierraleone_Scatter_Matrix.png')

########################### Correlation Analysis for Togo ###########################

# For Correlation Matrix (Solar Radiation vs Temperature)
plot_correlation_matrix(togo_data, "togo", solar_columns, 'Togo - Correlation Matrix (Solar Radiation & Temperature)', 'Togo_Correlation_Matrix.png')

# For Pair Plot (Solar Radiation vs Temperature)
plot_pair_plot(togo_data, "togo", solar_columns, 'Togo - Pair Plot (Solar Radiation & Temperature)', 'Togo_Pair_Plot.png')

# For Scatter Matrix (Wind Conditions vs Solar Irradiance)
plot_scatter_matrix(togo_data, "togo", wind_columns, 'Togo - Scatter Matrix (Wind Conditions & Solar Irradiance)', 'Togo_Scatter_Matrix.png')
