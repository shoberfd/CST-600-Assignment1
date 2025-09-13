import matplotlib.pyplot as plt

def explore_data(df):
    """Performs and prints initial exploratory data analysis."""
    # Print a header for the EDA section.
    print("\n--- Exploratory Data Analysis ---")
    
    # Display general information about the DataFrame (data types, non-null counts).
    print("\nDataset Info:")
    df.info()
    
    # Generate descriptive statistics (count, mean, std, etc.) for numeric columns.
    print("\nSummary Statistics:")
    print(df.describe())
        
    # Create histograms, capturing the returned array of Axes objects
    axes = df[['Age', 'Fare']].hist(bins=30, figsize=(10, 5))
    
    # Target the specific subplots using array indexing [row, col]
    
    # Target the first plot (Age) at [0, 0]
    ax_age = axes[0, 0]
    ax_age.set_xlabel('Age (Years)')
    ax_age.set_ylabel('Frequency (Count)')

    # Target the second plot (Fare) at [0, 1]
    ax_fare = axes[0, 1]
    ax_fare.set_xlabel('Fare Amount ($)')
    ax_fare.set_ylabel('Frequency (Count)')
    
    # Keep the original suptitle (this applies to the whole figure)
    plt.suptitle('Distributions of Age and Fare')
    
    # Add tight_layout to prevent labels/titles from overlapping
    # rect adjusts the layout to make room for the suptitle
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Show the plot to the user.
    plt.show()
    
    # Print a final status message for this section.
    print("EDA complete. Visualizations displayed.")