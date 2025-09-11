# Import the functions from our other project files.
from data_loader import load_data
from analysis import explore_data
from processing import clean_data, engineer_features

def main():
    """Main function to run the data processing pipeline."""
    # Define the relative path to the dataset.
    # The '..' means 'go up one directory' from src to the project root.
    filepath = 'data/titanic.csv'
    
    # --- Pipeline Execution ---
    # 1. Load the data using the imported function.
    df = load_data(filepath)
    
    # 2. Perform EDA. We pass a copy of the df to prevent any accidental changes.
    explore_data(df.copy())
    
    # 3. Clean the data (handle missing values and outliers).
    df_cleaned = clean_data(df.copy())
    
    # 4. Engineer new features and scale the data.
    df_engineered = engineer_features(df_cleaned.copy())
    
    # --- Final Output ---
    # Print a header for the final output section.
    print("\n--- Final Processed Data Head ---")
    # Display the first 5 rows of the fully processed DataFrame.
    print(df_engineered.head())
    
    print("\nProject script finished successfully! ✨")

# This standard Python construct ensures that the main() function is called
# only when this script is executed directly.
if __name__ == "__main__":
    main()