import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Preprocess Data to Extract Relevant Variables
def preprocess_data(data):
    data['GHI'] = pd.to_numeric(data['GHI'], errors='coerce')
    data['DNI'] = pd.to_numeric(data['DNI'], errors='coerce')
    data['DHI'] = pd.to_numeric(data['DHI'], errors='coerce')
    data['WS'] = pd.to_numeric(data['WS'], errors='coerce')
    data['Tamb'] = pd.to_numeric(data['Tamb'], errors='coerce')

    # Drop rows with missing values
    data = data.dropna(subset=['GHI', 'DNI', 'DHI', 'WS', 'Tamb'])
    return data

# Function to plot histograms for different variables
def plot_histogram(data, variable, data_name, save_as):
    plt.figure(figsize=(8, 6))
    sns.histplot(data[variable], kde=True, bins=30)
    plt.title(f'Histogram of {variable} ({data_name})')
    plt.xlabel(variable)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"../results/histograms/{data_name}/{save_as}")
    plt.close()

# ########################### Histograms for Benin ###########################

data1 = preprocess_data(benin_data)

# Plot Histograms for each variable
plot_histogram(data1, 'GHI', 'benin', 'Benin_GHI_Histogram.png')
plot_histogram(data1, 'DNI', 'benin', 'Benin_DNI_Histogram.png')
plot_histogram(data1, 'DHI', 'benin', 'Benin_DHI_Histogram.png')
plot_histogram(data1, 'WS', 'benin', 'Benin_WS_Histogram.png')
plot_histogram(data1, 'Tamb', 'benin', 'Benin_Tamb_Histogram.png')

# ########################### Histograms for Sierraleone ###########################

data2 = preprocess_data(sierraleone_data)

# Plot Histograms for each variable
plot_histogram(data2, 'GHI', 'sierraleone', 'Sierraleone_GHI_Histogram.png')
plot_histogram(data2, 'DNI', 'sierraleone', 'Sierraleone_DNI_Histogram.png')
plot_histogram(data2, 'DHI', 'sierraleone', 'Sierraleone_DHI_Histogram.png')
plot_histogram(data2, 'WS', 'sierraleone', 'Sierraleone_WS_Histogram.png')
plot_histogram(data2, 'Tamb', 'sierraleone', 'Sierraleone_Tamb_Histogram.png')

# ########################### Histograms for Togo ###########################

data3 = preprocess_data(togo_data)

# Plot Histograms for each variable
plot_histogram(data3, 'GHI', 'togo', 'Togo_GHI_Histogram.png')
plot_histogram(data3, 'DNI', 'togo', 'Togo_DNI_Histogram.png')
plot_histogram(data3, 'DHI', 'togo', 'Togo_DHI_Histogram.png')
plot_histogram(data3, 'WS', 'togo', 'Togo_WS_Histogram.png')
plot_histogram(data3, 'Tamb', 'togo', 'Togo_Tamb_Histogram.png')