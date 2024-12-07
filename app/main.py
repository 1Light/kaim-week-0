import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

# Add the parent directory to the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.load_data import load_and_clean_data

# Load data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Function to preprocess data for Z-score analysis
def preprocess_data_for_zscore(data):
    data['Tamb'] = pd.to_numeric(data['Tamb'], errors='coerce')
    data['GHI'] = pd.to_numeric(data['GHI'], errors='coerce')
    data['WS'] = pd.to_numeric(data['WS'], errors='coerce')
    data['RH'] = pd.to_numeric(data['RH'], errors='coerce')
    data['BP'] = pd.to_numeric(data['BP'], errors='coerce')
    
    # Drop rows with missing values
    data = data.dropna(subset=['Tamb', 'GHI', 'WS', 'RH', 'BP'])
    
    return data

# Function to preprocess data for time series analysis
def preprocess_data(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data['Month'] = data['Timestamp'].dt.month
    data['Hour'] = data['Timestamp'].dt.hour
    return data

# Function to plot interactive histograms using Streamlit widgets
def interactive_histograms(data, variables):
    st.sidebar.subheader('Select Variable for Histogram')
    selected_var = st.sidebar.selectbox('Choose Variable', variables)

    st.write(f"**Histogram for {selected_var}**")
    plt.figure(figsize=(10, 6))
    sns.histplot(data[selected_var], kde=True, color='blue', bins=30)
    plt.title(f"Histogram of {selected_var}")
    plt.xlabel(selected_var)
    plt.ylabel("Frequency")
    st.pyplot(plt)
    plt.clf()  # Clear the figure to prevent overlap

# Function to plot time series analysis
def plot_time_series(data, column, title_prefix, ylabel):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Timestamp', y=column)
    plt.title(f"{title_prefix} - {column} Over Time")
    plt.xlabel('Time')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()  # Clear the figure to prevent overlap

def plot_by_month(data, column, title_prefix, ylabel):
    monthly_data = data.groupby('Month')[column].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(data=monthly_data, x='Month', y=column, palette='viridis')
    plt.title(f"{title_prefix} - {column} by Month")
    plt.xlabel('Month')
    plt.ylabel(ylabel)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

def plot_by_hour(data, column, title_prefix, ylabel):
    hourly_data = data.groupby('Hour')[column].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=hourly_data, x='Hour', y=column, marker='o')
    plt.title(f"{title_prefix} - {column} by Hour")
    plt.xlabel('Hour')
    plt.ylabel(ylabel)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to display summary statistics (updated)
def display_summary_statistics(data):
    st.write("**Summary Statistics**")
    
    # Select only numeric columns, excluding the timestamp or non-numeric columns
    numeric_data = data.select_dtypes(include='number')
    
    # Generate summary statistics, excluding the 'count' row and the timestamp column
    summary = numeric_data.describe().drop('count')
    
    st.write(summary)

# Function to plot correlation matrix
def plot_correlation_matrix(data, columns, title):
    correlation = data[columns].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
    plt.title(title)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot pair plot
def plot_pair_plot(data, columns, title):
    sns.pairplot(data[columns])
    plt.suptitle(title, y=1.02)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot scatter matrix
def plot_scatter_matrix(data, columns, title):
    sns.pairplot(data[columns], kind="scatter")
    plt.suptitle(title, y=1.02)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot wind speed distribution
def plot_wind_speed_distribution(data, title_prefix):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['WS'], kde=True, color='blue', bins=30)
    plt.title(f"{title_prefix} - Wind Speed Distribution")
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot wind direction distribution
def plot_wind_direction_distribution(data, title_prefix):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['WD'], kde=True, color='green', bins=30)
    plt.title(f"{title_prefix} - Wind Direction Distribution")
    plt.xlabel('Wind Direction (degrees)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot the temperature correlation matrix
def plot_correlation_matrix(data, data_name):
    # Calculate the correlation matrix
    correlation_matrix = data[['RH', 'Tamb', 'GHI']].corr()

    # Plot the correlation matrix using a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix: RH, Temperature (Tamb), and Solar Radiation (GHI) ({data_name})')
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

# Function to plot the rh vs sr regression
def plot_rh_vs_sr_regression(data, data_name):
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
    st.pyplot(plt)
    plt.clf()

# Function to plot the rh vs temp regression
def plot_rh_vs_temp_regression(data, data_name):
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
    st.pyplot(plt)
    plt.clf()

# Preprocess the data
benin_data_cleaned = preprocess_data_for_zscore(benin_data)
sierraleone_data_cleaned = preprocess_data_for_zscore(sierraleone_data)
togo_data_cleaned = preprocess_data_for_zscore(togo_data)

# Sidebar for dataset selection
st.sidebar.title('Dataset and Task Selection')
dataset = st.sidebar.selectbox('Select Dataset', ['Benin', 'Sierra Leone', 'Togo'])
task = st.sidebar.selectbox('Select Task', ['Histogram', 'Summary Statistics', 'Time Series Analysis', 'Correlation Analysis', 'Wind Analysis', 'Temperature Analysis'])

# Display appropriate data and visualizations based on dataset and task choice
if task == 'Histogram':
    if dataset == 'Benin':
        st.title('Benin Data Visualization - Histogram')
        interactive_histograms(benin_data_cleaned, ['GHI', 'Tamb', 'WS', 'RH', 'BP'])
    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone Data Visualization - Histogram')
        interactive_histograms(sierraleone_data_cleaned, ['GHI', 'Tamb', 'WS', 'RH', 'BP'])
    else:
        st.title('Togo Data Visualization - Histogram')
        interactive_histograms(togo_data_cleaned, ['GHI', 'Tamb', 'WS', 'RH', 'BP'])

# Preprocess the data for time series analysis
elif task == 'Time Series Analysis':
    if dataset == 'Benin':
        st.title('Benin Data - Time Series Analysis')
        benin_data_cleaned = preprocess_data(benin_data)
        
        # Dropdown to select time series plot type
        time_series_type = st.sidebar.selectbox(
            'Select Time Series Analysis Type',
            ['Over Time', 'By Month', 'By Hour']
        )

        if time_series_type == 'Over Time':
            plot_time_series(benin_data_cleaned, 'GHI', 'Benin', 'GHI (W/m^2)')
        elif time_series_type == 'By Month':
            plot_by_month(benin_data_cleaned, 'GHI', 'Benin', 'GHI (W/m^2)')
        else:
            plot_by_hour(benin_data_cleaned, 'GHI', 'Benin', 'GHI (W/m^2)')

    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone Data - Time Series Analysis')
        sierraleone_data_cleaned = preprocess_data(sierraleone_data)
        
        # Dropdown to select time series plot type
        time_series_type = st.sidebar.selectbox(
            'Select Time Series Analysis Type',
            ['Over Time', 'By Month', 'By Hour']
        )

        if time_series_type == 'Over Time':
            plot_time_series(sierraleone_data_cleaned, 'GHI', 'Sierra Leone', 'GHI (W/m^2)')
        elif time_series_type == 'By Month':
            plot_by_month(sierraleone_data_cleaned, 'GHI', 'Sierra Leone', 'GHI (W/m^2)')
        else:
            plot_by_hour(sierraleone_data_cleaned, 'GHI', 'Sierra Leone', 'GHI (W/m^2)')

    else:
        st.title('Togo Data - Time Series Analysis')
        togo_data_cleaned = preprocess_data(togo_data)
        
        # Dropdown to select time series plot type
        time_series_type = st.sidebar.selectbox(
            'Select Time Series Analysis Type',
            ['Over Time', 'By Month', 'By Hour']
        )

        if time_series_type == 'Over Time':
            plot_time_series(togo_data_cleaned, 'GHI', 'Togo', 'GHI (W/m^2)')
        elif time_series_type == 'By Month':
            plot_by_month(togo_data_cleaned, 'GHI', 'Togo', 'GHI (W/m^2)')
        else:
            plot_by_hour(togo_data_cleaned, 'GHI', 'Togo', 'GHI (W/m^2)')

# Display summary statistics
elif task == 'Summary Statistics':
    if dataset == 'Benin':
        st.title('Benin Data Summary Statistics')
        display_summary_statistics(benin_data_cleaned)
    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone Data Summary Statistics')
        display_summary_statistics(sierraleone_data_cleaned)
    else:
        st.title('Togo Data Summary Statistics')
        display_summary_statistics(togo_data_cleaned)

# Display correlation analysis
elif task == 'Correlation Analysis':
    if dataset == 'Benin':
        st.title('Benin - Correlation Analysis')
        
        # Dropdown to select which plot to display
        correlation_plot_type = st.sidebar.selectbox(
            'Select Correlation Plot Type',
            ['Correlation Matrix', 'Pair Plot', 'Scatter Matrix']
        )

        if correlation_plot_type == 'Correlation Matrix':
            plot_correlation_matrix(benin_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Benin - Correlation Matrix (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Pair Plot':
            plot_pair_plot(benin_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Benin - Pair Plot (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Scatter Matrix':
            plot_scatter_matrix(benin_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Benin - Scatter Matrix (Solar Radiation & Temperature)')

    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone - Correlation Analysis')
        
        # Dropdown to select which plot to display
        correlation_plot_type = st.sidebar.selectbox(
            'Select Correlation Plot Type',
            ['Correlation Matrix', 'Pair Plot', 'Scatter Matrix']
        )

        if correlation_plot_type == 'Correlation Matrix':
            plot_correlation_matrix(sierraleone_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Sierra Leone - Correlation Matrix (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Pair Plot':
            plot_pair_plot(sierraleone_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Sierra Leone - Pair Plot (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Scatter Matrix':
            plot_scatter_matrix(sierraleone_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Sierra Leone - Scatter Matrix (Solar Radiation & Temperature)')

    else:
        st.title('Togo - Correlation Analysis')
        
        # Dropdown to select which plot to display
        correlation_plot_type = st.sidebar.selectbox(
            'Select Correlation Plot Type',
            ['Correlation Matrix', 'Pair Plot', 'Scatter Matrix']
        )

        if correlation_plot_type == 'Correlation Matrix':
            plot_correlation_matrix(togo_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Togo - Correlation Matrix (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Pair Plot':
            plot_pair_plot(togo_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Togo - Pair Plot (Solar Radiation & Temperature)')
        elif correlation_plot_type == 'Scatter Matrix':
            plot_scatter_matrix(togo_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Togo - Scatter Matrix (Solar Radiation & Temperature)')

# Display wind analysis
elif task == 'Wind Analysis':
    if dataset == 'Benin':
        st.title('Benin - Wind Analysis')
        
        # Dropdown to select wind analysis type
        wind_analysis_type = st.sidebar.selectbox(
            'Select Wind Analysis Type',
            ['Wind Speed Distribution', 'Wind Direction Distribution']
        )

        if wind_analysis_type == 'Wind Speed Distribution':
            plot_wind_speed_distribution(benin_data_cleaned, 'Benin')
        elif wind_analysis_type == 'Wind Direction Distribution':
            plot_wind_direction_distribution(benin_data_cleaned, 'Benin')

    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone - Wind Analysis')
        
        # Dropdown to select wind analysis type
        wind_analysis_type = st.sidebar.selectbox(
            'Select Wind Analysis Type',
            ['Wind Speed Distribution', 'Wind Direction Distribution']
        )

        if wind_analysis_type == 'Wind Speed Distribution':
            plot_wind_speed_distribution(sierraleone_data_cleaned, 'Sierra Leone')
        elif wind_analysis_type == 'Wind Direction Distribution':
            plot_wind_direction_distribution(sierraleone_data_cleaned, 'Sierra Leone')

    else:
        st.title('Togo - Wind Analysis')
        
        # Dropdown to select wind analysis type
        wind_analysis_type = st.sidebar.selectbox(
            'Select Wind Analysis Type',
            ['Wind Speed Distribution', 'Wind Direction Distribution']
        )

        if wind_analysis_type == 'Wind Speed Distribution':
            plot_wind_speed_distribution(togo_data_cleaned, 'Togo')
        elif wind_analysis_type == 'Wind Direction Distribution':
            plot_wind_direction_distribution(togo_data_cleaned, 'Togo')

# Temperature Analysis
elif task == 'Temperature Analysis':
    if dataset == 'Benin':
        st.title('Benin - Temperature Analysis')
        
        # Dropdown to select temperature analysis type
        temp_analysis_type = st.sidebar.selectbox(
            'Select Temperature Analysis Type',
            ['Correlation Matrix', 'RH vs Solar Radiation Regression', 'RH vs Temperature Regression']
        )

        if temp_analysis_type == 'Correlation Matrix':
            plot_correlation_matrix(benin_data_cleaned, 'Benin')
        elif temp_analysis_type == 'RH vs Solar Radiation Regression':
            plot_rh_vs_sr_regression(benin_data_cleaned, 'Benin')
        elif temp_analysis_type == 'RH vs Temperature Regression':
            plot_rh_vs_temp_regression(benin_data_cleaned, 'Benin')

    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone - Temperature Analysis')
        
        # Dropdown to select temperature analysis type
        temp_analysis_type = st.sidebar.selectbox(
            'Select Temperature Analysis Type',
            ['Correlation Matrix', 'RH vs Solar Radiation Regression', 'RH vs Temperature Regression']
        )

        if temp_analysis_type == 'Correlation Matrix':
            plot_correlation_matrix(sierraleone_data_cleaned, 'Sierra Leone')
        elif temp_analysis_type == 'RH vs Solar Radiation Regression':
            plot_rh_vs_sr_regression(sierraleone_data_cleaned, 'Sierra Leone')
        elif temp_analysis_type == 'RH vs Temperature Regression':
            plot_rh_vs_temp_regression(sierraleone_data_cleaned, 'Sierra Leone')

    else:
        st.title('Togo - Temperature Analysis')
        
        # Dropdown to select temperature analysis type
        temp_analysis_type = st.sidebar.selectbox(
            'Select Temperature Analysis Type',
            ['Correlation Matrix', 'RH vs Solar Radiation Regression', 'RH vs Temperature Regression']
        )

        if temp_analysis_type == 'Correlation Matrix':
            plot_correlation_matrix(togo_data_cleaned, 'Togo')
        elif temp_analysis_type == 'RH vs Solar Radiation Regression':
            plot_rh_vs_sr_regression(togo_data_cleaned, 'Togo')
        elif temp_analysis_type == 'RH vs Temperature Regression':
            plot_rh_vs_temp_regression(togo_data_cleaned, 'Togo')


