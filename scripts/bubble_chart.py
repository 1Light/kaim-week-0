import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Preprocess Data
def preprocess_data_for_bubble_chart(data):
    data['GHI'] = pd.to_numeric(data['GHI'], errors='coerce')
    data['Tamb'] = pd.to_numeric(data['Tamb'], errors='coerce')
    data['WS'] = pd.to_numeric(data['WS'], errors='coerce')
    data['RH'] = pd.to_numeric(data['RH'], errors='coerce')
    
    # Drop rows with missing values in the variables of interest
    data = data.dropna(subset=['GHI', 'Tamb', 'WS', 'RH'])
    
    return data

# Bubble Chart: GHI vs. Tamb vs. WS with RH as bubble size
def plot_bubble_chart(data, data_name, save_as):
    # Preprocess data
    data = preprocess_data_for_bubble_chart(data)
    
    # Bubble chart plotting
    plt.figure(figsize=(10, 8))
    plt.scatter(data['GHI'], data['Tamb'], s=data['RH']*10, c=data['WS'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5)
    
    # Title and labels
    plt.title(f'Bubble Chart: GHI vs. Tamb vs. WS with RH as bubble size ({data_name})', fontsize=14)
    plt.xlabel('Global Horizontal Irradiance (GHI) (W/m²)', fontsize=12)
    plt.ylabel('Ambient Temperature (Tamb) (°C)', fontsize=12)
    
    # Colorbar for Wind Speed (WS)
    plt.colorbar(label='Wind Speed (WS) (m/s)')
    
    # Display the plot and save it
    plt.tight_layout()
    plt.savefig(f"../results/bubble_charts/{data_name}/{save_as}")
    plt.close()

########################### Bubble Chart for Benin ###########################
plot_bubble_chart(benin_data, 'benin', 'Benin_GHI_vs_Tamb_vs_WS_bubble_chart.png')

########################### Bubble Chart for Sierraleone ###########################
plot_bubble_chart(sierraleone_data, 'sierraleone', 'Sierraleone_GHI_vs_Tamb_vs_WS_bubble_chart.png')

########################### Bubble Chart for Togo ###########################
plot_bubble_chart(togo_data, 'togo', 'Togo_GHI_vs_Tamb_vs_WS_bubble_chart.png')
