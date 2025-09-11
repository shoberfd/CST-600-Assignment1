import pandas as pd

def load_data(filepath):
    """Loads the dataset from a specified filepath."""
    # Print a status message to the console.
    print("Loading data...")
    
    # Use pandas' read_csv function to load the dataset into a DataFrame.
    df = pd.read_csv(filepath)
    
    # Confirm that the data has been loaded successfully.
    print("Data loaded successfully.")
    
    # Return the loaded DataFrame so it can be used by other functions.
    return df