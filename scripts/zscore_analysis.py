import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'load_data.py' is imported to load the cleaned data
from load_data import load_and_clean_data

# Load data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Function to preprocess data for Z-Score analysis
def preprocess_data_for_zscore(data):
    data['Tamb'] = pd.to_numeric(data['Tamb'], errors='coerce')
    data['GHI'] = pd.to_numeric(data['GHI'], errors='coerce')
    data['WS'] = pd.to_numeric(data['WS'], errors='coerce')
    data['RH'] = pd.to_numeric(data['RH'], errors='coerce')
    data['BP'] = pd.to_numeric(data['BP'], errors='coerce')
    
    # Drop rows with missing values
    data = data.dropna(subset=['Tamb', 'GHI', 'WS', 'RH', 'BP'])
    
    return data

# Function to calculate Z-scores
def calculate_z_scores(data, variables):
    z_scores = {}
    
    for var in variables:
        mean = data[var].mean()
        std_dev = data[var].std()
        z_scores[var] = (data[var] - mean) / std_dev
    
    return pd.DataFrame(z_scores)

# Function to identify outliers based on Z-scores (Z > 3 or Z < -3)
def identify_outliers(z_scores_df):
    outliers = {}
    for column in z_scores_df.columns:
        outliers[column] = z_scores_df[(z_scores_df[column] > 3) | (z_scores_df[column] < -3)]
    return outliers

# Function to plot Z-scores for visualization and save as image
def plot_z_scores(z_scores_df, data_name, save_as):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=z_scores_df)
    plt.title(f'Z-Scores Distribution ({data_name})')
    plt.tight_layout()
    plt.savefig(f"../results/zscore_analysis/{data_name}/{save_as}")
    plt.close()

# Preprocess data for Z-score analysis for each dataset
benin_data_cleaned = preprocess_data_for_zscore(benin_data)
sierraleone_data_cleaned = preprocess_data_for_zscore(sierraleone_data)
togo_data_cleaned = preprocess_data_for_zscore(togo_data)

# Calculate Z-scores for the relevant variables
variables_of_interest = ['Tamb', 'GHI', 'WS', 'RH', 'BP']
benin_z_scores = calculate_z_scores(benin_data_cleaned, variables_of_interest)
sierraleone_z_scores = calculate_z_scores(sierraleone_data_cleaned, variables_of_interest)
togo_z_scores = calculate_z_scores(togo_data_cleaned, variables_of_interest)

# Identify outliers for each dataset
benin_outliers = identify_outliers(benin_z_scores)
sierraleone_outliers = identify_outliers(sierraleone_z_scores)
togo_outliers = identify_outliers(togo_z_scores)

# Plot Z-scores and save them as images for each dataset
plot_z_scores(benin_z_scores, 'benin', 'Benin_Zscore_Distribution.png')
plot_z_scores(sierraleone_z_scores, 'sierraleone', 'Sierraleone_Zscore_Distribution.png')
plot_z_scores(togo_z_scores, 'togo', 'Togo_Zscore_Distribution.png')

# Optionally, you can also print or return the outliers for further analysis
print("Benin Outliers:", benin_outliers)
print("Sierraleone Outliers:", sierraleone_outliers)
print("Togo Outliers:", togo_outliers)