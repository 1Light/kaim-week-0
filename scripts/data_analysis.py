import pandas as pd

# Import load_data.py as a module
from load_data import load_and_clean_data

# Load and assign the cleaned data
benin_data, sierraleone_data, togo_data = load_and_clean_data()

# Generate summary statistics for each country's dataset (excluding the timestamp table)
benin_stats = benin_data.select_dtypes(include='number').describe()
sierraleone_stats = sierraleone_data.select_dtypes(include='number').describe()
togo_stats = togo_data.select_dtypes(include='number').describe()

# Drop the count row
benin_stats = benin_stats.drop('count')
sierraleone_stats = sierraleone_stats.drop('count')
togo_stats = togo_stats.drop('count')

# Display the summary statistics
print("Benin Summary Statistics:")
print(benin_stats)

print("\nSierraleone Summary Statistics:")
print(sierraleone_stats)

print("\nTogo Summary Statistics:")
print(togo_stats)

"""
# Save the summary statistics to CSV files
benin_stats.to_csv('../results/summary_stats/benin_summary_stats.csv', index=True)  
sierraleone_stats.to_csv('../results/summary_stats/sierraleone_summary_stats.csv', index=True)  
togo_stats.to_csv('../results/summary_stats/togo_summary_stats.csv', index=True)
"""