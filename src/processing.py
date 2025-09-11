import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def clean_data(df):
    """Handles missing values and outliers in the dataframe."""
    # Print a header for the data cleaning section.
    print("\n--- Data Cleaning and Handling ---")
    
    # Calculate the median of the 'Age' column to use for imputation.
    age_median = df['Age'].median()
    # Fill any missing ('NaN') values in the 'Age' column with the calculated median.
    df['Age'].fillna(age_median, inplace=True)
    # Confirm the action and the value used for imputation.
    print(f"Missing 'Age' values imputed with median: {age_median:.2f}")

    # Drop the 'Cabin' column from the DataFrame. The 'axis=1' specifies a column.
    df.drop('Cabin', axis=1, inplace=True)
    # Justify why the column was dropped.
    print("'Cabin' column dropped due to excessive missing values.")
    
    # Calculate the first (Q1) and third (Q3) quartiles for the 'Fare' column.
    Q1 = df['Fare'].quantile(0.25)
    Q3 = df['Fare'].quantile(0.75)
    # Calculate the Interquartile Range (IQR).
    IQR = Q3 - Q1
    # Define the upper bound for outlier detection (anything above this is an outlier).
    upper_bound = Q3 + 1.5 * IQR
    
    # Use numpy's 'where' to cap the values in 'Fare'.
    # If a value is greater than upper_bound, it's replaced with upper_bound; otherwise, it stays the same.
    df['Fare'] = np.where(df['Fare'] > upper_bound, upper_bound, df['Fare'])
    print(f"Outliers in 'Fare' capped at the upper bound: {upper_bound:.2f}")
    
    # Use an assertion to programmatically check that there are no nulls left in 'Age'.
    # If the condition is false, the program will stop with an error.
    assert df['Age'].isnull().sum() == 0, "NaNs still exist in Age column."
    
    print("Data cleaning complete.")
    return df

def engineer_features(df):
    """Creates new features and applies scaling."""
    # Print a header for the feature engineering section.
    print("\n--- Feature Engineering and Scaling ---")
    
    # Create the 'FamilySize' feature by summing sibling/spouse and parent/child counts, plus 1 for the passenger.
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    print("Created 'FamilySize' feature.")

    # Create the 'IsAlone' feature by checking if 'FamilySize' is 1.
    # Convert the boolean result (True/False) to an integer (1/0).
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    print("Created 'IsAlone' feature.")

    # Instantiate the StandardScaler object.
    scaler = StandardScaler()
    # Define the list of numeric columns that need to be scaled.
    numeric_cols = ['Age', 'Fare', 'FamilySize']
    # Fit the scaler to the data and transform it, updating the columns in the DataFrame.
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print(f"Applied StandardScaler to: {', '.join(numeric_cols)}")
    
    print("Feature engineering complete.")
    return df