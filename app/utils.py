import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

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
def plot_tamb_correlation_matrix(data, columns, title):
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



