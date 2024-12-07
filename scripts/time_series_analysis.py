import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Extract the month and hour from the timestamp column
def preprocess_data(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data['Month'] = data['Timestamp'].dt.month
    data['Hour'] = data['Timestamp'].dt.hour
    return data

# Plot Functions
def plot_time_series(data, column, title_prefix, ylabel, save_as):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Timestamp', y=column)
    plt.title(f"{title_prefix} - {column} Over Time")
    plt.xlabel('Time')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"../results/time_series_analysis/{title_prefix}/{save_as}")
    plt.close()

def plot_by_month(data, column, title_prefix, ylabel, save_as):
    monthly_data = data.groupby('Month')[column].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(data=monthly_data, x='Month', y=column, palette='viridis')
    plt.title(f"{title_prefix} - {column} by Month")
    plt.xlabel('Month')
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"../results/time_series_analysis/{title_prefix}/{save_as}")
    plt.close()

def plot_by_hour(data, column, title_prefix, ylabel, save_as):
    hourly_data = data.groupby('Hour')[column].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=hourly_data, x='Hour', y=column, marker='o')
    plt.title(f"{title_prefix} - {column} by Hour")
    plt.xlabel('Hour')
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"../results/time_series_analysis/{title_prefix}/{save_as}")
    plt.close()

def evaluate_cleaning_impact(data, sensor_columns, dataset_name, save_as):
    for sensor in sensor_columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=data, x='Cleaning', y=sensor)
        plt.title(f'Impact of Cleaning on {sensor} ({dataset_name})')
        plt.xlabel('Cleaning (0 = No, 1 = Yes)')
        plt.ylabel(sensor)
        plt.tight_layout()
        plt.savefig(f"../results/time_series_analysis/{dataset_name}/{save_as}_{sensor}_cleaning_impact.png") 
        plt.close()

# Aggregate and Plot for Each Dataset
def process_and_plot(data, dataset_name):
    processed_data = preprocess_data(data)
    
    # Plot Time Series
    plot_time_series(processed_data, 'GHI', dataset_name, 'GHI (W/m^2)', f"{dataset_name}_GHI_Time_Series.png")
    plot_time_series(processed_data, 'Tamb', dataset_name, 'Temperature (°C)', f"{dataset_name}_Tamb_Time_Series.png")
    plot_time_series(processed_data, 'DHI', dataset_name, 'DHI (W/m^2)', f"{dataset_name}_DHI_Time_Series.png")
    plot_time_series(processed_data, 'DNI', dataset_name, 'DNI (W/m^2)', f"{dataset_name}_DNI_Time_Series.png")
    
    # Plot by Month
    plot_by_month(processed_data, 'GHI', dataset_name, 'GHI (W/m^2)', f"{dataset_name}_GHI_by_Month.png")
    plot_by_month(processed_data, 'Tamb', dataset_name, 'Temperature (°C)', f"{dataset_name}_Tamb_by_Month.png")
    plot_by_month(processed_data, 'DHI', dataset_name, 'DHI (W/m^2)', f"{dataset_name}_DHI_by_Month.png")
    plot_by_month(processed_data, 'DNI', dataset_name, 'DNI (W/m^2)', f"{dataset_name}_DNI_by_Month.png")
    
    # Plot by Hour
    plot_by_hour(processed_data, 'GHI', dataset_name, 'GHI (W/m^2)', f"{dataset_name}_GHI_by_Hour.png")
    plot_by_hour(processed_data, 'Tamb', dataset_name, 'Temperature (°C)', f"{dataset_name}_Tamb_by_Hour.png")
    plot_by_hour(processed_data, 'DHI', dataset_name, 'DHI (W/m^2)', f"{dataset_name}_DHI_by_Hour.png")
    plot_by_hour(processed_data, 'DNI', dataset_name, 'DNI (W/m^2)', f"{dataset_name}_DNI_by_Hour.png")
    
    # Evaluate Cleaning Impact
    evaluate_cleaning_impact(processed_data, ['ModA', 'ModB'], dataset_name, dataset_name)

"""
# Process and Plot for Benin, Sierra Leone, and Togo
process_and_plot(benin_data, 'benin')
process_and_plot(sierraleone_data, 'sierraLeone')
process_and_plot(togo_data, 'togo')
"""