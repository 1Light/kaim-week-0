import pandas as pd

# Load the datasets
data1 = pd.read_csv('../data/benin-malanville.csv')
data2 = pd.read_csv('../data/sierraleone-bumbuna.csv')
data3 = pd.read_csv('../data/togo-dapaong_qc.csv')

# Let's print the first few rows of each data set to verify successful load
print(data1.head())
print(data2.head())
print(data3.head())