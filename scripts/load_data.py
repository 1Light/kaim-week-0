import gdown
import pandas as pd
import os

def download_from_gdrive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

def load_and_clean_data():

    file_ids = {
        "benin": "1fpqN0RjgTaXGcz-LoueOy0nlvGa_BbWV",  
        "sierraleone": "1uV5DbK2XOHdzYZewJw31nxSuFuOCOZ9B",  
        "togo": "1UFoqU5jN6OYt64Fy0kpFYrzj3pITXMQR"  
    }

    # Define local paths to save the data temporarily
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'temp_data'))
    os.makedirs(base_path, exist_ok=True)  
    
    # Define file paths for each dataset
    benin_path = os.path.join(base_path, 'benin-malanville.csv')
    sierraleone_path = os.path.join(base_path, 'sierraleone-bumbuna.csv')
    togo_path = os.path.join(base_path, 'togo-dapaong_qc.csv')

    # Download files only if they don't exist
    if not os.path.exists(benin_path):
        print("Downloading Benin data...")
        download_from_gdrive(file_ids["benin"], benin_path)

    if not os.path.exists(sierraleone_path):
        print("Downloading Sierra Leone data...")
        download_from_gdrive(file_ids["sierraleone"], sierraleone_path)

    if not os.path.exists(togo_path):
        print("Downloading Togo data...")
        download_from_gdrive(file_ids["togo"], togo_path)
    
    # Load the data (after confirming they are downloaded)
    data1 = pd.read_csv(benin_path)
    data2 = pd.read_csv(sierraleone_path)
    data3 = pd.read_csv(togo_path)

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

    Result: The column called 'Comments' is empty.
    """

    # Drop the 'Comments' column
    data1.drop(columns=['Comments'], inplace=True)
    data2.drop(columns=['Comments'], inplace=True)
    data3.drop(columns=['Comments'], inplace=True)

    # Define a function to check for negative values and outliers
    def check_negative_and_outliers(data, column, expected_range=None):
        # Define a list of columns where negative values are acceptable
        valid_negative_columns = ['Tamb', 'TModA', 'TModB']

        # Check for negative values only if the column is not in the valid list
        if column not in valid_negative_columns and (data[column] < 0).any():
            print(f"Negative values found in {column}. Converting to positive.")
            data[column] = data[column].abs()

        # Check for outliers using IQR (Interquartile Range) method, if no expected range is provided
        if expected_range is None:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

            if not outliers.empty:
                print(f"Outliers found in {column}. Replacing with capped values.")
                # For other columns, replace outliers by capping them at the threshold
                data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)
                print(f"Outliers in {column} replaced with capped values.")

        else:
            # Check for values outside the expected range
            lower_bound, upper_bound = expected_range
            outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]

            if not outliers.empty:
                print(f"Values outside expected range found in {column}. Replacing with capped values.")

                # Special handling for the 'Cleaning' column (binary data: 0 or 1)
                if column == 'Cleaning':
                    # Handle case when there is no mode in 'Cleaning' (e.g., if all values are outliers)
                    if data[column].mode().empty:
                        print(f"No mode found for {column}, handling outliers differently.")
                        # Use threshold for outliers in 'Cleaning'
                        data.loc[outliers.index, column] = 0  # or any default value (0 or 1)
                        print(f"Outliers in {column} replaced with default value 0.")
                    else:
                        mode_value = data[column].mode()[0]  # Get the most frequent value (mode)
                        data.loc[outliers.index, column] = mode_value
                        print(f"Outliers in {column} replaced with mode value {mode_value}.")
                else:
                    # For other columns, replace outliers by capping them at the threshold
                    data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)
                    print(f"Outliers in {column} replaced with capped values.")

    # Apply checks to all relevant columns in each dataset
    print("Applying checks for data1")
    check_negative_and_outliers(data1, 'GHI')
    check_negative_and_outliers(data1, 'DNI')
    check_negative_and_outliers(data1, 'DHI')
    check_negative_and_outliers(data1, 'ModA')
    check_negative_and_outliers(data1, 'ModB')
    check_negative_and_outliers(data1, 'Tamb')
    check_negative_and_outliers(data1, 'RH', expected_range=(0, 100))
    check_negative_and_outliers(data1, 'WS')
    check_negative_and_outliers(data1, 'WSgust')
    check_negative_and_outliers(data1, 'WSstdev')
    check_negative_and_outliers(data1, 'WD', expected_range=(0, 360))
    check_negative_and_outliers(data1, 'WDstdev')
    check_negative_and_outliers(data1, 'BP', expected_range=(900, 1050))
    check_negative_and_outliers(data1, 'Cleaning', expected_range=(0, 1))
    check_negative_and_outliers(data1, 'Precipitation', expected_range=(0, None))
    check_negative_and_outliers(data1, 'TModA')
    check_negative_and_outliers(data1, 'TModB')

    # Repeat for the other data2
    print("Applying checks for data2")
    check_negative_and_outliers(data1, 'GHI', expected_range=(0, 4000))
    check_negative_and_outliers(data2, 'DNI', expected_range=(0, 2000))
    check_negative_and_outliers(data2, 'DHI', expected_range=(0, 2000))
    check_negative_and_outliers(data2, 'ModA')
    check_negative_and_outliers(data2, 'ModB')
    check_negative_and_outliers(data2, 'Tamb', expected_range=(-50, 50))
    check_negative_and_outliers(data2, 'RH', expected_range=(0, 100))
    check_negative_and_outliers(data2, 'WS', expected_range=(0, 100))
    check_negative_and_outliers(data2, 'WSgust', expected_range=(0, 100))
    check_negative_and_outliers(data2, 'WSstdev', expected_range=(0, 100))
    check_negative_and_outliers(data2, 'WD', expected_range=(0, 360))
    check_negative_and_outliers(data2, 'WDstdev', expected_range=(0, 360))
    check_negative_and_outliers(data2, 'BP', expected_range=(900, 1050))
    check_negative_and_outliers(data2, 'Cleaning', expected_range=(0, 1))
    check_negative_and_outliers(data2, 'Precipitation', expected_range=(0, None))
    check_negative_and_outliers(data2, 'TModA', expected_range=(-50, 50))
    check_negative_and_outliers(data2, 'TModB', expected_range=(-50, 50))
    check_negative_and_outliers(data2, 'GHI', expected_range=(0, 1000))

    # Repeat for the other data3
    print("Applying checks for data3")
    check_negative_and_outliers(data1, 'GHI', expected_range=(0, 4000))
    check_negative_and_outliers(data3, 'DNI', expected_range=(0, 2000))
    check_negative_and_outliers(data3, 'DHI', expected_range=(0, 2000))
    check_negative_and_outliers(data3, 'ModA')
    check_negative_and_outliers(data3, 'ModB')
    check_negative_and_outliers(data3, 'Tamb', expected_range=(-50, 50))
    check_negative_and_outliers(data3, 'RH', expected_range=(0, 100))
    check_negative_and_outliers(data3, 'WS', expected_range=(0, 100))
    check_negative_and_outliers(data3, 'WSgust', expected_range=(0, 100))
    check_negative_and_outliers(data3, 'WSstdev', expected_range=(0, 100))
    check_negative_and_outliers(data3, 'WD', expected_range=(0, 360))
    check_negative_and_outliers(data3, 'WDstdev', expected_range=(0, 360))
    check_negative_and_outliers(data3, 'BP', expected_range=(900, 1050))
    check_negative_and_outliers(data3, 'Cleaning', expected_range=(0, 1))
    check_negative_and_outliers(data3, 'Precipitation', expected_range=(0, None))
    check_negative_and_outliers(data3, 'TModA', expected_range=(-50, 50))
    check_negative_and_outliers(data3, 'TModB', expected_range=(-50, 50))
    check_negative_and_outliers(data3, 'GHI', expected_range=(0, 1000))

    return data1, data2, data3