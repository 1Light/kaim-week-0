# MoonLight Energy Solutions - Solar Energy Strategy Report

## Project Overview

**MoonLight Energy Solutions** aims to enhance its operational efficiency and sustainability through strategic solar investments. As an Analytics Engineer, the project involves analyzing environmental measurements from different locations to identify trends and insights that can guide the company’s solar installation strategy. This report covers the analysis of solar irradiance data from three regions: **Benin - Malanville**, **Sierra Leone - Bumbuna**, and **Togo - Dapaong QC**.

The main objectives of this project were:
- To analyze environmental data to identify key trends.
- To provide a data-driven recommendation for the best regions to invest in solar installations based on the analysis.
- To develop a dashboard using **Streamlit** for dynamic data visualization and interaction.

## Table of Contents

1. [Project Understanding](#project-understanding)
2. [Project Implementation](#project-implementation)
3. [Data Analysis & Insights](#data-analysis--insights)
4. [Dashboard Development](#dashboard-development)
5. [Results & Interpretation](#results--interpretation)
6. [Installation and Setup](#installation-and-setup)
7. [Contributions](#contributions)
8. [Licenses](#licenses)

## Project Understanding

This project focuses on providing insights from solar energy data to help MoonLight Energy Solutions choose optimal locations for solar panel installations. It involves a series of tasks, including:

1. **Data Quality Check**: Analyzing missing values, outliers, and incorrect entries in the dataset.
2. **Summary Statistics**: Calculating measures like mean, median, and standard deviation for solar radiation, temperature, and wind conditions.
3. **Time Series Analysis**: Observing patterns in solar irradiance and temperature over time.
4. **Correlation Analysis**: Identifying relationships between solar radiation and weather variables.
5. **Wind and Temperature Analysis**: Analyzing the impact of wind and temperature on solar irradiance.
6. **Data Cleaning**: Handling anomalies and missing values in the dataset.
7. **Dashboard Development**: Building an interactive dashboard using Streamlit for visualization and insights sharing.

## Project Implementation

### Steps Taken:

1. **Data Analysis**: 
   - The initial step was to clean the dataset by handling missing values and identifying outliers in columns like GHI, DNI, DHI, WS, and WSgust.
   - Next, summary statistics were calculated to understand data distribution and variability across the three locations: Malanville, Bumbuna, and Dapaong QC.
   
2. **Time Series and Correlation Analysis**:
   - Time series plots were used to examine trends in GHI, DNI, DHI, and temperature throughout the day and month.
   - Correlation matrices and pair plots were generated to visualize relationships between solar radiation and temperature, as well as wind conditions.

3. **Wind and Temperature Insights**:
   - Radial bar plots and wind roses helped visualize wind speed and direction patterns in each location.
   - Temperature analysis explored the relationship between relative humidity and temperature fluctuations.

4. **Dashboard Development**:
   - Streamlit was used to build an interactive dashboard that dynamically fetches and processes data, providing users with the ability to customize and explore different visualizations.

### Tools and Technologies Used:

- **Python**: For data analysis and statistical computations.
- **Streamlit**: For dashboard development and data visualization.
- **Pandas & NumPy**: For data manipulation and cleaning.
- **Matplotlib & Seaborn**: For data visualization (plots, histograms, pair plots, etc.).
- **VSCode**: For code development and initial analysis.

## Data Analysis & Insights

- **Summary Statistics**: Key statistical measures such as mean, median, and standard deviation were calculated for solar irradiance (GHI, DNI, DHI), temperature (TModA, TModB), and wind speed (WS, WSgust) for the three regions. This helped in understanding the data distribution and variability.
  
- **Time Series Analysis**: Observations about solar irradiance patterns across months and times of the day were made. Anomalies were noted, such as peaks in solar irradiance and temperature fluctuations in specific months.
  
- **Correlation Analysis**: It was found that solar radiation showed a significant correlation with temperature in some regions, while wind conditions had a lesser impact on solar irradiance but were important for temperature analysis.

- **Wind & Temperature Analysis**: Wind speed and direction were explored through radial bar plots and wind roses. Temperature and humidity were found to have a notable impact on solar radiation, with certain regions exhibiting more consistent solar irradiance.

## Dashboard Development

A dynamic **Streamlit dashboard** was developed to allow users to interact with the data and gain insights. Features included:
- **Interactive Sliders and Buttons**: Users can customize the visualizations by selecting specific variables and adjusting time ranges.
- **Dynamic Data Fetching**: The dashboard fetches and processes the data dynamically based on user input.
- **Visualization**: Key trends, such as solar radiation over time, wind speed distributions, and temperature correlations, are visualized interactively.

## Results & Interpretation

The analysis provided valuable insights into the potential for solar energy investments in each region:
- **Malanville (Benin)** exhibited high GHI values throughout the year, making it a prime location for solar installations.
- **Bumbuna (Sierra Leone)** showed fluctuations in solar radiation, with peaks observed during certain months, suggesting a need for more targeted installations.
- **Dapaong QC (Togo)** had a stable solar irradiance pattern, with moderate temperature and wind conditions, making it a viable region for year-round solar energy production.

## Installation and Setup

### Requirements:

- Python 3.x
- Pandas
- NumPy
- Gdown
- Matplotlib
- Seaborn
- Streamlit
- Windrose
- Scikit-learn

### Setup Instructions:

1. Clone the repository:
   ```bash
   git clone https://github.com/1Light/kaim-week-0.git
   cd kaim-week-0
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit dashboard:
   ```bash
   streamlit run app/main.py
   ```

4. Open the dashboard in your web browser and explore the interactive visualizations.

## Contributions

- **Data Cleaning and Preparation**: Identifying and handling missing data, outliers, and incorrect values.
- **Exploratory Data Analysis**: Conducted thorough analysis using statistical methods, correlation analysis, and time series plots.
- **Streamlit Dashboard**: Designed and developed an interactive dashboard to present the findings and provide an interactive user experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
