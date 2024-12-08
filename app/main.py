import sys
import os
import streamlit as st
from utils import preprocess_data_for_zscore, display_summary_statistics, preprocess_data, interactive_histograms, plot_time_series, plot_by_month, plot_by_hour, plot_tamb_correlation_matrix, plot_pair_plot, plot_scatter_matrix, plot_wind_speed_distribution, plot_wind_direction_distribution, plot_correlation_matrix, plot_rh_vs_sr_regression, plot_rh_vs_temp_regression

# Add the parent directory to the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.load_data import load_and_clean_data

# Load data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Preprocess the data
benin_data_cleaned = preprocess_data_for_zscore(benin_data)
sierraleone_data_cleaned = preprocess_data_for_zscore(sierraleone_data)
togo_data_cleaned = preprocess_data_for_zscore(togo_data)

# Sidebar for dataset selection
st.sidebar.title('Dataset and Task Selection')
dataset = st.sidebar.selectbox('Select Dataset', ['Benin', 'Sierra Leone', 'Togo'])
task = st.sidebar.selectbox('Select Task', ['Histogram', 'Summary Statistics', 'Time Series Analysis', 'Correlation Analysis', 'Wind Analysis', 'Temperature Analysis'])

# Display summary statistics
if task == 'Summary Statistics':
    if dataset == 'Benin':
        st.title('Benin Data Summary Statistics')
        display_summary_statistics(benin_data_cleaned)
    elif dataset == 'Sierra Leone':
        st.title('Sierra Leone Data Summary Statistics')
        display_summary_statistics(sierraleone_data_cleaned)
    else:
        st.title('Togo Data Summary Statistics')
        display_summary_statistics(togo_data_cleaned)

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
            plot_tamb_correlation_matrix(benin_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Benin - Correlation Matrix (Solar Radiation & Temperature)')
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
            plot_tamb_correlation_matrix(sierraleone_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Sierra Leone - Correlation Matrix (Solar Radiation & Temperature)')
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
            plot_tamb_correlation_matrix(togo_data_cleaned, ['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], 'Togo - Correlation Matrix (Solar Radiation & Temperature)')
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

