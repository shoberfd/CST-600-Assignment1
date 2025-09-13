# Customer Transaction Analysis Project

This project focuses on the exploratory data analysis (EDA), cleaning, outlier handling, and feature engineering of a customer dataset. The goal is to prepare the data for downstream machine learning modeling by improving its quality and deriving insightful features.

## Business Scenario

As a Data Scientist, I am tasked with evaluating customer-transaction data to improve operational decision-making. This involves exploring the dataset to find initial insights, addressing data quality issues like missing values and outliers, and engineering new features that could strengthen predictive models.

## Dataset

* **Source:** [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
* **Description:** This is a classic dataset containing demographic and passenger information for 891 of the 2,224 passengers and crew on board the Titanic. It is often used to predict survival based on features like age, class, and gender.

## Environment Setup

This project uses Python 3.10+. To set up the environment and install dependencies, follow these steps from the project's root directory:

1.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    py -3 -m venv .venv
    .venv\Scripts\activate
    ```
2.  **Install required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

With the virtual environment activated, run the main script from the root directory:

```bash
python src/main.py
```

The script will execute the full pipeline: loading the data, performing EDA, cleaning, feature engineering, and printing the head of the final, processed DataFrame.

## Summary of Steps and Decisions

1.  **Exploratory Data Analysis (EDA):**
    * Initial analysis revealed missing values in the `Age` and `Cabin` columns.
    * The `Fare` column showed significant right-skewness and numerous outliers, as seen in its boxplot.
2.  **Data Cleaning:**
    * **Missing `Age`:** Imputed with the median age. The median is more robust to outliers than the mean, making it a better choice for a skewed distribution.
    * **Missing `Cabin`:** The column was dropped entirely as over 77% of its values were missing, making imputation unreliable.
3.  **Outlier Handling:**
    * **`Fare` Outliers:** Detected using the IQR (Interquartile Range) method. Outliers were **capped** at the upper bound (Q3 + 1.5 * IQR) instead of being removed to retain valuable information without distorting model training.
4.  **Feature Engineering:**
    * `FamilySize`: Created by summing `SibSp` (siblings/spouses) and `Parch` (parents/children) plus 1 (for the passenger themselves). This feature consolidates family information.
    * `IsAlone`: A binary feature derived from `FamilySize`. It is 1 if `FamilySize` is 1, and 0 otherwise, simplifying the family context.
5.  **Scaling:**
    * `StandardScaler` was applied to the numerical columns (`Age`, `Fare`, `FamilySize`). This was chosen to normalize the features, giving them a mean of 0 and a standard deviation of 1. This is a standard prerequisite for many machine learning algorithms like SVMs and logistic regression.