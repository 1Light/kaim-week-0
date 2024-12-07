import pandas as pd

# Load the datasets
data1 = pd.read_csv('../data/benin-malanville.csv')
data2 = pd.read_csv('../data/sierraleone-bumbuna.csv')
data3 = pd.read_csv('../data/togo-dapaong_qc.csv')

"""
# Print the first few rows of each data set to verify successful load
print(data1.head())
print(data2.head())
print(data3.head()) """

# Change the data type of the timestamp column to pandas datetime object (datetime64[ns])
data1['Timestamp'] = pd.to_datetime(data1['Timestamp'])
data2['Timestamp'] = pd.to_datetime(data2['Timestamp'])
data3['Timestamp'] = pd.to_datetime(data3['Timestamp'])

"""
# Check the data types of the columns
print(data1.dtypes)
print(data2.dtypes)
print(data3.dtypes)

# Check for missing data
print(data1.isnull().sum())
print(data2.isnull().sum())
print(data3.isnull().sum())

Result: Comments column is empty.
"""

# Drop the 'Comments' column
data1.drop(columns=['Comments'], inplace=True)
data2.drop(columns=['Comments'], inplace=True)
data3.drop(columns=['Comments'], inplace=True)

print(data1.head())



