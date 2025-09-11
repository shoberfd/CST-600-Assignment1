import matplotlib.pyplot as plt
import seaborn as sns

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
    
    # Create histograms for 'Age' and 'Fare' to visualize their distributions.
    df[['Age', 'Fare']].hist(bins=30, figsize=(10, 5))
    plt.suptitle('Distributions of Age and Fare')
    
    # Show the plot to the user.
    plt.show()

    # Create a boxplot for 'Fare' to visually identify outliers.
    sns.boxplot(x=df['Fare'])
    plt.title('Boxplot of Ticket Fare')
    
    # Show the plot to the user.
    plt.show()
    
    # Print a final status message for this section.
    print("EDA complete. Visualizations displayed.")